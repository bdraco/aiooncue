"""Top-level package for Async Oncue."""
from __future__ import annotations

from dataclasses import dataclass
import json

import aiohttp

__author__ = """J. Nick Koston"""
__email__ = "nick@koston.org"
__version__ = "0.3.4"

from .const import NAME_TO_SENSOR_ID

REQUIRED_DEVICE_KEYS = {
    "displayname",
    "devicestate",
    "productname",
    "version",
    "serialnumber",
}
REQUIRED_DEVICE_SENSOR_KEYS = {"FirmwareVersion", "GensetModelNumberSelect"}

DEFAULT_REQUEST_TIMEOUT = 15

BASE_ENDPOINT = "https://api.kohler.com/krm/v1"

COMMAND_ENDPOINT = "/devices/command"

LIST_DEVICES_ENDPOINT = "/devices/listdevices"
LIST_DEVICES_PARAMETERS = "[4,11,60,69,102,91,114,115,549]"

DEVICE_DETAILS_ENDPOINT = "/devices/devicedetails"
DEVICE_DETAILS_PARAMETERS = (
    "[2,3,4,6,7,11,18,20,32,55,56,60,69,93,102,113,114,115,864,870,872,1671]"
)

ALL_DETAILS_NAMES = [
    "Controller Type",  # 2
    "Current Firmware",  # 3
    "Engine Speed",  # 4
    "Engine Target Speed",  # 5
    "Engine Oil Pressure",  # 6
    "Engine Coolant Temperature",  # 7
    "Battery Voltage",  # 11
    "Lube Oil Temperature",  # 18
    "Generator Controller Temperature",  # 20
    "Engine Compartment Temperature",  # 32
    "Generator True Total Power",  # 55
    "Generator True Percent Of Rated Power",  # 56
    "Generator Voltage AB",  # 57
    "Generator Voltage Average Line To Line",  # 60
    "Generator Current Average",  # 68
    "Generator Frequency",  # 69
    "Genset Model Number Select",  # 91
    "Generator Serial Number",  # 93
    "Generator Controller Serial Number",  # 95
    "Generator State",  # 102
    "Generator Controller Clock Time",  # 113,
    "Generator Controller Total Operation Time",  # 114,
    "Engine Total Run Time",  # 115,
    "Engine Total Run Time Loaded",  # 116,
    "Engine Total Number Of Starts",  # 118,
    "Genset Total Energy",  # 119   -- note that this can be 1.1986518E7
    "Ats Contactor Position",  # 549
    "Ats Sources Available",  # 550,
    "Source1 Voltage Average Line To Line",  # 588,
    "Source2 Voltage Average Line To Line",  # 623,
    "IP Address",  # 864,
    "Mac Address",  # 869
    "Connected Server IP Address",  # 870
    "Network Connection Established",  # 872
    "Serial Number",  # 908
    "Latest Firmware",  # 1671
]

ALL_DEVICES_PARAMETERS = json.dumps(
    [[NAME_TO_SENSOR_ID[name] for name in ALL_DETAILS_NAMES]], separators=(",", ":")
)

LOGIN_FAILED_CODES = {0: "Unknown", 1200: "Session Expired", 1207: "Invalid Password"}

LOGIN_ENDPOINT = "/users/connect"


@dataclass
class OncueSensor:
    name: str
    display_name: str
    value: str
    display_value: str
    unit: str | None


@dataclass
class OncueDevice:
    name: str
    state: str
    product_name: str
    hardware_version: str
    serial_number: str
    sensors: dict[str, OncueSensor]


class LoginFailedException(Exception):
    """Login failed exception."""


class Oncue:
    """Async oncue api."""

    def __init__(
        self,
        username: str,
        password: str,
        websession: aiohttp.ClientSession,
        timeout: int = DEFAULT_REQUEST_TIMEOUT,
    ):
        """Create oncue async api object."""
        self._websession = websession
        self._timeout = timeout
        self._username = username
        self._password = password
        self._auth_invalid = 0

    async def _get(self, endpoint: str, params=None) -> dict:
        """Make a get request."""
        response = await self._websession.request(
            "GET",
            f"{BASE_ENDPOINT}{endpoint}",
            timeout=self._timeout,
            params=params,
        )
        return await response.json()

    async def _get_authenticated(self, endpoint: str, params=None) -> dict:
        if self._auth_invalid:
            raise LoginFailedException(self._auth_invalid)

        for _ in range(2):
            data = await self._get(endpoint, {"sessionkey": self._sessionkey, **params})
            if "code" not in data or data["code"] not in LOGIN_FAILED_CODES:
                return data
            await self.async_login()

        raise LoginFailedException(self._auth_invalid)

    async def async_login(self) -> None:
        """Call api to login"""
        login_data = await self._get(
            LOGIN_ENDPOINT, {"username": self._username, "password": self._password}
        )

        if "sessionkey" not in login_data:
            self._auth_invalid = f"{login_data['message']} ({login_data.get('code')})"
            raise LoginFailedException(self._auth_invalid)

        self._sessionkey = login_data["sessionkey"]

    async def async_fetch_all(self) -> dict[str, OncueDevice]:
        """Fetch all devices."""
        devices = await self.async_list_devices_with_params()
        indexed_devices: dict[str, OncueDevice] = {}
        for device in devices:
            if REQUIRED_DEVICE_KEYS.intersection(device) != REQUIRED_DEVICE_KEYS:
                continue
            sensors: dict[str, OncueSensor] = {}
            for sensor in device["parameters"]:
                value = sensor["value"]
                name = sensor["name"]
                unit = None
                if len(sensor["displayvalue"]) > len(str(value)) + 1:
                    unit = sensor["displayvalue"][len(str(value)) + 1 :]
                sensors[name] = OncueSensor(
                    name=name,
                    display_name=sensor["displayname"],
                    value=sensor["value"],
                    display_value=sensor["displayvalue"],
                    unit=unit,
                )
            if (
                REQUIRED_DEVICE_SENSOR_KEYS.intersection(sensors)
                != REQUIRED_DEVICE_SENSOR_KEYS
            ):
                continue
            indexed_devices[device["id"]] = OncueDevice(
                name=device["displayname"],
                state=device["devicestate"],
                product_name=device["productname"],
                hardware_version=device["version"],
                serial_number=device["serialnumber"],
                sensors=sensors,
            )
        return indexed_devices

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

    async def async_device_details(self, device: str) -> dict:
        """Call api to get device devices"""
        return await self._get_authenticated(
            LIST_DEVICES_ENDPOINT,
            {"device": device, "parameters": DEVICE_DETAILS_PARAMETERS},
        )

    async def async_start_loaded_full_speed_exercise(self, device: str) -> None:
        """Call api to stat a loaded full speed exercise."""
        await self._async_do_action(device, "startloadedfullspeedexercise")

    async def async_start_unloaded_full_speed_exercise(self, device: str) -> None:
        """Call api to stat an unloaded full speed exercise."""
        await self._async_do_action(device, "startunloadedfullspeedexercise")

    async def async_start_unloaded_cycle_exercise(self, device: str) -> None:
        """Call api to stat an unloaded cycle exercise."""
        await self._async_do_action(device, "startunloadedcycleexercise")

    async def async_end_exercise(self, device: str) -> None:
        """Call api to end an exercise."""
        await self._async_do_action(device, "endexercise")

    async def _async_do_action(self, device: str, action: str) -> None:
        """Call api to do an action."""
        await self._get_authenticated(
            LIST_DEVICES_ENDPOINT,
            {"device": device, "service": "doaction", "value": action},
        )
