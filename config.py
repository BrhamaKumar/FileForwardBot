from os import getenv


API_ID = int(getenv("API_ID", "10000844"))
API_HASH = getenv("API_HASH", "776f257fc1d1f8aa4aea9dd35d10a45b")
BOT_TOKEN = getenv("BOT_TOKEN", "7025582687:AAGv9iGPm2xj-R0axV0rri3z1WsKvZpbe-Q")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5638987940 6962753370 5019308664").split()))

# --------------- Channel ------------ #
FORWARD_IDS = -1002177136098
MOVIES_ID = -1002177136098
SERIES_ID = -1002130072841
