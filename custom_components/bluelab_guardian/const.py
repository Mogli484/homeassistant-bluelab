from datetime import timedelta

DOMAIN = "bluelab_guardian"
CONF_API_TOKEN = "ed_chws4gyaa939b0gd7pbnotfgj83lgp7hqfvy8wll0cvk21r3uzsvbmxclpbpv9hv"
CONF_ORGANIZATION_ID = "98a0a700-f5f6-11ef-a5ae-8dff4b34f2dc"
DEVICE_LIST_URL = "https://api.edenic.io/api/v1/device/"
TELEMETRY_URL = "https://api.edenic.io/api/v1/telemetry/"
DEVICE_ATTRIBUTE_URL = "https://api.edenic.io/api/v1/device-attribute/"
TELEMETRY_UPDATE_INTERVAL = timedelta(seconds=70)
ATTRIBUTE_UPDATE_INTERVAL = timedelta(seconds=70)
