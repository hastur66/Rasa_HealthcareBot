FROM rasa/rasa:2.2.8-full

WORKDIR /app

COPY ./requirements.txt ./

USER root
RUN apt-get --allow-releaseinfo-change update
RUN apt-get -y install software-properties-common
RUN apt-get --allow-releaseinfo-change update
#RUN apt-get -y install ffmpeg
RUN pip3 install --upgrade setuptools pip
#RUN pip install -r requirements.txt

EXPOSE 5005
