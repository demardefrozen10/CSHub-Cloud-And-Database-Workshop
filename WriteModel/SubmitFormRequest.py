from pydantic import BaseModel, Field

class SubmitFormRequest(BaseModel):
    name: str = Field(min_length=1)
    year_of_study: str = Field(min_length=1)
    major: str = Field(min_length=1)
    interests: str = Field(min_length=1)
    what_you_like_about_cshub: str = Field(min_length=1)