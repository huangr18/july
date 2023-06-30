### Style transfer web app 

#### Tools used
- FastAPI: for the API
- streamlit : for the interface
- Docker: to containerize the app

#### Run
```bash
cd machine_learning_web_template
make build
make up
```
or
```bash
cd machine_learning_web_template
./download_models.sh
docker-compose up -d
```
