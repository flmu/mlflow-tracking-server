FROM python:3.9

LABEL maintainer "Florian Muchow <flmuchow@gmail.com>"

RUN pip install mlflow==1.13 && \
    pip install awscli --upgrade --user && \
    pip install boto3==1.16.46

ENV PORT 5000

COPY files/run.sh /

ENTRYPOINT ["/run.sh"]
