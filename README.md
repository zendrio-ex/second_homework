## Here is really bad model, because it's just about fastapi and docker.

To run docker container you should execute "docker build .". 
Then docker run -it --rm -p 8000:8000 --name prediction_service [id]

or use docker compose with 'docker compose build', then 'docker compose up'.