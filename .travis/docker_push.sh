#!/bin/bash
echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
cd mlflow_tracking_server && docker build --no-cache -t mlflow-tracking-server:0.2.0 .
docker tag mlflow-tracking-server:0.1.1 foxrider/mlflow-tracking-server:0.1.1
docker push foxrider/mlflow-tracking-server:0.1.1
