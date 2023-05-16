FROM python:alpine3.18
WORKDIR /
ADD https://git.jbranan.com/jblu/apprise-client/raw/branch/main/apprise-client.py opt
ENV toml_path=''
RUN pip install requests
CMD [ "python", "opt/apprise-client.py" ]