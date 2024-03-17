class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "6758236533"
    sudo_users = "6758236533", "6758236533"
    GROUP_ID = -1002074852216
    TOKEN = "6684851281:AAGgGgYXwzoXKAQ21S2Z9oUCl3Gx8byqlfU"
    mongo_url = "mongodb+srv://HaremDBBot:ThisIsPasswordForHaremDB@haremdb.swzjngj.mongodb.net/?retryWrites=true&w=majority"
    PHOTO_URL = ["https://graph.org/file/722b32b3a4bb4a882759b.jpg", "https://telegra.ph/file/4211fb191383d895dab9d.jpg"]
    SUPPORT_CHAT = "animefed2"
    UPDATE_CHAT = "Ix_Updates"
    BOT_USERNAME = "Collect_Em_AllBot"
    CHARA_CHANNEL_ID = "-1002141220919"
    api_id = 20967639
    api_hash = "f0cc55917e860f93d2c9aaa4a7caa69c"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
