Flask and Vue Tutorial
======================

# Background

This is a stub project for a web app with Flask background and
Vue.  We use Vuetify for web UI components.

- https://en.wikipedia.org/wiki/IP_address
- https://en.wikipedia.org/wiki/Port_(computer_networking)
- https://en.wikipedia.org/wiki/URL
- https://www.w3schools.com/whatis/whatis_json.asp
- https://www.tutorialspoint.com/http/index.htm
  Pay attention to:
  * What is content-type.
  * How different components of the URL play their parts in the
	protocol.
  * How parameters are passed in the GET method.
  * How parameters are passed in the POST method; how files are
	uploaded.
- Flask Quickstart (we do not need the template part): https://www.tutorialspoint.com/flask/index.htm
- https://www.w3schools.com/whatis/whatis_html.asp
- https://www.w3schools.com/whatis/whatis_vue.asp
- https://www.w3schools.com/whatis/whatis_ajax.asp
  This is the AJAX concept; we use `axios` for implementation.

References

- Vue https://vuejs.org/guide/quick-start.html#using-vue-from-cdn
- Vuetify (for reference only.) https://next.vuetifyjs.com/en/components/all/
- https://www.w3schools.com/js/


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

## Python3

Python should be available in most systems.  In Ubuntu it can be
installed by

```
# This is most likely not needed as python3 should be already available.
sudo apt-get install python3 python3-pip
```

To install dependencies, run 

```
pip3 install -r requirements.txt
```

## Node.js

### Install Node

If node is not already available:

```
$ sudo bash
# cd /opt
# wget https://nodejs.org/dist/v16.18.1/node-v16.18.1-linux-x64.tar.xz
# tar xf node-v16.18.1-linux-x64.tar.xz
# ln -s node-v16.18.1-linux-x64 node
# cat > /etc/profile.d/node.sh		# add environment variable to system
export NODE_HOME=/opt/node
export PATH=$PATH:$NODE_HOME/bin
<Ctrl-D>
```
Start a new terminal so node is made available to the shell.

### Yarn

If yarn is not available.
```
sudo npm install --global yarn
```

### Setup Project Directory
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


