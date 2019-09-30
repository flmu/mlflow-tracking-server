FROM python:3.7

LABEL maintainer "Florian Muchow <flmuchow@gmail.com>"

RUN pip install mlflow==1.2.0 && \
    pip install awscli --upgrade --user && \
    pip install boto3==1.9.237

ENV PORT 5000
ENV AWS_BUCKET bucket
ENV AWS_ACCESS_KEY_ID aws_id
ENV AWS_SECRET_ACCESS_KEY aws_key

COPY files/run.sh /

ENTRYPOINT ["/run.sh"]
