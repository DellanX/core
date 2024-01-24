"""Constants for Torque integration testing."""
from collections.abc import Mapping

from homeassistant.const import CONF_EMAIL

# NOTE, both queries will require 2 additional query parameters.
# 1. eml (Email)
# 2. session (Session ID)
# This packet isn't sent often, and was only seen as the first request for the scrape performed
# Source Query: "eml=<EMAIL>&v=9&session=<SESSION_ID>&id=<ID>&time=1705984435787&profileName=Amy&profileFuelType=0&profileWeight=1400.0&profileVe=88.0&profileFuelCost=0.8981850019934101&profileDisplacement=4.0&profileTankCapacity=79.49364738&profileTankUsed=8.072321734470634&profileVehicleType=9&profileOdometer=16415&profileMPGAdjust=1.0&profileBoostAdjust=0.0&profileDragCoeff=0.3&profileOBDAdjust=1.0"
DATA_PROFILE_QUERY: Mapping[str, str] = {
    "eml": "test@example.org",
    "id": "12345",
    "time": "1705984435787",
    "profileName": "Amy",
    "profileFuelType": "0",
    "profileWeight": "1400.0",
    "profileVe": "88.0",
    "profileFuelCost": "0.8981850019934101",
    "profileDisplacement": "4.0",
    "profileTankCapacity": "79.49364738",
    "profileTankUsed": "8.072321734470634",
    "profileVehicleType": "9",
    "profileOdometer": "16415",
    "profileMPGAdjust": "1.0",
    "profileBoostAdjust": "0.0",
    "profileDragCoeff": "0.3",
    "profileOBDAdjust": "1.0",
}
# This packet is one of many, and contains the sensor header data from an instance of time when the scrape was performed
# Source Query: "eml=<EMAIL>&v=9&session=<SESSION_ID>&id=<ID>&time=1705984435789&userUnitff1005=Â°&userUnitff1006=Â°&userUnitff1001=mph&userUnitff1007=&userUnitff1223=g&userShortNameff1223=Accel&userFullNameff1223=Acceleration Sensor(Total)&userUnit0c=rpm&userShortName0c=Revs&userFullName0c=Engine RPM&userUnit2f=%&userShortName2f=Fuel&userFullName2f=Fuel Level (From Engine ECU)&userUnitff126b=%&userShortNameff126b=Fuel Rem&userFullNameff126b=Fuel Remaining (Calculated from vehicle profile)&userUnitff1271=gal&userShortNameff1271=Fuel Used&userFullNameff1271=Fuel used (trip)"
DATA_HEADER_QUERY: Mapping[str, str] = {
    "eml": "test@example.org",
    "id": "12345",
    "time": "1705984435789",
    "userUnitff1005": "Â°",
    "userUnitff1006": "Â°",
    "userUnitff1001": "mph",
    "userUnitff1007": "",
    "userUnitff1223": "g",
    "userShortNameff1223": "Accel",
    "userFullNameff1223": "Acceleration Sensor(Total)",
    "userUnit0c": "rpm",
    "userShortName0c": "Revs",
    "userFullName0c": "Engine RPM",
    "userUnit2f": "%",
    "userShortName2f": "Fuel",
    "userFullName2f": "Fuel Level (From Engine ECU)",
    "userUnitff126b": "%",
    "userShortNameff126b": "Fuel Rem",
    "userFullNameff126b": "Fuel Remaining (Calculated from vehicle profile)",
    "userUnitff1271": "gal",
    "userShortNameff1271": "Fuel Used",
    "userFullNameff1271": "Fuel used (trip)",
}
# This packet is one of many, and contains the sensor value data from an instance of time when the scrape was performed
# Source Query: eml=<EMAIL>&v=9&session=<SESSION_ID>&id=<ID>&time=1705984473784&kff1005=-97.74798387412254&kff1006=30.430986729228223&kff1001=0.0&kff1007=123.46544647216797&kff1223=-0.01&kc=1178.0&kff126b=10.106546831318784&kff1271=0.04379265942863656
DATA_VALUE_QUERY: Mapping[str, str] = {
    "eml": "test@example.org",
    "v": "9",
    "id": "12345",
    "time": "1705984473784",
    "kff1005": "-97.74798387412254",
    "kff1006": "30.430986729228223",
    "kff1001": "0.0",
    "kff1007": "123.46544647216797",
    "kff1223": "-0.01",
    "kc": "1178.0",
    "kff126b": "10.106546831318784",
    "kff1271": "0.04379265942863656",
}

MOCK_DATA_STEP = {
    CONF_EMAIL: "test@example.org",
}
