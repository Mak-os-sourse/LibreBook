# LibreBook

<p align="center">
    <em>A simple educational fullstack project.</em>
</p>

<p align="center">
    <img src="https://img.shields.io/github/languages/top/Mak-os-sourse/Librebook">
    <img src="https://img.shields.io/github/license/Mak-os-sourse/Librebook">
    <img src="https://img.shields.io/github/stars/Mak-os-sourse/Librebook">
</p>

## Stack

**Backend**
* Django
* Django REST Framework
* drf-yasg / drf-spectacular (Swagger)
* PyJWT

**Frontend**
* Vite
* JavaScript
* Axios
* Bootstrap
* ESLint
* Prettier

**Infrastructure**
* Docker
* Nginx
* PostgreSQL

## Installation and launch

First, clone the repository:
* `git clone https://github.com/your-username/Librebook.git`

Copy the environment file and adjust the values if needed:
* `cp settings.env.example settings.env`

Now you can build and run the containers:
* `docker-compose up -d --build`

The application will be available on the port configured for Nginx in `docker-compose.yml`.

## Structure
```
├───backend
│   ├───book
│   ├───comment
│   ├───favorites
│   ├───librebook
│   ├───user
│   ├───manage.py
│   └───settings.py
├───frontend
│   ├───api
│   ├───components
│   ├───public
│   ├───template
│   ├───index.html
│   ├───login.html
│   ├───regist.html
│   ├───profile.html
│   ├───addBook.html
│   ├───bookView.html
│   ├───main.js
│   ├───styles.scss
│   └───styles.js
├───nginx
│   └───default.conf
├───add_fake_books.py
├───docker-compose.yml
├───Dockerfile
├───pyproject.toml
├───package.json
├───vite.config.js
├───eslint.config.js
├───jsconfig.json
├───Makefile
├───settings.env
└───LICENSE
```