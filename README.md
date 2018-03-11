# Load Balancer Example
This is a simple example to create a load balancer. Here we will use the nginx as load balancer and two simple httpserver in python3

#Create the image
```
docker build -t image_name .
```

#Run
```
docker-compose scale app=3 nginx=1
```
