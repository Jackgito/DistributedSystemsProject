**Twitter Clone**

This project implements a simplified Twitter clone application built with Python and Node.js. It utilizes MongoDB as the database, XML-RPC for communication between the Python server and client and RESTful API in the Node.js server.

**Features:**

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

**Technology Stack:**

* Programming Languages: Python, JavaScript
* Database: MongoDB
* Communication Protocol: XML-RPC, RESTful API (via Node.js)

**Running the Application:**

1. **Node.js Server:**
    * Navigate to the node-server directory.
    * Run `npm install` to install dependencies.
    * Start the server with `node server.js` to handle database operations.
2. **Python Server**
    * Ensure you have MongoDB running locally (port 27017 by default).
    * Open a terminal in the project directory and run: `python server.py`
3. **Client:**
    * Open a separate terminal in the project directory and run: `python client.py`

**Code Structure:**

The codebase is divided into three main parts:

* **node-server/server.js:** Handles the interactions with MongoDB through RETSTful API, including user management, post creation, and post fetching. This server utilizes Express.js and Mongoose to manage routes and data schema. 
* **server.py:** Handles communication between the Python client and the Node.js server. Processes client requests, communicates with the Node:js server via HTTP requests and handles XML-RPC responses to the client.
* **client.py:** This file implements the client-side interface. It uses the `xmlrpc.client` library to communicate with the server and displays menus for various user actions like viewing posts, creating posts, searching, and signing out. Additionally, separate modules handle functionalities like authentication, post creation, and search.
