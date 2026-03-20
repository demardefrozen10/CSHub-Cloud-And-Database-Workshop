from pydantic import BaseModel, Field

class SubmitFormRequest(BaseModel):
    name: str = Field(min_length=1)
    email: str = Field(min_length=1)
    Message: str = Field(min_length=1)