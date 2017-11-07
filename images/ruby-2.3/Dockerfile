# Copyright 2017 The Kubernetes Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Includes go and gcloud
FROM ruby:2.3
LABEL maintainer="christian.simon@jetstack.io"


# Install virtualbox package url
ADD https://www.virtualbox.org/download/oracle_vbox_2016.asc /tmp/oracle_vbox_2016.asc
RUN echo "deb http://download.virtualbox.org/virtualbox/debian jessie contrib" > /etc/apt/sources.list.d/virtualbox.list \
 && cat /tmp/oracle_vbox_2016.asc | apt-key add -

RUN apt-get update && apt-get install -y \
    python \
    git \
    dkms \
    virtualbox-5.1 \
    curl \
    zlib1g-dev \
    build-essential \
    libc++-dev \
    ruby-dev \
    libssl-dev \
    libreadline-dev \
    libyaml-dev \
    libsqlite3-dev \
    sqlite3 \
    libxml2-dev \
    libxslt1-dev \
    libcurl4-openssl-dev \
    python-software-properties \
    libffi-dev \
    nodejs \
    rsync \
    wget && \
    apt-get clean


# Download and install vagrant
RUN curl -sL -o /tmp/vagrant.deb https://releases.hashicorp.com/vagrant/1.9.5/vagrant_1.9.5_x86_64.deb \
 && echo "5c2d841c88589c929b6b24e8d7fc443b8b76c809c5ad600a7c192fc794fa329a  /tmp/vagrant.deb" | sha256sum -c \
 && DEBIAN_FRONTEND=noninteractive dpkg -i /tmp/vagrant.deb \
 && rm /tmp/vagrant.deb


ENV GCLOUD_VERSION 163.0.0
RUN wget https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-$GCLOUD_VERSION-linux-x86_64.tar.gz && \
    tar xf google-cloud-sdk-$GCLOUD_VERSION-linux-x86_64.tar.gz -C / && \
    rm google-cloud-sdk-$GCLOUD_VERSION-linux-x86_64.tar.gz && \
    /google-cloud-sdk/install.sh
ENV PATH "/google-cloud-sdk/bin:${PATH}"

WORKDIR /workspace
ADD runner /
ENTRYPOINT ["/bin/bash", "/runner"]
