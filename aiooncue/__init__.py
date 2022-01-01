"""Top-level package for Async Oncue."""

__author__ = """J. Nick Koston"""
__email__ = "nick@koston.org"
__version__ = "0.2.2"


DEFAULT_REQUEST_TIMEOUT = 15

BASE_ENDPOINT = "https://api.kohler.com/krm/v1"

LIST_DEVICES_ENDPOINT = "/devices/listdevices"
LIST_DEVICES_PARAMETERS = "[4,11,60,69,102,91,114,115,549]"

DEVICE_DETAILS_ENDPOINT = "/devices/devicedetails"
DEVICE_DETAILS_PARAMETERS = (
    "[2,3,4,6,7,11,18,20,32,55,56,60,69,93,102,113,114,115,864,870,872,1671]"
)

ALL_DEVICES_PARAMETERS = (
    "[2,3,4,6,7,11,18,20,32,55,56,60,69,91,93,102,113,114,115,549,864,870,872,1671]"
)


LOGIN_FAILED_CODES = {0, 1200}

LOGIN_ENDPOINT = "/users/connect"


class LoginFailedException(Exception):
    """Login failed exception."""


class Oncue:
    """Async oncue api."""

    def __init__(self, username, password, websession, timeout=DEFAULT_REQUEST_TIMEOUT):
        """Create oncue async api object."""
        self._websession = websession
        self._timeout = timeout
        self._username = username
        self._password = password
        self._auth_invalid = 0

    async def _get(self, endpoint, params=None):
        """Make a get request."""
        response = await self._websession.request(
            "GET",
            f"{BASE_ENDPOINT}{endpoint}",
            timeout=self._timeout,
            params=params,
        )
        return await response.json()

    async def _get_authenticated(self, endpoint, params=None):
        if self._auth_invalid:
            raise LoginFailedException(self._auth_invalid)

        for _ in range(2):
            data = await self._get(endpoint, {"sessionkey": self._sessionkey, **params})
            if "code" not in data or data["code"] not in LOGIN_FAILED_CODES:
                return data

            self._auth_invalid = data["message"]
            await self.async_login()

    async def async_login(self):
        """Call api to login"""
        login_data = await self._get(
            LOGIN_ENDPOINT, {"username": self._username, "password": self._password}
        )

        if "sessionkey" not in login_data:
            self._auth_invalid = login_data["message"]
            raise LoginFailedException(self._auth_invalid)

        self._sessionkey = login_data["sessionkey"]

    async def async_list_devices_with_params(self):
        """Call api to list devices."""
        return await self._get_authenticated(
            LIST_DEVICES_ENDPOINT,
            {
                "events": "active",
                "showperipheraldetails": "true",
                "parameters": ALL_DEVICES_PARAMETERS,
            },
        )

    async def async_list_devices(self):
        """Call api to list devices"""
        return await self._get_authenticated(
            LIST_DEVICES_ENDPOINT,
            {
                "events": "active",
                "showperipheraldetails": "true",
                "parameters": LIST_DEVICES_PARAMETERS,
            },
        )

    async def async_device_details(self, device):
        """Call api to get device devices"""
        return await self._get_authenticated(
            LIST_DEVICES_ENDPOINT,
            {"device": device, "parameters": DEVICE_DETAILS_PARAMETERS},
        )
