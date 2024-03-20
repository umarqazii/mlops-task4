# Model Deployement Using Docker

## Run Without Make

- Run the following command to build the docker image

```bash
docker build -t flask-image .
```

- Run the following command to run the docker container

```bash
docker run -d -p 5000:5000 flask-image
```

OR

## Run Using Make

- Build docker container

```bash
make build
```

- Run docker container

```bash
make run
```
