# Rapid Motors

A car showroom management system using Vue.js and Flask.

# Frontend Documentation (Vue.js)

## Initial setup

- Clone this respository `git clone <SSH/HTTPS URL>`.
- Change directory to the frontend directory `cd rapid-motors/frontend`.
- Install the dependencies `npm install`.
- Run the application in development mode `npm run serve`.
- Deploy the frontend on [Vercel](https://vercel.com).

# Backend Documentation (Flask)

## Database setup

- Run the psql command using a terminal (Eg: Git bash).
- Login to your PSQL account `psql -U <user>`.
- Enter your password.
- Create the database `CREATE DATABASE <db_name>;`.
- Connect to that database `\c <db_name>;`.
- Create the necessary tables using flask-migrate.
  - Run the command `flask db upgrade`.

## Backend setup

- Install python virtual environment package if not installed already `pip install virtualenv`.
- Create a python virtual environment `virtualenv <environment_name>`.
- Run the virtual environment:
  - For windows based systems (environment_name): `source <environment_name>\Scripts\activate.bat`.
  - For Unix based systems (environment_name): `source <environment_name>/bin/activate`.
- Install dependencies `pip install -r requirements.txt`.

## Setting backend environment variables

- Create a copy of .env.example to .env `cp .env.example .env`.
- For `DATABASE_URL`:
  - In local development, set the variable to `postgresql://<username>:<password>@localhost:5432/<db_name>`.
  - In production development, set the variable to the published URL.
- For `GMAIL_USERNAME`:
  - In local and production development, set the variable to the email address of your gmail account.
- For `GMAIL_PASSWORD`:
  - In local and production development, set the variable to the password of your gmail account.

## Running backend in development mode

- Run the backend `flask run`.

## Running backend in production mode

- Run the backend `gunicorn app:app`. <br />**Note:** This command works only on Linux.
