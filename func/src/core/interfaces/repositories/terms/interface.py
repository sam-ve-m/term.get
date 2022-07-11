from abc import ABC, abstractmethod

from src.domain.enums.terms import TermsFileType


class ITermRepository(ABC):
    @classmethod
    @abstractmethod
    async def get_term_link(cls, term: TermsFileType) -> str:
        pass
