import logging

from openai import OpenAI

from ...config import settings
from ...util import log


class OpenAIService:
    def __init__(self) -> None:
        self.logger = logging.getLogger(__name__)
        self.client = OpenAI(api_key=settings.openai_api_key)

    @log
    def populate_latex_template(self, latex_template: str, content: str) -> str:
        response = self.client.chat.completions.create(
            model=settings.openai_model,
            messages=[
                {
                    "role": "system",
                    "content": """
                        You have two texts: a LaTeX template and a content text.
                        Using the conent text and the LaTeX template, populate the LaTeX
                        template with the content text.
                        """,
                },
                {"role": "user", "content": f"LATEX TEMPLATE: \n{latex_template}\n\nCONTENT: \n{content}"},
            ],
        )

        return response.choices[0].message.content.strip()


# openai_service = OpenAIService()
# openai_service.populate_latex_template("Hello World!", "Hello World!")
