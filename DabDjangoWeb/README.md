USING VENV:
to start the venv, cd to the directory where DanDjangoWeb is located and run: "pipenv shell"
to install any new packages, run: "pipenv install"

USING DOCKER:
image name: dab-django-project-docker-container

Build docker image: "docker build -t dab-django-project ."
Run docker container from image: docker run -p 8000:8000 dab-django-project
