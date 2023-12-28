class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "6550000741"
    sudo_users = "6550000741", "6758236533"
    GROUP_ID = -1002028197914
    TOKEN = "6926055023:AAEZp5tXJ0CjNzyhuzVIGe6raFDgsp-XVqw"
    mongo_url = "mongodb+srv://HaremDBBot:ThisIsPasswordForHaremDB@haremdb.swzjngj.mongodb.net/?retryWrites=true&w=majority"
    PHOTO_URL = ["https://graph.org/file/722b32b3a4bb4a882759b.jpg", "https://telegra.ph/file/4211fb191383d895dab9d.jpg"]
    SUPPORT_CHAT = "Grab_Your_Characters_6"
    UPDATE_CHAT = "Yumeko_toxbot_support"
    BOT_USERNAME = "Collect_Em_AllBot"
    CHARA_CHANNEL_ID = "-1001873432374"
    api_id = 20967639
    api_hash = "f0cc55917e860f93d2c9aaa4a7caa69c"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
