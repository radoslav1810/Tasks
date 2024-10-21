
FROM python:3.12-slim


WORKDIR /fifth_task


COPY rabbit.py jbf.py  ./


RUN pip install pyats genie


CMD ["easypy", "rabbit.py"]
