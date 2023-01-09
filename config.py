from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("17059958"))
API_HASH = getenv("61f1dff818fccd96e77db4477f360d0d")

BOT_TOKEN = getenv("5948256402:AAFBM7GpPb7NpbSwghA4TzF4bOZVg3hA6Vg")
OWNER_ID = int(getenv("5530347700"))

MONGO_DB_URI = getenv("mongodb+srv://kailasvg:kailasvg@cluster04.gvju7bn.mongodb.net/?retryWrites=true&w=majority")
MUST_JOIN = getenv("Pk_links", None)
