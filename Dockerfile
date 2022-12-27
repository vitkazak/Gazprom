FROM python:3.9-slim-bullseye
RUN pip3 install requests
WORKDIR /opt/project
ADD ./task.py /opt/project/task.py
CMD [ "python", "/opt/project/task.py" ]