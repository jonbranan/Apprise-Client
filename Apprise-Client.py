import requests as r
from tomllib import load

config_file_path = './config.toml'
with open(config_file_path, 'rb') as c:
        config = load(c)

def apprise_notify(req_obj, host, port, aurls, title, body):
    payload = {'urls': aurls,'title': title,'body': body,}
    url = f'http://{host}:{port}/notify/'
    apprise_response = req_obj.post(url, json = payload ,verify=False)
    return apprise_response

a = apprise_notify(r,config["apprise"]["host"],config["apprise"]["port"],config["apprise"]["aurls"],\
                   config["apprise"]["title"],config["apprise"]["body"])