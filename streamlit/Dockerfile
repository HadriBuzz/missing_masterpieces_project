FROM python:3.11

EXPOSE 8701

COPY ./requirements.txt /code/requirements.txt

RUN pip install --upgrade -r /code/requirements.txt

COPY ./ /code/

WORKDIR /code/source/

ENTRYPOINT ["/bin/bash"]

CMD ["/code/source/start_streamlit.sh"]