
FROM ubuntu

# Install OpenJDK-11

RUN apt-get update && \
    apt-get install -y openjdk-18-jre-headless && \
    apt-get clean

## install python 

RUN apt-get install -y python3

## install rytr api situation

RUN set -xe \
    && apt-get update \
    && apt-get install -y python3-pip

RUN pip install rytrme_api_python

RUN pip install flask

## copy only the artifacts we need from the first stage and discard the rest

COPY  /calling-python-situation-test-1.0-SNAPSHOT-jar-with-dependencies.jar /text-format-dashboard-online-api.jar
COPY . /

##COPY  /calling-python-situation-test-1.0-SNAPSHOT-jar-with-dependencies.jar /text-format-dashboard-online-api.jar

# set the startup command to execute the jar

CMD ["java", "-jar", "/text-format-dashboard-online-api.jar"]
