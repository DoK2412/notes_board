FROM python:3.11

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt --root-user-action=ignore

COPY ./ /code/

CMD ["uvicorn", "app:app", "--host", "212.113.117.104", "--port", "8085"]