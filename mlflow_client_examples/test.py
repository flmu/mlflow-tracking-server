import os
from random import random, randint
import mlflow
from mlflow.utils.file_utils import (build_path)

if __name__ == "__main__":
    print("Running mlflow_tracking.py")

    mlflow.set_tracking_uri("http://127.0.0.1:5000")


    if not os.path.exists("/Users/Florian/Desktop/mlflow"):
        os.makedirs("/Users/Florian/Desktop/mlflow")

    mlflow.log_param("param1", randint(0, 100))

    mlflow.log_metric("foo", random())
    mlflow.log_metric("foo", random() + 1)
    mlflow.log_metric("foo", random() + 2)


    with open("/Users/Florian/Desktop/mlflow/test.txt", "w") as f:
        f.write("hello world!")

    mlflow.log_artifacts("mlflow")