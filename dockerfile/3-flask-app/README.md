<link rel='stylesheet' href='../../assets/css/main.css'/>

# Lab: Bundling a Flask Web Application

In this app, we will create a Python app using flask, and deploy it using docker.

Here is the [Dockerfile](Dockerfile) we are going to use

```Dockerfile
FROM python:3.10.6-buster

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt
COPY app.py /usr/src/app/
EXPOSE 5000
CMD ["python3", "/usr/src/app/app.py"]
```

Note what we're going to do.  We are going to start with ubuntu.

Be in the project dir
```bash
cd  ~/docker-labs/dockerfile/3-flask-app
```

```bash
docker build .  -t flask-app
```

You will get a very long output, which will be Docker loading all of your
Dockerfile commands onto your container.

You should look at your Dockerfile

```console
[+] Building 0.9s (9/9) FINISHED
 => [internal] load build definition from Dockerfile                                                                                                                                   0.0s
 => => transferring dockerfile: 32B                                                                                                                                                    0.0s
 => [internal] load .dockerignore                                                                                                                                                      0.0s
 => => transferring context: 2B                                                                                                                                                        0.0s
 => [internal] load metadata for docker.io/library/python:3.10.6-buster                                                                                                                0.8s
 => [1/4] FROM docker.io/library/python:3.10.6-buster@sha256:6ec5fc87e4628ac35d5cbb65afd8b97a94db40fec824cd66e5c326df43203127                                                          0.0s
 => => resolve docker.io/library/python:3.10.6-buster@sha256:6ec5fc87e4628ac35d5cbb65afd8b97a94db40fec824cd66e5c326df43203127                                                          0.0s
 => [internal] load build context                                                                                                                                                      0.0s
 => => transferring context: 63B                                                                                                                                                       0.0s
 => CACHED [2/4] COPY requirements.txt /usr/src/app/                                                                                                                                   0.0s
 => CACHED [3/4] RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt                                                                                                       0.0s
 => CACHED [4/4] COPY app.py /usr/src/app/                                                                                                                                             0.0s
 => exporting to image                                                                                                                                                                 0.0s
 => => exporting layers                                                                                                                                                                0.0s
 => => writing image sha256:6eb2c0b8a9e672dcfba1e93bbc959c6da225a258d2f61c54cfe5918e2ecb1cb3                                                                                           0.0s
 => => naming to docker.io/library/flask-app                                                                                                                                           0.0s                                                                                       0.0s
```

**_NOTE:_**
-  Your output might be a little different
- I've snipped this for clarity, but pay attention to what's going on


## List your images

```bash
docker images
```

```console
REPOSITORY   TAG       IMAGE ID       CREATED         SIZE
flask-app    latest    6eb2c0b8a9e6   6 minutes ago   904MB
```

Notice `flask-app` is fairly large (904MB). This is because we have a full-on ubuntu-python system here.  We may not  need that.

## Run the container

```bash
docker container run -p 5000:5000  --name flask-app flask-app
```

This will run our app.  console output should look like the following

```console
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://172.17.0.2:5000
```

## Access our Flask app

Open your browser and go to localhost:5000

You should see something like the following in your browser:

```console
Hello! I am Flask running on a docker instance.
```

You can also test this on command line

```bash
curl localhost:5000/
```

This indicates your Flask app is running properly. You can now close your container by typing control-c.

**_NOTE:_**

- If you're using PowerShell 7 with the latest version of Windows 11, control-C might not work, You need to close your terminal completely and stop the container manually using `docker container stop flask-app`

---
Verified by Farshid on 2022-09-06 08:24:00 UTC