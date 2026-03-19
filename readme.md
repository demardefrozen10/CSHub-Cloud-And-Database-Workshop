# FastAPI Backend To Oracle Database

## How to Run

### Install Python

https://www.python.org/downloads/

### Install FastAPI via pip

```pip install "fastapi[standard]"```

### Install OracleDB Driver

```pip install oracledb```

### Start the server 

```fastapi dev```

If that does not work, then most likely FastAPI has not been added to your environment variables. Try this instead:

python -m uvicorn main:app --reload

Head to ```http://127.0.0.1:8000``` and test your endpoints!

## How this works in a nutshell

Using the OracleDB driver, we are establishing a connection to the database using the credentials provided. This is more low level, instead of using a ORM, we are writing raw SQL queries and executing it against the database with the help of the driver.
