import pytest

from src.domain.exceptions.model import FileNotFound
from src.domain.models.request.model import TermModel
from src.repositories.terms.repository import (
    TermRepository,
)
from src.repositories.cache.repository import CacheRepository
from src.services.terms.service import TermService
from unittest.mock import patch
from pytest import mark

term_model_dummy = TermModel(file_type="term_refusal")


# @mark.asyncio
# @patch.object(TermService, "_BankVisualIdentityService__get_logo_url")
# async def test_get_bank_logo(get_url_mock):
#     url_return_value = "https://www.image_link_here.com"
#     get_url_mock.return_value = url_return_value
#     result = await TermService.get_bank_logo(term_model_dummy)
#     assert await get_url_mock.called_with(term_model_dummy.bank_code)
#     assert result == url_return_value


# def test_get_logo_path(monkeypatch):
#     monkeypatch.setattr(TermService, "_BankVisualIdentityService__images_folder", "banks")
#     expected_result = f"banks/79/logo.png"
#     result = TermService._BankVisualIdentityService__get_logo_path("79")
#     assert result == expected_result


@mark.asyncio
@patch.object(
    TermRepository,
    "get_term_link",
    return_value="https://www.term_link_here.com",
)
@patch.object(CacheRepository, "save_term_in_cache", return_value=True)
@patch.object(
    CacheRepository, "get_cached_term", return_value="https://www.term_link_here.com"
)
async def test_get_term_url_when_there_is_cache(
    get_in_cache_mock, save_in_cache_mock, generate_url_mock
):
    result = await TermService.get_term_url(term_model_dummy)
    assert type(result) == str
    assert get_in_cache_mock.called
    assert not generate_url_mock.called


@mark.asyncio
@patch.object(
    TermRepository,
    "get_term_link",
    return_value="https://www.term_link_here.com",
)
@patch.object(CacheRepository, "save_term_in_cache", return_value=True)
@patch.object(CacheRepository, "get_cached_term", return_value=None)
async def test_get_term_url_when_there_is_no_cache(
    get_in_cache_mock, save_in_cache_mock, generate_url_mock
):
    result = await TermService.get_term_url(term_model_dummy)
    assert type(result) == str
    assert get_in_cache_mock.called
    assert save_in_cache_mock.called
    assert generate_url_mock.called
