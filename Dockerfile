FROM python:3.10-alpine AS Builder

ENV PYTHONNUMBUFFERED 1

RUN mkdir /code

WORKDIR /code
COPY . /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
# EXPOSE 8000
# RUN python manage.py migrate
CMD [ "gunicorn", "-c", "config/gunicorn/conf.py", "--bind", ":8855", "portafolio.wsgi:application" ]
# FROM python:3.10-alpine AS Builder
# # Install dependencies
# RUN pip install --upgrade pip
# # RUN pip install pipenv
# # COPY Pipfile* /
# # RUN pipenv lock --requirements > requirements.txt
# # RUN apk add --update --no-cache --virtual .tmp gcc libc-dev
# RUN mkdir code
# # Copy sources files
# WORKDIR /code
# COPY requirements.txt /code/
# RUN python -m pip install -r requirements.txt
# COPY . .
# # Default port
# # ARG ARG_DEFAULT_PORT=8000
# # EXPOSE $ARG_DEFAULT_PORT
# # ENV DEFAULT_PORT=${ARG_DEFAULT_PORT}
# # Install migrations
# RUN python manage.py migrate
# # Run server
# # EXPOSE 8000
# # ENTRYPOINT python manage.py runserver --noreload

# # docker build --build-arg ARG_DEFAULT_PORT=8000 -t prueba1 .
