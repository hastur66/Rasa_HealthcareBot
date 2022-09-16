FROM rasa/rasa-sdk:2.2.0

WORKDIR /app

COPY ./requirements.txt ./

USER root
RUN apt-get update && apt-get install
RUN pip3 install --upgrade setuptools pip
RUN pip install -r requirements.txt

EXPOSE 5055
