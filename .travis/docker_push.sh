#!/bin/bash
echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
cd mlflow_tracking_server && docker build --no-cache -t mlflow-tracking-server:0.3.0 .
docker tag mlflow-tracking-server:0.3.0 foxrider/mlflow-tracking-server:0.3.0
docker push foxrider/mlflow-tracking-server:0.3.0
