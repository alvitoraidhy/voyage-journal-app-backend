<!-- markdownlint-disable MD032 MD033-->

# **alvitoraidhy/chingu-journal-app-backend**

---

## **About the project**

* This project is created as a warm-up before applying to Chingu Tier-3 Voyage 36. The web application consists of two repositories. This repository contains the back-end of the web application.
* The web applications features a simple account-based note management system. The back-end handles the storage of the accounts and the notes, and the application logic of the application.
* The back-end side of the application heavily depends on the following packages:
    + FastAPI, as the web application framework
    + Tortoise ORM, as the database ORM

---

## **Installation**

- Install all of the required Python
 packages:

```sh
pip install -r requirements.txt
```

- Set up a PostgreSQL database and export an environment variable, containing the credentials of the database in the form of a URL:

```sh
export DATABASE_URL=postgres://postgres:postgres@localhost:5432/journal-app
```

- Run the database migration script:

```sh
aerich upgrade
```

---

## **Usage**

- Run the following command. You may change the host and port as needed:

```sh
uvicorn --host 0.0.0.0 --port 8000 main:app
```

---

## **License**

See the license in the '**[LICENSE](LICENSE)**' file.
