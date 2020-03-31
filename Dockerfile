FROM debian:buster
RUN apt-get update -y
RUN apt-get install -y -q python3-pip wget git fonts-noto-core libfreetype6-dev libharfbuzz-dev libfribidi-dev libglib2.0-dev
RUN echo "clone repo"
RUN git clone -q https://github.com/python-pillow/Pillow.git
WORKDIR ./Pillow/depends/
RUN ./install_raqm.sh
RUN pip3 install pillow
COPY ./files/test.py ./test.py
RUN python3 ./test.py