#!/bin/bash
cd mlflow_tracking_server && docker build --no-cache -t mlflow-tracking-server:0.2.0 .
