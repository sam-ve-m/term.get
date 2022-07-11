from pydantic import BaseModel

from src.domain.enums.terms import TermsFileType


class TermModel(BaseModel):
    file_type: TermsFileType
