from fastapi import FastAPI
from fastapi import HTTPException
import json
import oracledb

from DBConnection.connect import get_connection
from WriteModel.SubmitFormRequest import SubmitFormRequest

app = FastAPI()


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.get("/get-responses")
def get_responses():
    select_sql = "SELECT name, year_of_study, interests, what_you_like_about_cshub FROM STUDENTS"

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
            YEAR_OF_STUDY,
            MAJOR,
            INTERESTS,
            WHAT_YOU_LIKE_ABOUT_CSHUB
        )
        VALUES (
            :name,
            :year_of_study,
            :major,
            :interests,
            :what_you_like_about_cshub
        )
    """

    try:
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    insert_sql,
                    {
                        "name": payload.name,
                        "year_of_study": payload.year_of_study,
                        "major": payload.major,
                        "interests": payload.interests,
                        "what_you_like_about_cshub": payload.what_you_like_about_cshub,
                    },
                )
            conn.commit()
    except oracledb.Error as exc:
        raise HTTPException(status_code=500, detail=f"Failed to save form data: {exc}")
    return {"message": "Form submitted successfully"}