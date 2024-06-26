# Twitter Clone

This project implements a simplified Twitter clone application built with 
Python and Node.js. It utilizes MongoDB as the database, XML-RPC for 
communication between the Python server and client and RESTful API in the 
Node.js server.

## Features

* User Management:
    * Users can sign up with a username and password. Duplicate usernames are not allowed.
    * Users can log in with their credentials.
* Posting:
    * Users can create and publish tweets containing text, hashtags, and a timestamp.
* Feed:
    * Users can view the 10 most recent tweets.
* Interactions:
    * Users can like and comment on existing tweets.
* Search:
    * Users can search for tweets based on hashtags.

## Technology Stack

* Programming Languages: Python, JavaScript
* Database: MongoDB
* Communication Protocol: XML-RPC, RESTful API (via Node.js)

## Running the application

All installation methods requires you to clone the repository and set
the repository root as your current working directory:

```
$ git clone https://github.com/Jackgito/DistributedSystemsProject.git
$ cd DistributedSystemsProject
```

The client can be run with python, but requires functional servers in order to 
operate:

```
$ python3 -m venv client-env
$ ./client-env/bin/python3 client/client.py
```

### Docker compose

This method requires docker to be installed on your system.

Clone the repository and execute docker compose, which will setup the 
node server, python server and mongodb.

```
$ docker compose up -d
```

### Manual deployment

##### Requirements

   * Node version 18 or newer
   * Python 3.11 or newer
   
##### Node server

Install required packages using npm and run server.js using node.

```
$ cd node-server
$ npm install
$ node server.js
```

By default node-server requires mongodb to be run `localhost:27017` and will
by default expose itself on port `5000`. These can be configured with env
variables:

```
$ export SERVER_PORT=<node-server-port> # Default is 5000

$ export MONGO_HOST=<mongo-host> # Default is "localhost"
$ export MONGO_PORT=<mongo-port> # Default is 27017

$ node server.js
```

##### MongoDB server

Make sure you have the mongodb server runnign on port `27017`, if you
have docker installed, you can run the following command to get mongodb
running:

```
$ docker run --name mongodb -d -p 27017:27017 mongodb/mongodb-community-server:latest
```

##### Python server

Create python environment, install requirements and launch the server 
application.

```
$ python3 -m venv server-env
$ ./server-env/bin/pip3 install -r server/requirements.txt
$ ./server-env/bin/python3 server/server.py
```

Python server will by default be run on `localhost:3000` and will require
by default node-server to be run on `localhost:5000`. These can be configured
with env variables:

```
$ export NODE_SERVER_HOST=<node-server-host> # Default is "localhost"
$ export NODE_SERVER_PORT=<node-server-port> # Default is 5000

$ export PYTHON_SERVER_HOST=<python-server-host> # Default is "localhost"
$ export PYTHON_SERVER_PORT=<python-server-port> # Default is 3000

$ ./server-env/bin/python3 server/server.py
```

The env variables have different values when deploying with docker compose,
the values can be found from the `docker-compose.yml` file on repo root.

## Code Structure

The codebase is divided into three main parts:

* **node-server/server.js:** Handles the interactions with MongoDB through RETSTful API, including user management, post creation, and post fetching. This server utilizes Express.js and Mongoose to manage routes and data schema. 
* **server/server.py:** Handles communication between the Python client and the Node.js server. Processes client requests, communicates with the Node:js server via HTTP requests and handles XML-RPC responses to the client.
* **client/client.py:** This file implements the client-side interface. It uses the `xmlrpc.client` library to communicate with the server and displays menus for various user actions like viewing posts, creating posts, searching, and signing out. Additionally, separate modules handle functionalities like authentication, post creation, and search.
