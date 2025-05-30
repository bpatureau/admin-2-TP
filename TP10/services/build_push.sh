#!/bin/bash

set -e

username="maxion78"
version="1.0"

# Microservices
docker build -t $username/woody_product:$version api/product_service
docker build -t $username/woody_order:$version api/order_service
docker build -t $username/woody_misc:$version api/misc_service
docker build -t $username/woody_order_worker:$version api/order_worker

# Autres services
docker build -t $username/woody_rp:$version reverse-proxy
docker build -t $username/woody_database:$version database
docker build -t $username/woody_front:$version front

# Tags latest
docker tag $username/woody_product:$version $username/woody_product:latest
docker tag $username/woody_order:$version $username/woody_order:latest
docker tag $username/woody_misc:$version $username/woody_misc:latest
docker tag $username/woody_order_worker:$version $username/woody_order_worker:latest

docker tag $username/woody_rp:$version $username/woody_rp:latest
docker tag $username/woody_database:$version $username/woody_database:latest
docker tag $username/woody_front:$version $username/woody_front:latest

# Push
docker login

docker push $username/woody_product:$version
docker push $username/woody_product:latest
docker push $username/woody_order:$version
docker push $username/woody_order:latest
docker push $username/woody_misc:$version
docker push $username/woody_misc:latest
docker push $username/woody_order_worker:$version
docker push $username/woody_order_worker:latest

docker push $username/woody_rp:$version
docker push $username/woody_rp:latest
docker push $username/woody_database:$version
docker push $username/woody_database:latest
docker push $username/woody_front:$version
docker push $username/woody_front:latest