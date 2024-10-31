# Important Commands
  
### Setup
`source ./bin/setup.sh`

### Run Code
`python3 dataset.py`<br>
`python3 main.py`<br>
`python3 app.py`

### Run Uvicorn Webserver
`uvicorn app:app --reload`

### FastAPI UI
`http://127.0.0.1:8000/docs`

### MLFlow UI
`mlflow ui`

### Clear
`source ./bin/cleanup.sh`

### Docker Image
`docker build -t {image-name} .`<br>
`docker run -d -p 80:80 {image-name}`<br>
`docker stop {container-id}`

### Use Docker UI
`http://localhost:80/predict`