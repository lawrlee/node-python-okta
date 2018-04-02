FROM python:3.6-stretch

RUN mkdir /api
WORKDIR /api
ADD . /api

RUN apt-get update -y && apt-get install -y \
    apt-transport-https \
    build-essential \
    curl \
    git \
    libssl-dev \
    libfontconfig1 \
    libfreetype6 \
    libgif-dev \
    libjpeg62-turbo \
    libtiff5 \
    libxml2 \
    wget

## Install node
#ENV NPM_CONFIG_LOGLEVEL info
#ENV NODE_VERSION 6.14.0
#RUN curl https://nodejs.org/dist/v${NODE_VERSION}/node-v${NODE_VERSION}-linux-x64.tar.xz | tar -C /usr/local --strip-components 1 -Jxv
#
## Install yarn
#RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
#RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list
#
#RUN apt-get update -y && apt-get install -y \
#    yarn \
#&& apt-get clean && rm -rf /var/lib/apt/lists/*
#
#RUN yarn global add serverless
#RUN yarn install

RUN pip install -r requirements.txt

CMD FLASK_APP=app.py python -m flask run --host=0.0.0.0