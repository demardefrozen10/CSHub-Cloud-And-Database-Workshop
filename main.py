from fastapi import FastAPI
from fastapi import HTTPException
from fastapi.middleware.cors import CORSMiddleware
import oracledb

from DBConnection.connect import get_connection
from WriteModel.SubmitFormRequest import SubmitFormRequest

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.get("/get-responses")
def get_responses():
    select_sql = "SELECT name, email, message FROM STUDENTS"

    try:
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(select_sql)
                column_names = [description[0].lower() for description in cursor.description]
                rows = cursor.fetchall()
                return [dict(zip(column_names, row)) for row in rows]
    except oracledb.Error:
        raise HTTPException(status_code=500, detail="Failed to save form data")


@app.post("/submit-form", status_code=201)
def submit_form(payload: SubmitFormRequest):
    insert_sql = """
        INSERT INTO STUDENTS (
            NAME,
            EMAIL,
            MESSAGE,

        )
        VALUES (
            :name,
            :email,
            :message
        )
    """

    try:
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    insert_sql,
                    {
                        "name": payload.name,
                        "email": payload.email,
                        "message": payload.Message,
                    },
                )
            conn.commit()
    except oracledb.Error as exc:
        raise HTTPException(status_code=500, detail=f"Failed to save form data: {exc}")
    return {"message": "Form submitted successfully"}