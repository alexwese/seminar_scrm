FROM python:3.8

RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir pandas
RUN pip3 install --no-cache-dir numpy
RUN pip3 install --no-cache-dir matplotlib
RUN pip3 install --no-cache-dir nltk
RUN pip3 install --no-cache-dir tika
RUN pip3 install --no-cache-dir wordcloud
RUN pip3 install --no-cache-dir pattern
#RUN pip3 install --no-cache-dir PIL


RUN apt-get update \
 && apt-get install -y \
      git \
      unzip \
 && rm -rf /var/lib/apt/lists/*

# Install OpenJDK-11
RUN apt-get update && \
    apt-get install -y openjdk-11-jre-headless && \
    apt-get clean;

COPY TextMiner.py /
COPY TextMiner2.py /
COPY DocumentsSCRM /DocumentsSCRM/

CMD ["python", "TextMiner.py"]