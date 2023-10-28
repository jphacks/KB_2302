FROM python:3.8.3

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . /code

EXPOSE 80

CMD ["uvicorn", "run:app", "--host", "0.0.0.0", "--port", "80"]