from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from . import schemas
from .config import settings
from .controller import Controller

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_allow_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


con = Controller()


@app.post("/generate-cv/text")
def generate_cv_from_text(user_id: str, template_id: str, content_text: schemas.TextInput) -> str:
    return con.generate_cv(user_id=user_id, template_id=template_id, content_text=content_text)


@app.post("/generate-cv/pdf")
def generate_cv_from_pdf(user_id: str, template_id: str, pdf_file_name: str) -> str:
    return con.generate_cv(user_id=user_id, template_id=template_id, pdf_file_name=pdf_file_name)
