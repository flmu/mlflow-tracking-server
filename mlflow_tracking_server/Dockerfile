FROM python:3.9

LABEL maintainer "Florian Muchow <flmuchow@gmail.com>"

RUN pip install --upgrade pip && \
    pip install awscli --upgrade --user && \
    pip install boto3==1.34.158 && \
    pip install mlflow==2.15.1

ENV PORT 5000

COPY files/run.sh /

CMD ["/run.sh"]
