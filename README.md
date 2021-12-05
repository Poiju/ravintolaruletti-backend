<h1 align="center">Backend<p align="center"> <a href="https://github.com/Poiju/ravintolaruletti-backend" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/django/django-original.svg" alt="django" width="40" height="40"/> </a> <a href="https://github.com/Poiju" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/github/github-icon.svg" alt="github" width="40" height="40"/> </a> <a href="https://ruletti.herokuapp.com" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/heroku/heroku-icon.svg" alt="heroku" width="40" height="40"/> </a> <a href="https://postman.com" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/getpostman/getpostman-icon.svg" alt="postman" width="40" height="40"/> </a> </h1>


Team: [Risto Lähteenkorva](https://www.linkedin.com/in/r-lahteenkorva) , Maisa Mäntyvaara, [Krista Nyberg](https://www.linkedin.com/in/krista-nyberg-5a7721176/), Tomi Salo, [Tuomas Valkamo](https://www.linkedin.com/in/tuomasvalkamo/)

#
<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#backend">Backend</a></li>
    <li><a href="#endpoints">Endpoints</a></li>
    <li><a href="#usage-of-postman">Usage of postman</a></li>
    <li><a href="#technologies-and-libraries">Technologies and libraries</a></li>
    <li><a href="#installation-instructions-for-running-server-locally">Installation instructions for running server locally</a></li>
  </ol>
</details>

## Backend

Documentation of unfinished backend

hosted at [here](https://ruletti.herokuapp.com)

## Endpoints

| Function | Description | Attributes |
| --- | --- | --- |
| / | api-root | GET, no attributes |
| /users/ | users list | GET, no attributes |
| /users/ | create new user | POST, Authorization: Token xxxx, username='username' email='email' is_staff=True/False |
| /users/n/ | individual users data | GET, n = user number |
| /api-auth/login | login screen | POST -H Authorization: Token xxxx |
| /api-auth/logout | logout screen | no attributes |
| /api-token-auth | get token for user | POST user:password |


## Usage of postman

<p align="center">
<a ><img src="" alt="kuva1" border="0" width="30%" />&nbsp;</a>
<a ><img src="" alt="kuva1" border="0" width="30%" />&nbsp;</a>
<a ><img src="" alt="kuva1" border="0" width="30%" /></a>
</p>

## Technologies and libraries

* [Python](https://www.python.org/downloads/)
* [Django](https://www.djangoproject.com/)
* Deployment helper library [Django on heroku](https://pypi.org/project/django-on-heroku/)
* Django rest framework [Django rest framework](https://www.django-rest-framework.org/)
* Hosting at[Heroku](https://www.heroku.com/)

 
## Installation instructions for running server locally

1. [install python](https://www.python.org/downloads/)  
2. Run the following lines in your CLI, or the built-in terminal of your code editor:  

```

git clone https://github.com/Poiju/ravintolaruletti-backend.git  

cd ravintolaruletti-backend  

python -m pip install virtualenv  

venv\Scripts\activate  

python -m pip install -r requirements.txt  

python manage.py runserver  

```

Server starts at http://127.0.0.1:8000/

