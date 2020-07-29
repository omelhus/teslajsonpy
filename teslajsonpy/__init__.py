#  SPDX-License-Identifier: Apache-2.0
"""
Python Package for controlling Tesla API.

For more details about this api, please refer to the documentation at
https://github.com/zabuldon/teslajsonpy
"""
from teslajsonpy.controller import Controller
from teslajsonpy.exceptions import TeslaException, UnknownPresetMode
from teslajsonpy.homeassistant.battery_sensor import Battery, Range
from teslajsonpy.homeassistant.binary_sensor import (
    ChargerConnectionSensor,
    OnlineSensor,
    ParkingSensor,
)
from teslajsonpy.homeassistant.charger import ChargerSwitch, ChargingSensor, RangeSwitch
from teslajsonpy.homeassistant.climate import Climate, TempSensor
from teslajsonpy.homeassistant.gps import GPS, Odometer
from teslajsonpy.homeassistant.lock import Lock
from teslajsonpy.homeassistant.sentry_mode import SentryModeSwitch
from teslajsonpy.homeassistant.trunk import FrunkLock, TrunkLock

from .__version__ import __version__

__all__ = [
    "Battery",
    "Range",
    "ChargerConnectionSensor",
    "ChargingSensor",
    "OnlineSensor",
    "ParkingSensor",
    "ChargerSwitch",
    "RangeSwitch",
    "Climate",
    "TempSensor",
    "Controller",
    "TeslaException",
    "UnknownPresetMode",
    "GPS",
    "Odometer",
    "Lock",
    "SentryModeSwitch",
    "TrunkLock",
    "FrunkLock",
    "__version__",
]
