import requests
from django.utils import timezone
from django.db.models import Q
from django.core.mail import EmailMessage, send_mail

import graphene
from graphene import relay, ObjectType
from graphene.types.generic import GenericScalar
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from graphql_relay import from_global_id
from graphene_file_upload.scalars import Upload
from graphql_jwt.decorators import login_required, superuser_required

from .models import Post
# from .models import *

class PostNode(DjangoObjectType):
    details_description = GenericScalar()

    class Meta:
        model = Post
        # filter_fields = ['title','author__first_name']
        filter_fields = {
            'title': ['icontains']
        }
        fields = "__all__"
        # exclude = ('is_archived',)
        interfaces = (relay.Node,)

    def resolve_image(self, info):
        """Resolve product photo absolute path"""
        if self.image:
            self.image = info.context.build_absolute_uri(self.image.url)
        return self.image



class PostMutation(relay.ClientIDMutation): # Create_or_Update
    class Input:
        id = graphene.ID()  
        title = graphene.String()
        image = Upload() # Upload Image
        description = graphene.String()
        details_description = GenericScalar() # RichTextField 
        is_active = graphene.Boolean(default_value=True)
        is_archived = graphene.Boolean(default_value=False)
        
    instance = graphene.Field(PostNode) 
      
    @classmethod
    @login_required
    def mutate_and_get_payload(cls, root, info, **input):
        
        user = info.context.user
        
        id = input.get("id")
        title = input.get("title")
        image = input.get("image")
        description = input.get("description")
        details_description = input.get("details_description")
        is_active = input.get("is_active")
        is_archived = input.get("is_archived")
        
        if id is not None:
            pk = from_global_id(id)[1]
            try:
                instance = Post.objects.get(id=pk)
            except:
                raise Exception("Object not found.")
            
            if instance:
                if instance.author == user:
                    instance.title = title if title is not None else instance.title
                    instance.image = image if image is not None else instance.image
                    instance.description = description if description is not None else instance.description
                    instance.details_description = details_description if details_description is not None else instance.details_description
                    instance.is_active = is_active if is_active is not None else instance.is_active
                    instance.is_archived = is_archived if is_archived is not None else instance.is_archived
                else:
                    raise Exception("You don't have permission to update.")
        else:    
            instance = Post.objects.create(
                title = title,
                image = image,
                description = description,
                details_description = details_description,
                is_active = is_active, 
                is_archived = False,
                author = user
            )
            
        return PostMutation(instance=instance)
    
    
class PostDelete(graphene.Mutation):
    message = graphene.String()
    is_success = graphene.Boolean()
    class Input:
        id = graphene.ID()
        
    instance = graphene.Field(PostNode)
        
    @classmethod
    @login_required 
    def mutate(cls, root, info, **input):
        user = info.context.user
        id = input.get("id")
        message = "Somethings went wrong."
        is_success = False
        
        if id is not None:
            id = from_global_id(id)[1]
            # print("--------------id-----------------:", id)
            try:
                instance = Post.objects.get(id=id)                    
            except:
                raise Exception("Object does not exist.")
            if instance:
                if instance.user == user:
                    instance.delete()
                    message = "Successfully deleted your object."
                    is_success = True
                else:
                    raise Exception("Permission Denied")
                        
        return cls(message=message, is_success=is_success)
