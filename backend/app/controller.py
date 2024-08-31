import logging

from .services.FileService.file_service import FileService
from .services.LLMService.openai_service import OpenAIService
from .util import log

logger = logging.getLogger(__name__)


class Controller:
    def __init__(self) -> None:
        self.logger = logging.getLogger(__name__)
        self.file_service = FileService(local_file_directory="../data/files")
        self.openai_service = OpenAIService()

    @log
    def get_text_from_pdf(self, user_id: str, file_name: str) -> str:
        return self.file_service.get_text_from_pdf(user_id=user_id, file_name=file_name)

    @log
    def get_template_latex_from_file(self, template_id: str, user_id: str = "") -> str:
        return self.file_service.get_latex_from_file(
            sub_directory="templates",
            template_id=template_id,
            user_id=user_id,
        )

    @log
    def get_generated_latex_from_file(self, user_id: str, template_id: str) -> str:
        return self.file_service.get_latex_from_file(
            sub_directory="generated",
            template_id=template_id,
            user_id=user_id,
        )

    @log
    def write_latex_template_to_file(self, latex_text: str, template_id: str, user_id: str = "") -> str:
        file_name = self.file_service.write_latex_to_file(
            sub_directory="templates",
            latex_text=latex_text,
            template_id=template_id,
            user_id=user_id,
        )
        return f"Successfully created latex file: {file_name}"

    @log
    def write_latex_generated_to_file(self, latex_text: str, template_id: str, user_id: str) -> str:
        file_name = self.file_service.write_latex_to_file(
            sub_directory="generated",
            latex_text=latex_text,
            template_id=template_id,
            user_id=user_id,
        )
        return f"Successfully created latex file: {file_name}"

    @log
    def make_pdf_from_latex(self, user_id: str, template_id: str) -> str:
        return self.file_service.make_pdf_from_latex(
            sub_directory="generated",
            template_id=template_id,
            user_id=user_id,
        )

    @log
    def generate_cv(
        self, user_id: str, template_id: str, pdf_file_name: str | None = None, content_text: str = ""
    ) -> str:
        # Get text from PDF
        content = content_text
        if pdf_file_name is not None:
            content = self.get_text_from_pdf(user_id=user_id, file_name=pdf_file_name)

        # Retrieve the LaTeX template text
        latex_template = self.get_template_latex_from_file(template_id=template_id)

        # Populate the LaTeX template with the content text
        generated_latex = self.openai_service.populate_latex_template(
            latex_template=latex_template, content=content
        )

        # Write Generated LaTeX to file
        self.write_latex_generated_to_file(latex_text=generated_latex, template_id=template_id, user_id=user_id)

        # Make PDF from LaTeX
        return self.make_pdf_from_latex(user_id=user_id, template_id=template_id)
