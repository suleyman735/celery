pip freeze> requirements.txt
chmod +x ./entrypoint.sh
http://0.0.0.0:8000/
docker-compose up -d --build
./manage.py startapp cworker
docker exec -it django /bin/sh
rm -r cworker
