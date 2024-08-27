FROM python:3.12-alpine

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# COPY ./app /code/app

# Expose port 80 for HTTP traffic
EXPOSE 80

# Remove --reload
CMD ["fastapi", "run", "app/main.py", "--port", "80", "--reload"]