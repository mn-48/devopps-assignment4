# Create Docker image and push it Private repository docker hub
```
docker build -t emv2-django-backend .
```
```
docker tag emv2-django-backend mdnazmulhossain/emv2-django-backend
```
```
docker push mdnazmulhossain/emv2-django-backend
```
# Puss image as backend tag
# Create Docker image and push it Private repository docker hub

```
docker tag emv2-django-backend mdnazmulhossain/emv2-django-backend:backend
```
```
docker push mdnazmulhossain/emv2-django-backend:backend
```

# ECS Connect to docker hub private repository
```
ECS_ENGINE_AUTH_TYPE=docker
ECS_ENGINE_AUTH_DATA={"https://index.docker.io/v1/":{"username":"mdnazmulhossain","password":"Mn@150148","email":"nazmul.cse48@gmail.com"}}
```

[help](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/private-auth-container-instances.html)


docker build -t em-nextjs:nextjs-v2 ./frontend


# ======================================================================
# ========================= AWS ECR ====================================

# install awscli

```
sudo apt-get update
```
```
sudo apt-get install awscli
```

# See version
```
aws --version
```
# Configure awscli 
```
aws configure
```
```

AWS_ACCESS_KEY_ID = 

AWS_SECRET_ACCESS_KEY =

Region: ap-south-1

format: json

aws ecr get-login-password --region ap-south-1 | docker login --username AWS --password-stdin 435786908364.dkr.ecr.ap-south-1.amazonaws.com

```

# backend dockerized and push to AWS ECR
```
docker build -t emv2-django-backend:dj-v2 ./backend
```
```
docker tag emv2-django-backend:dj-v2 435786908364.dkr.ecr.ap-south-1.amazonaws.com/ehsanmarketing-ecr:dj-v2
```
```
docker push 747575259476.dkr.ecr.ap-south-1.amazonaws.com/ehsanmarketing-v2:dj-v2
```

# frontend dockerized and push to AWS ECR

```
docker build -t emv2-nextjs-frontend:nextjs-v1 ./frontend

docker tag emv2-nextjs-frontend:nextjs-v1 435786908364.dkr.ecr.ap-south-1.amazonaws.com/ehsanmarketing-ecr:nextjs-v1

docker push 435786908364.dkr.ecr.ap-south-1.amazonaws.com/ehsanmarketing-ecr:nextjs-v1
```
*docker run -p 3000:3000 435786908364.dkr.ecr.ap-south-1.amazonaws.com/ehsanmarketing-ecr:nextjs-v1*


# Docker CMD
## Stop and Delete Container: 

  ```
  # stop all container
  docker stop $(docker ps -a -q)

  # Delete all stopped containers: 
  docker rm $(docker ps -a -q)
  # docker container prune
 
  # Delete all Docker images
  docker rmi $(docker images -q)
  
  ```
  
  ```
  docker container prune
  ```
  
  ```
  docker image prune
  ```

  ```
  docker rmi -f image_id
  ```

  ```
  docker volume prune
  ```

  ```
  docker network prune
  ```

  
  #### Deploy NextJs AWS EC2

  # Update EC2 Instances

  ```sudo apt-get update```

  # 1 Install NodeJs

  ```sudo apt install nodejs```

# Install npm

```sudo apt install npm```

>yes

# Create new NextJs Project

```npx create-next-app@latest```

*What is project name?* ```frontend```

```cd frontend```

```npm run dev```



# Install Nginx

```sudo apt install nginx```

> yes

# See nginx status

```sudo systemctl status nginx.service```

*Change inbound rules of security groups*


# Important 

1. sites-available 
2. sites-enable

```cd /etc/nginx/sites-available```

```touch myApp.conf```

```
server {
  listen 80;
  listen [::]:80;
  server_name ip_address domain_name;

  location / {
    include proxy_params;
    proxy_pass http://localhost:3000;
  }
}

```
# link sites-available <-------> sites-enable

```sudo ln /etc/nginx/sites-available/myApp.conf /etc/nginx/sites-enable```

# test nginx

```sudo nginx -t```

# restyart nginx

```sudo systemctl restart nginx.service```

```npm run dev```

# Create Jobs to Host app

```sudo nano /etc/systemd/system/myAPP.sercice```


```
[Unit]
Description=This service will run npm dev
After=network.target



[Service]
User=ubuntu
Group=www-data



WorkingDirectory=/home/ubuntu/frontend
ExecStart=npm run dev
[Install]
WantedBy=multi-user.target

```

## This is important to restart service / After update code run this cmd
```sudo systemctl restart myAPP.sercice```

```
npm run build && npm start
```


# Create New user name as nextjsuser:
```
sudo adduser nextjsuser
```
nextjsuser1234
#  Granting Administrative Privileges:
```
sudo usermod -aG sudo nextjsuser
```

# Setting Up a Basic Firewall

```
sudo ufw app list
```

```
Output
Available applications:
  OpenSSH
```

```
sudo ufw allow OpenSSH
```

```
sudo ufw enable
```

```
sudo ufw status
```