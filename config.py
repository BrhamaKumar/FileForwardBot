from os import getenv


API_ID = int(getenv("API_ID", "10000844"))
API_HASH = getenv("API_HASH", "776f257fc1d1f8aa4aea9dd35d10a45b")
BOT_TOKEN = getenv("BOT_TOKEN", "6998167875:AAF6c7Y0cI2XydqWGphthDkZNjr9TwdDnbU")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5638987940 5019308664").split()))

# --------------- Channel ------------ #
FORWARD_IDS = -1002177136098
MOVIES_ID = -1002177136098
SERIES_ID = -1001914996147
