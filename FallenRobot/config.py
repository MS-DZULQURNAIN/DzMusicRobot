class Config(object):
    LOGGER = True

    API_ID = 16452568
    API_HASH = "f936697c5c9e5bffd433babef7a4e4c9"
    TOKEN = "6049689032:AAH_Nmx-icacIb5FEAolpLdyiUnZjH11SU4"
    OWNER_ID = 1337085565
    EVENT_LOGS = (-1001935424604)
    SUPPORT_CHAT = "envSample"
    DATABASE_URL = "postgres://xgjapvne:JAVP4wiquJr5a-99moi-XV4EYxBZ4F3X@hansken.db.elephantsql.com/xgjapvne"
    MONGO_DB_URI = "mongodb+srv://elia:chan@elia.peyngcs.mongodb.net/?retryWrites=true&w=majority"
    START_IMG = "https://telegra.ph/file/d3b40cbdcbd84bfca790d.jpg"
    CASH_API_KEY = "ZMOE8Q6BE25J7BEU"
    TIME_API_KEY = "J1BBEIOV38CZ"

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = [1337085565]  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
