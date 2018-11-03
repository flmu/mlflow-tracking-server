# TODO
- Section: Prerequisite
- Section: Test the MLFlow Tracking Server
- Share the results in the corresponding threads


# Docker image of MLFLow Tracking Server

[![Build Status](https://travis-ci.org/flmu/mlflow-tracking-server.svg?branch=master)](https://travis-ci.org/flmu/mlflow-tracking-server)

This repo provides a docker image of [MLFLow Tracking Server](https://www.mlflow.org/docs/latest/tracking.html) based on an internal file system for metadata (e.g. parameters, metrics) and an [AWS S3 bucket](https://aws.amazon.com/s3/) for [files and artifacts](https://www.mlflow.org/docs/latest/tracking.html#storage).

## Prerequisite
Before you start the MLFlow Tracking Server, you must create an AWS Bucket and the corresponding credentials.
1. AWS Bucket: TODO
2. AWS Credentials for your bucket: TODO

## Run the MLFlow Tracking Server

```bash
$ docker run \
    --rm \
    --name mlflow-tracking-server \
    -p 5000:5000 \
    -e PORT=5000 \
    -e FILE_DIR=/mlflow \
    -e AWS_BUCKET=<YOUR_AWS_BUCKET> \
    -e AWS_ACCESS_KEY_ID=<YOUR_AWS_ACCESS_KEY_ID> \
    -e AWS_SECRET_ACCESS_KEY=<YOUR_AWS_SECRET_ACCESS_KEY> \
    foxrider/mlflow-tracking-server:0.2.0
```

Access to http://127.0.0.1:5000

## Environment variables

### Required

|Key|Description|
|---|---|
|`FILE_DIR`|Directory for artifacts and metadata (e.g. parameters, metrics)|
|`AWS_BUCKET`|Name of AWS Bucket that will contain the artifacts|
|`AWS_ACCESS_KEY_ID`|AWS-Access-Key that you have created in the `Prerequisite` section|
|`AWS_SECRET_ACCESS_KEY`|AWS-Secret-Access-Key that you have created in the `Prerequisite` section|

### Optional

|Key|Description|Default|
|---|---|---|
|`PORT`|Value for `listen` directive|`5000`|

## Test the MLFlow Tracking Server
TODO
- AWS_SECRET_ACCESS_KEY + AWS_ACCESS_KEY_ID on client side or ~/.aws/credentials
- Client Example: my example + mlflow example (mlflow experiments create hello_world_experiment + MLFLOW_EXPERIMENT_ID=<Number> python examples/train.py)
- AWS Bucket Subfolder

## Author

Florian Muchow ([@flmu](https://github.com/flmu))
