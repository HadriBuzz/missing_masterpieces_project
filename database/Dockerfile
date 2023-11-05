FROM python:3.11

EXPOSE 8702

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./source /code/source

WORKDIR /code/source

CMD ["python3", "-m", "uvicorn", "fast_api:app", "--host", "0.0.0.0", "--port", "8702"]
