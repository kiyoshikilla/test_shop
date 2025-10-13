<div align="center">
  <h1>Twilight Store<br><a href="https://twilight-store.onrender.com/">https://twilight-store.onrender.com/</a></h1>
  <p>
    A modern e-commerce web application built with Django and containerized with Docker.
  </p>

  <p>
    <img src="https://img.shields.io/badge/Python-3.11-blue.svg" alt="Python 3.11">
    <img src="https://img.shields.io/badge/Django-4.2-darkgreen.svg" alt="Django 4.2">
    <img src="https://img.shields.io/badge/Docker-20.10-blue.svg" alt="Docker">
    <img src="https://img.shields.io/badge/license-MIT-green.svg" alt="MIT License">
  </p>
</div>

A fully-featured e-commerce platform that provides a seamless shopping experience. It includes a complete backend powered by Django, with a containerized setup using Docker for easy development and deployment.

---

## 📒 Index

-   [About](#-about)
-   [Usage](#-usage)
-   [Installation](#-installation)
-   [Commands](#-commands)
-   [Development](#-development)
    -   [Pre-Requisites](#-pre-requisites)
    -   [Development Environment](#-development-environment)
    -   [File Structure](#-file-structure)
-   [Build](#-build)
-   [Deployment](#-deployment)
-   [Branches](#-branches)
-   [FAQ](#-faq)
-   [Resources](#-resources)

## 🔰 About

**Twilight Store** is an online shopping application designed to provide a robust and scalable solution for e-commerce businesses. The backend is built on the powerful Django framework, leveraging its features for rapid development, security, and scalability.

The project is architected with a modern technology stack, including:
* **PostgreSQL** for a reliable relational database.
* **Redis** for efficient caching and performance enhancement.
* **Cloudinary** for cloud-based media file management.
* **Docker and Docker Compose** to create a consistent and isolated environment, simplifying both development and deployment.
* **Nginx** as a high-performance web server and reverse proxy.

This setup ensures that the application is not only feature-rich but also maintainable and easy to deploy.

## ⚡ Usage

Once the application is running, you can use it as follows:
* **Browse Products:** Navigate to the homepage or the "Shop" page to view all available products.
* **Filter Products:** Use the sidebar on the shop page to filter products by category or size.
* **View Product Details:** Click on any product to see its detailed description, price, and available options.
* **Add to Cart:** From the product detail page, you can add items to your shopping cart.
* **Manage Cart:** Go to the shopping cart page to review your selected items, update quantities, or remove items.
* **User Accounts:** Register for a new account or log in to an existing one to manage your personal information and view your order history.

## 🔌 Installation

To get this project running on your local machine, follow these detailed steps. This setup uses Docker, so you won't need to install Python, Django, or PostgreSQL on your host machine directly.

1.  **Clone the Repository**
    Open your terminal and clone the project:
    ```bash
    git clone [https://github.com/kiyoshikilla/twilight-store.git](https://github.com/kiyoshikilla/twilight-store.git)
    cd twilight-store
    ```

2.  **Configure Environment Variables**
    Create a `.env` file in the root directory of the project. This file will hold all your secret keys and configuration settings. You can start by copying the example if one is provided, or create it from scratch.
    ```bash
    # Create the file
    touch .env
    ```
    Now, open the `.env` file and add the following configuration. Replace the placeholder values with your actual credentials.
    ```env
    # Django Settings
    SECRET_KEY='your-super-secret-key-here'
    DEBUG=True
    ALLOWED_HOSTS=127.0.0.1 localhost

    # PostgreSQL Database
    DB_ENGINE=django.db.backends.postgresql
    DB_NAME=postgres
    DB_USER=postgres
    DB_PASSWORD=postgres
    DB_HOST=db  # This 'db' refers to the service name in docker-compose.yml
    DB_PORT=5432
    DB_PARSE=postgres://postgres:postgres@db:5432/postgres

    # Redis Cache
    REDIS_BACK=django_redis.cache.RedisCache
    REDIS_LOC=redis://redis:6379/1 # 'redis' is the service name
    REDIS_CLASS=django_redis.client.DefaultClient

    # Cloudinary for Media Storage
    CLOUDINARY_URL=cloudinary://<api_key>:<api_secret>@<cloud_name>
    CLOUD_NAME=<your_cloud_name>
    API_CLOUD=<your_api_key>
    API_SECRET=<your_api_secret>
    ```

3.  **Build and Run with Docker Compose**
    This single command will build the images for the web, database, and other services, and then start the containers.
    ```bash
    docker-compose up --build
    ```
    The `--build` flag ensures that the Docker images are rebuilt from scratch. You can omit it on subsequent runs.

## 📦 Commands

All commands should be run from the root directory of the project.

* **Start the application:**
    ```bash
    docker-compose up
    ```

* **Apply database migrations:**
    (Run in a separate terminal while the application is running)
    ```bash
    docker-compose exec web python manage.py migrate
    ```

* **Create a superuser for the admin panel:**
    ```bash
    docker-compose exec web python manage.py createsuperuser
    ```

* **Collect static files (for production):**
    ```bash
    docker-compose exec web python manage.py collectstatic --noinput
    ```

* **Stop the application:**
    ```bash
    docker-compose down
    ```

## 🔧 Development

This section provides guidance for developers who wish to contribute to the project.

### 📓 Pre-Requisites

Make sure you have the following tools installed on your system:
* [**Git**](https://git-scm.com/downloads): For version control.
* [**Docker**](https://www.docker.com/get-started): For containerization.
* [**Docker Compose**](https://docs.docker.com/compose/install/): To manage multi-container Docker applications.

### 🔩 Development Environment

Setting up the development environment is straightforward thanks to Docker. The process is identical to the [Installation](#-installation) steps. By following them, you will have a complete, isolated development environment running in containers.

Any changes you make to the source code on your host machine will be automatically reflected inside the `web` container due to the volume mapping defined in `docker-compose.yml`.


### 📁 File Structure

Here is a simplified overview of the project's structure:

```

.
├── docker-compose.yml      \# Defines all services (web, db, redis, nginx)
├── Dockerfile              \# Instructions to build the Django application image
├── nginx.conf              \# Nginx configuration for reverse proxy
├── manage.py               \# Django's command-line utility
├── requirements.txt        \# Python dependencies
├── products/               \# Django app for products, categories, and cart
│   ├── models.py           \# Database models
│   ├── views.py            \# Application logic (controllers)
│   ├── urls.py             \# URL routing for the products app
│   └── templates/          \# HTML templates for products
├── users/                  \# Django app for user authentication and profiles
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
├── static/                 \# Static files (CSS, JS, images)
└── twilight\_store/         \# Main Django project configuration
├── settings.py         \# Project settings
└── urls.py             \# Root URL configuration

````

## 🔨 Build

The project build is handled by Docker. The `Dockerfile` contains all the instructions to create a production-ready image for the Django application. To build all the services' images, you can run:

```bash
docker-compose build
````
This will build the images defined in docker-compose.yml using the instructions in the Dockerfile for the web service.

## 🚀 Deployment
To deploy this application, you can use any platform that supports Docker. Here are some general steps:

Set up a server: This can be a virtual private server (VPS) from any cloud provider like AWS, Google Cloud, or DigitalOcean.

Install Docker and Docker Compose: Follow the official documentation to install Docker and Docker Compose on your server.

Configure environment variables: Create a .env file on your server with your production settings. Make sure DEBUG is set to False and ALLOWED_HOSTS includes your domain name.

Run the application: Use docker-compose up -d to run the application in detached mode.

For a more robust setup, you might want to consider using a managed database service instead of running PostgreSQL in a container.


## 🌿 Branches
main: This is the primary branch and represents the most stable version of the project. All pull requests should be made against this branch.

develop: This branch is for ongoing development. It's a good idea to base your feature branches off of develop.

## 📝 Guideline
Fork the repository: Start by forking the project to your own GitHub account.

Create a new branch: For each new feature or bugfix, create a new branch from the develop branch.

Make your changes: Write your code and make sure to follow the existing coding style.

Submit a pull request: Once your changes are ready, submit a pull request to the main branch of the original repository.

## ❓ FAQ
Q: I'm getting a SECRET_KEY error when I try to run the application.

A: This is because you haven't set up your environment variables correctly. Make sure you've created a .env file in the root directory of the project and added a SECRET_KEY value.

Q: How do I access the admin panel?

A: First, you'll need to create a superuser by running docker-compose exec web python manage.py createsuperuser. Then, you can access the admin panel by navigating to /admin on your local server.

## 📚 Resources
Django Documentation

Docker Documentation

PostgreSQL Documentation

Redis Documentation
