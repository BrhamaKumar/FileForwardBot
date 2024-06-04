from os import getenv


API_ID = int(getenv("API_ID", "10000844"))
API_HASH = getenv("API_HASH", "776f257fc1d1f8aa4aea9dd35d10a45b")
BOT_TOKEN = getenv("BOT_TOKEN", "7025582687:AAGv9iGPm2xj-R0axV0rri3z1WsKvZpbe-Q")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6750546542 6962753370 5019308664").split()))

# --------------- Channel ------------ #
FORWARD_IDS = -1002032466369
MOVIES_ID = -1002060165607
SERIES_ID = -1002130072841
