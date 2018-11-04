import os
from random import random, randint
import mlflow

if __name__ == "__main__":
    print("Running the test script ...")

    mlflow.set_tracking_uri("http://127.0.0.1:5000")

    if not os.path.exists("artifact_folder"):
        os.makedirs("artifact_folder")

    mlflow.log_param("param1", randint(0, 100))

    mlflow.log_metric("foo", random())
    mlflow.log_metric("foo", random() + 1)
    mlflow.log_metric("foo", random() + 2)

    with open("artifact_folder/test.txt", "w") as f:
        f.write("hello world!")

    mlflow.log_artifacts("artifact_folder")
