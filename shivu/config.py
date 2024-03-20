class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "6529892817"
    sudo_users = "6529892817", "6693744800"
    GROUP_ID = -1002139608040
    TOKEN = "6859073442:AAFFCb2qA648IETNkpgASW8h-gKSQZx-nZg"
    mongo_url = "mongodb+srv://Teamix1:teamix1@cluster0.y7h1qxl.mongodb.net/?retryWrites=true&w=majority"
    PHOTO_URL = ["https://telegra.ph/file/a8f201f8d09943dc57a86.jpg", "https://telegra.ph/file/a8f201f8d09943dc57a86.jpg"]
    SUPPORT_CHAT = "Muichiro_support"
    UPDATE_CHAT = "Muichiro_Updates"
    BOT_USERNAME = "Grab_carsbot"
    CHARA_CHANNEL_ID = "-1002082423339"
    api_id = 20967639
    api_hash = "f0cc55917e860f93d2c9aaa4a7caa69c"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
