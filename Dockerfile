FROM python:3.12-slim

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN apt-get update && apt-get install -y mariadb-client libmariadb-dev gcc

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

RUN apt-get remove -y libmariadb-dev gcc  && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# COPY ./app /code/app

# Expose port 80 for HTTP traffic
EXPOSE 80

# Remove --reload
CMD ["fastapi", "run", "app/main.py", "--port", "80", "--reload"]