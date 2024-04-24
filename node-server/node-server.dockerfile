FROM node:20.12.2-buster

WORKDIR /usr/src/app

COPY package*.json ./
RUN npm install
COPY . .

ENV MONGO_HOST=${MONGO_HOST:-mongodb}
ENV MONGO_PORT=${MONGO_PORT:-27017}
EXPOSE 5001
CMD [ "node", "server.js" ]
