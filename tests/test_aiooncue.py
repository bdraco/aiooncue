#!/usr/bin/env python
# pylint: disable=protected-access

"""Tests for `aiooncue` package."""

from unittest.mock import Mock, patch
import pytest

import aiohttp


from aiooncue import (
    LOGIN_INVALID_PASSWORD,
    LOGIN_INVALID_USERNAME,
    LoginFailedException,
    Oncue,
    ServiceFailedException,
)

@pytest.mark.asyncio
async def test_login():
    """Tests login"""

    # Successful Login
    api = Oncue("username", "password", Mock())
    with patch.object(api, "_get") as mock_get:
        mock_get.return_value = {"sessionkey": "123"}
        await api.async_login()
    assert api._sessionkey == "123"
    assert api._auth_invalid == 0

    # Relogin and return an invalid username, this should not make the auth_invalid
    with patch.object(api, "_get") as mock_get:
        mock_get.return_value = {"code": LOGIN_INVALID_USERNAME, "sessionkey": "321"}
        with pytest.raises(ServiceFailedException):
            await api.async_login()
    assert api._auth_invalid == 0

    # Relogin and return an invalid password, this should make the auth_invalid
    with patch.object(api, "_get") as mock_get:
        mock_get.return_value = {
            "code": LOGIN_INVALID_PASSWORD,
            "sessionkey": "321",
            "message": "bad username",
        }
        with pytest.raises(LoginFailedException):
            await api.async_login()
    assert api._auth_invalid == f"bad username ({LOGIN_INVALID_PASSWORD})"
