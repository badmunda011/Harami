from VipX.core.bot import Vip
from VipX.core.dir import dirr
from VipX.core.git import git
from VipX.core.userbot import Userbot
from VipX.misc import dbb, heroku, sudo

from .logging import LOGGER


dirr()

git()

dbb()

heroku()

sudo()

# Clients
app = Vip()

userbot = Userbot()


from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()
