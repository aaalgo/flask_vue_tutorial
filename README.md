Flask and Vue Tutorial
======================

# Background

This is a stub project for a web app with Flask background and
Vue.  We use Vuetify for web UI components.

- https://en.wikipedia.org/wiki/IP_address
- https://en.wikipedia.org/wiki/Port_(computer_networking)
- https://en.wikipedia.org/wiki/URL
- https://en.wikipedia.org/wiki/JSON
- https://www.tutorialspoint.com/http/index.htm
  Pay attention to:
  * What is content-type.
  * How different components of the URL play their parts in the
	protocol.
  * How parameters are passed in the GET method.
  * How parameters are passed in the POST method; how files are
	uploaded.

- Flask Quickstart (we do not need the template part): https://www.tutorialspoint.com/flask/index.htm
- Vue https://vuejs.org/guide/quick-start.html#using-vue-from-cdn
- Vuetify https://next.vuetifyjs.com/en/components/all/


# Architecture

The Vue project under `web` is compiled to a bunch of static files under
the `static` directory, which is served by the Flask web server.
The static files will be loaded by the browser, and further interaction
will be realized by communication between the browser and the Flask
web server in the form of restful web service request, i.e. HTTP message
exchanges in JSON.

In the deployment mode, this is implemented by the fact that:
- Flask serves static files under `static` by default.
- All other restful requests are implemented by the python code.

In the development mode, the frontend files is directly served by yarn,
and the browser also connects to yarn.  Therefore we need to set up yarn
so the restful API are forwarded to the flask server.  This is
implemented by the following lines in the configuration file
`vite.config.js`:

```
  server: {
    ...
    proxy: {
      '/api/': 'http://127.0.0.1:8888'
    }
  }
```

By default we configure the flask server to listen the port 8888.

# Dependencies

- Python3.  To install flask run `pip3 install flask`.
- Node.js.  To install yarn run `sudo npm install --global yarn`.

```
$ cd web
$ npm install
$ yarn build
```


# How to Run

## Method 1. For deployment or for back-end development only.

- Change to `web`; run `yarn build` to update the static files.
- Change back to project root and run `./server.py`.

Browse the URL printed out by the python server.

## Method 2. For front-end development.

The advantage of this is the code changes in the front-end part
is immediately reflected in the browser without the need to recompile.

- Run `./server.py`.
- Change to `web`; run `yarn dev`.

Browse the URL printed out by `yarn`.


