# node-python-okta

Sample deployment of a node front-end reading from a Python backend using Okta authentication and jwt.

# Deployment

    $ docker-compose up

This spins up a node container serving the front-end on port 3000 and a Flask container serving the back-end
on port 5000

# Client Authentication (Node) Resources

* https://github.com/okta/samples-js-react
* https://developer.okta.com/quickstart/#/react/nodejs/express
* https://github.com/okta/samples-nodejs-express-4

# Resource Validation (Python) Resources

* https://developer.okta.com/authentication-guide/tokens/validating-access-tokens