# build our heroku-ready local Docker image
docker build -t sohbot-django -f Dockerfile .


# push your directory container for the web process to heroku
heroku container:push web -a sohbot


# promote the web process with your container 
heroku container:release web -a sohbot


# run migrations
heroku run python3 manage.py migrate -a sohbot
