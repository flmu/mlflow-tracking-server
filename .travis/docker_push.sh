#!/bin/bash
echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
docker build --no-cache -t mlflow-tracking-server:0.1.1 .
docker tag mlflow-tracking-server:0.1.1 foxrider/mlflow-tracking-server:0.1.1
docker push foxrider/mlflow-tracking-server:0.1.1
