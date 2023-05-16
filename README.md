# apprise-client

> This is meant to be a wrapper to use apprise in existing python projects. 

From the Apprise Developers

> [Apprise](https://github.com/caronc/apprise)  allows you to send a notification to almost all of the most popular notification services available to us today such as:  _Telegram_,  _Discord_,  _Slack_,  _Amazon SNS_,  _Gotify_, etc. This API provides a simple gateway to directly access it via an HTTP interface.
> -   This project was designed to be incredibly light weight.
> - Configuration can be persistently stored for retrieval.

You may simply import my wrapper *apprise_notify()* into your project
> apprise_notify()

    from apprise-client import apprise_notify


It requires a *requests object* along with the following:
 - [ ] host
 - [ ] port
 - [ ] apprise urls
 - [ ] apprise message title
 - [ ] apprise message body

## Python Code example

 
    import  requests  as  r
    from apprise-client import apprise_notify
    
    host = "192.168.1.50"
	port = 8088
	aurls = 'mailto://user:pass@gmail.com'
	title = 'test title'
	body = 'test body'
	
    apprise_notify(r, host, port, aurls, title, body)

## You may also use a toml file to specify the options:

    import  requests  as  r
    from  tomllib  import  load
    from apprise-client import apprise_notify
    
    config_file_path  =  './config.toml'
    
	with  open(config_file_path, 'rb') as  c:
				config  =  load(c)

    host = config["apprise"]["host"]
	port = config["apprise"]["port"]
	aurls = config["apprise"]["aurls"]
	title = config["apprise"]["title"]
	body = config["apprise"]["body"]
	
    apprise_notify(r, host, port, aurls, title, body)

## toml file example:

    [apprise]
    host = "192.168.x.x"
    port = 8088
    aurls = 'mailto://user:pass@gmail.com'
    title = 'test title'
    body = 'test body'

## Apprise Documentation
[Github](https://github.com/caronc/apprise)
[Apprise urls](https://github.com/caronc/apprise/wiki#notification-services)

I recommend using docker to take advantage of the apprise service:
[Docker Hub](https://hub.docker.com/r/caronc/apprise)