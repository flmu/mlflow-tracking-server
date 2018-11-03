FROM python:3.7.0

LABEL maintainer "Florian Muchow <flmuchow@gmail.com>"

RUN pip install mlflow
RUN pip install awscli --upgrade --user

ENV PORT 5000
ENV AWS_BUCKET bucket
ENV AWS_ACCESS_KEY_ID aws_id
ENV AWS_SECRET_ACCESS_KEY aws_key

COPY files/run.sh /

ENTRYPOINT ["/run.sh"]
