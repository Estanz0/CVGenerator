from pydantic import BaseModel


class TextInput(BaseModel):
    content: str
