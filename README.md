# AccessControlApp

Main functionalities:
- client management
- access control with physical gates

The AccessControlApp is meant to do access control, and can run on the edge, 
connecting to the physical hardware like gates. 
The app provides a database, python backend and a webserver for frontend.



## Installation

To install this application on a production ready device, 
simply execute `raspberry_setup.sh` and the app should be up and running. 


## Development

To develop further on this project, you can run the application locally and write python in the
/api folder. You might restart the container running `docker compose up` while developping.

To develop the frontend, it's best practise to `npm install` and `yarn serve` in the web folder,
so you can develop quite fast. In the ./dist folder your project is build. 

You can deploy by rebuilding the images and pushing them to ducker hub.


## Roadmap

- building and using the created docker images to deploy on production
- Build a frontend in Vue.js
    - Client management
    - Access management
- Control physical gates for access control
- Build a eid integration for new customers
- Build NFC integration for logins
- Find a way to upgrade database schema's without rebuilding the entire database
- Try to make the total application smaller in disksize
