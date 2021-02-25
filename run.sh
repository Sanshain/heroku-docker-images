docker rm -f $(docker ps -a -q)
docker run -ti --name django-heroku -e "PORT=8000" -e "DEBUG=1" -p 8007:8000 web:latest

# sudo docker run -ti -e "PORT=8000" -e "DEBUG=1" -p 8007:8000 web-a-f:latest bash