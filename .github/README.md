<h1 align="center">
  <br>
  <a href="https://github.com/DiziASP/seleksi-3-labpro-monolith">
    <img src="https://github.com/DiziASP/seleksi-3-labpro-monolith/blob/master/.github/image/monolith-logo.png?raw=true" alt="Monolith FS">
  </a>
</h1>

<h4 align="center">A monolithic full stack website made with Django.</h4>

<p align="center">
    <a href="https://github.com/DiziASP/seleksi-3-labpro-monolith/commits/master">
      <img src="https://img.shields.io/github/last-commit/DiziASP/seleksi-3-labpro-monolith.svg?style=flat-square&logo=github&logoColor=white"
           alt="GitHub last commit">
</p>

<p align="center">
  <a href="#about">About</a> •
  <a href="#installation">Installation</a> •
  <a href="#docker">Docker</a> •
  <a href="#tech-stack">Tech Stack</a> •
  <a href="#my-design-patterns">My Design Patterns</a> •
  <a href="#bonus">Bonus</a> •
  <a href="#license">License</a>
</p>

---

## About

<table>
<tr>
<td>
  
**BelanjaBelinji** is a **monolithic fullstack web application** built on _Django and TailwindCSS_ that aims to provide a **seamless** shopping experience for customers. It is a **monolithic** application, meaning that the frontend and backend are **coupled** together. This project is made for the **Seleksi 3 LabPro** assignment.

![Landing Page](https://github.com/DiziASP/seleksi-3-labpro-monolith/blob/master/.github/image/Landing.png?raw=true)
<p align="right">
<sub>(Preview)</sub>
</p>

</td>
</tr>
</table>

## Installation

### Prerequisites

* **[Install](https://docs.python.org/3.11/)** the latest version of Python.
* **[Install](https://docs.python.org/3/library/venv.html)** the venv library.

### Installation Steps

1. **[Clone this](https://github.com/DiziASP/seleksi-3-labpro-monolith.git)** repository to your local machine.

2. Initialize a virtual environment in the project directory.

    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment.

    ```bash
    # Windows
    venv\Scripts\activate.bat
    
    # Linux
    source venv/bin/activate
    ```

4. Install the dependencies.

    ```bash
    pip install -r requirements.txt
    ```

5. Run the server.

    ```bash
    python manage.py runserver
    ```

6. Open the website url `http://127.0.0.1:8000/` on your browser.

## Docker

You can also run the application using Docker. Make sure you have Docker installed on your machine.

1. **[Clone this](https://github.com/DiziASP/seleksi-3-labpro-monolith.git)** repository to your local machine.

2. Since the application uses PostgreSQL and a single service api, you need to create a `.env` file in the root directory of the project. The `.env` file should contain the following environment variables:

    ```bash
    SECRET_KEY=<your_secret_key>
    DEBUG=<True_or_False>
    SS_API_URL=<your_single_service_api_url>
    PGDATABASE=<your_database_name>
    PGHOST=<your_database_host>
    PGPASSWORD=<your_database_password>
    PGPORT=<your_database_port>
    PGUSER=<your_database_username>
    ```

3. Build and Run the Docker Container using Docker Compose

      ```bash
      docker-compose up
      ```

4. Your docker is up and running. Open the website url `http://127.0.0.1:8000/` on your browser.

   ![Landing Page](https://github.com/DiziASP/seleksi-3-labpro-monolith/blob/master/.github/image/docker-container.png?raw=true)

## Tech Stack

 ![Python](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python)
 ![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
 ![TailwindCSS](https://img.shields.io/badge/tailwindcss-%2338B2AC.svg?style=for-the-badge&logo=tailwind-css&logoColor=white)
 ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

## My Design Patterns

* **[Model-Template-View (MTV)](https://towardsdatascience.com/working-structure-of-django-mtv-architecture-a741c8c64082?gi=50fedc3ee24b)**

    The MTV design pattern is a software design pattern that is a variation of the MVC design pattern used in software development. In MTV, the controller is replaced by a template engine. This pattern is commonly used on Django projects. The reason I chose this design pattern is because it is the default design pattern used in Django projects and template engines are very useful for rendering static HTML pages.

* **[Singleton](https://refactoring.guru/design-patterns/singleton)**

    The Singleton design pattern is a software design pattern that restricts the instantiation of a class to one object. This is useful when exactly one object is needed to coordinate actions across the system. I implemented this design pattern on the `permissions.py` file because i only need one instance of the **Custom Auhentication** class to check the user's permissions.

* **[Strategy](https://refactoring.guru/design-patterns/strategy)**

    The Strategy design pattern is a software design pattern that enables an algorithm's behavior to be selected at runtime. This is useful when there are multiple algorithms that can be used interchangeably. I implemented this design pattern with the `ListAPIView` and other Class Based Views because they have multiple methods that can be used interchangeably.

## Bonus

* **B01 - OWASP**

    This bonus implementation is explained further on the [Single Service Repository](https://github.com/DiziASP/seleksi-3-labpro-ss-be)

* **B02 - Deployment**

    The application is deployed on railway. You can access the website [here](https://seleksi-3-labpro-monolith-production.up.railway.app/).

* **B03 - Single Service Implementation**

    Implemented on Single Service Repository [here](https://github.com/DiziASP/seleksi-3-labpro-ss-be).

* **B04 - Polling**

    Not Implemented.

* **B05 - Lighthouse**

    Using Google Chrome Lighthouse, I got the following results for the website's Front End:

    ![Lighthouse1](https://github.com/DiziASP/seleksi-3-labpro-monolith/blob/master/.github/image/lighthouse-1.png?raw=true)
    ![Lighthouse2](https://github.com/DiziASP/seleksi-3-labpro-monolith/blob/master/.github/image/lighthouse-2.png?raw=true)
    ![Lighthouse3](https://github.com/DiziASP/seleksi-3-labpro-monolith/blob/master/.github/image/lighthouse-3.png?raw=true)
    ![Lighthouse4](https://github.com/DiziASP/seleksi-3-labpro-monolith/blob/master/.github/image/lighthouse-4.png?raw=true)
  
    Based on this score, I've managed to gain a average score of more than 95. The reason of the low score for the performance is because the CPU used in railway free tier is noticeably slow and also python is considerably slower than most of programming language

* **B06 - Responsive Layout**

    The website is responsive-ish since i'm using overflow on the table hence in the mobile view the table is scrollable to the left and right.

    ![Mobile](https://github.com/DiziASP/seleksi-3-labpro-monolith/blob/master/.github/image/mobile.png?raw=true)

* **B07 - API Documentation**

    The API Documentation is available on the website's [API Documentation Page](https://seleksi-3-labpro-monolith-production.up.railway.app/api/schema/swagger-ui/).

    Implemented with [Swagger](https://swagger.io/).

* **B08 - SOLID Principle**

    This monolith application is built with the SOLID principle in mind. The SOLID principle is a set of five principles that makes software design more understandable, flexible, and maintainable. The SOLID principle in this project are the following:

  * **S**ingle Responsibility Principle

    Some class in this project has a single responsibility. For example, the `User` class is only responsible for handling user data such as the Model, Serializers, etc.

  * **O**pen-Closed Principle

    Some class in this project is open for extension but closed for modification. For example, the `LoginSerializer` class was extended from the `serializers.ModelSerializer` class but it's not modifying the parent.

  * **L**iskov Substitution Principle

    Some class in this project can be substituted with its subtypes. For example, the `ModelSerializer` class can be substituted with its subtypes such as `LoginSerializer` and `RegisterSerializer`.
  
  * **I**nterface Segregation Principle

    Some class in this project has multiple interfaces that are specific to the client. For example, the `ListAPIView` class has multiple interfaces such as `get`, `post`, `put`, `delete`, etc. which must be implemented when the class is instantiated.
  
  * **D**ependency Inversion Principle

    Some class in this project depends on abstractions rather than concrete implementations. For example, the `ListAPIView` class depends on the `get` interface which is an abstraction rather than a concrete implementation (we don't know what the `get` interface does, we just know that it exists and we can use it to do **GET METHOD**).

* **B09 - Wireshark**

    This bonus implementation is available on the [Single Service Repository](https://github.com/DiziASP/seleksi-3-labpro-ss-be)

* **B10 - Automated Testing**

    This bonus implementation is only implemented and available on the [Single Service Repository](https://github.com/DiziASP/seleksi-3-labpro-ss-be)

* **B11 - Additional Feature**

    In the monolith application, I added a **Search Bar** feature on the **Product List Page**. This feature is useful for customers to search for products that they want to buy.

    ![Search](https://github.com/DiziASP/seleksi-3-labpro-monolith/blob/master/.github/image/search-bar.png?raw=true)

* **B12 - FE Admin Bug**

    Not Implemented.

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
