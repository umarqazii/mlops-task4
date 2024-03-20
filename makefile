install:
    pip install -r requirements.txt

train:
    python main.py

build:
    docker build -t flask-image .

run:
    docker run -p 5000:5000 flask-image