#!/bin/bash
docker login -u "$DOCKER_USERNAME" --password-stdin
docker build --no-cache -t mlflow-tracking-server:0.1.0 .
docker tag mlflow-tracking-server:0.1.0 foxrider/mlflow-tracking-server:0.1.0
docker push mlflow-tracking-server:0.1.0
