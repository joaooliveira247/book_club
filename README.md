# 📘 Book club

![GitHub Pipenv locked Python version](https://img.shields.io/badge/Python-3.10.6-blue)

## ℹ️ About:

_This project has does how portfolio._

The purpose of this project is extract data from a site and save it in a SQL database.

To do it, I chose to use Postgre database, I also create a function to save it in CSV format.

I opted to use Postgres inside a container, but you can configure `.env` to run of the way do you want.

If you only want data as CSV, you don't need configure `.env` or `docker-compose.yml` file.

### [Link to Challenge](https://medium.com/@meigarom/o-projeto-de-data-engineering-para-o-seu-portf%C3%B3lio-c186c7191823)

## 💻 Requirements:

### `Python >= 3.10`

### [`Docker`](https://www.docker.com/) & [`Docker compose`](https://docs.docker.com/compose/)

```bash
docker compose -d
```

- It will up your container.

### `Poetry`

This project uses a packaging and dependency management called [`poetry`](https://python-poetry.org/).

- Installation:

  `(osx / linux / bash on windows) install instructions`

  ```bash
  curl -sSL https://install.python-poetry.org | python3 -
  ```

  `windows(Powershell) install instructions`

  ```bash
  (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
  ```

- Running

  ```bash
  poetry install
  ```

  - To install all dependencies of the project.

  ####

  ```bash
  poetry shell
  ```

  - To give a shell with environment activate.

## 📜 Documentation:

**⚠️ Windows**

If you are running this project on Windows replace the `python3` by `poetry run`.

- `CLI`

  - `create`

    ```bash
    python3 manage.py create
    ```

    - It will create book_table, with name that you set in `.env`

  - `load`

    ```bash
    python3 manage.py load
    ```

    - It will load all data in database.

    `load` has arguments, if do you want only save in `csv`:

    ```bash
    python3 manage.py load --csv
    ```

    - It will save the data in `book_club.csv` in the project directory.

    ###

    ```bash
    python3 manage.py --csv --path <path>
    ```

    - The flag `--path` will save the csv archive in a directory.

    `ex:`

    ```bash
    python3 manage.py load --csv --path ~/Documents/CSV
    ```

  The `CLI` has commands to query, but I strongly recommend using a `SDK` to make queries and manipulate data.

  > **_OBS:_**
  >
  > This commands only works if you set database requirements to work (`.env`, `docker-compose.yml`).

  - `select`

  ###

  ```bash
  python3 manage.py select <id_1> <id_2> <...>
  ```

  - It will return one/many rows in terminal.

  ###

  - `select-title`

  ###

  ```bash
  python3 manage.py select-title <title>
  ```

  - It will return one/nothing rows in terminal.

  ###

  - `insert`

  ###

  ```bash
  python3 manage.py insert "<title>" <category> <stars> <price> <is_available>
  ```

  - It will insert a book in database.

    `ex:`

    ```bash
    python3 manage.py insert "python fluence" tecnology 5 100 true
    ```

  ###

  - `delete`

  ###

  ```bash
  python3 manage.py delete <id>
  ```

  - It will delete a book from database.

  - `rows`

  ```bash
  python3 manage.py rows
  ```

  - It will return the number of rows in a table.

- `functions`

  

## 🐍 Usage libraries:

- [requests - 2.31.0](https://requests.readthedocs.io/en/latest/)

- [beautifulsoup4 - 4.12.2](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

- [sqlalchemy - 2.0.15](https://www.sqlalchemy.org/)

- [psycopg2 - 2.9.6](https://www.psycopg.org/docs/)

- [rich - 13.3.5](https://rich.readthedocs.io/en/stable/introduction.html)

- [typer - 0.9.0](https://typer.tiangolo.com/)

- [python-dotenv - 1.0.0](https://pypi.org/project/python-dotenv/)
