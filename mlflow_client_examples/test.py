import os
from random import random, randint
import mlflow

if __name__ == "__main__":
    print("Running the test script ...")

    #Connect to tracking server
    mlflow.set_tracking_uri("http://127.0.0.1:5000")

    #Create directory for artifacts
    if not os.path.exists("artifact_folder"):
        os.makedirs("artifact_folder")

    #Test parametes
    mlflow.log_param("param1", randint(0, 100))

    #Test metrics
    mlflow.log_metric("metric1", random())
    mlflow.log_metric("metric1", random())
    mlflow.log_metric("metric1", random())
    mlflow.log_metric("metric1", random())

    #Test artifact
    with open("artifact_folder/test.txt", "w") as f:
        f.write("hello world!")
    mlflow.log_artifacts("artifact_folder")
