## Without Make

```bash
docker build -t flask-image .
```

```bash
docker run -d -p 5000:5000 flask-image
```
## Using Make

- Build docker container

```bash
make build
```

- Run docker container

```bash
make run
```
