FROM node:6.14-stretch

RUN mkdir /web
WORKDIR /web
ADD . /web

RUN yarn global add serverless create-react-app
RUN yarn install

CMD yarn start