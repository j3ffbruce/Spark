FROM bitnami/spark:latest

USER root
RUN apt-get update && apt-get install -y python3-pip

RUN pip3 install numpy pandas pytest py4j

RUN mkdir -p /scripts/project_01/.pytest_cache && chmod -R 777 /scripts/project_01/.pytest_cache

USER root