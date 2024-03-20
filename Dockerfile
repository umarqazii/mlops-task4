FROM python:3.11-slim
WORKDIR /app
# copy current directory (where code was present) to current working directory(/app) of docker container
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"]