FROM ubuntu:18.04

RUN apt-get update && apt-get install -y python3 python3-pip sudo

RUN useradd -m akash

RUN chown -R akash:akash /home/akash/

COPY --chown . /home/akash/app/

USER akash

RUN cd /home/akash/app/ && pip3 install -r requirements.txt

WORKDIR /home/akash/app