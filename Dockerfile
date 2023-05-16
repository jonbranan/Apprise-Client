FROM python:alpine3.18
WORKDIR /
COPY apprise-client.py opt
ENV toml_path=''
RUN pip install requests
CMD [ "python", "opt/apprise-client.py" ]