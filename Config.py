import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "29531177"))
    API_HASH = os.environ.get("API_HASH", "aa97e198b3c514f96e98cd45c2371bd2")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", 6267885804:AAHamFNKpjcZ7xQjnBcaz7em6SYyfpQCl0M)
    STRING_SESSION = os.environ.get("STRING_SESSION", 1BVtsOI0Bu4qx01GePjcuXdMgWCNiKcNm-kAVJ9YCezSGhw_n47sByestfz6oolZa4S9gyZa1jGYC2FOiJJMdNvzlOM1UihlDYxL-Ojl--Gs07GF9PhJ1hm8XxKYKkljpMorwU3FSgDnJdo9nqZoRdQ-XSCJJMs9VTQ062mzrNGeZL9oL1cPcyxUCppHbfAPcw01qJQISwjw1TJ8pWyOqHfTt9XeLo1y6_gp33MPw9h6Q6k1VBgsCjVkz8W2lsNneBr_DZHCo_N5T5-_Ag8g0a88yGczwPTYjtzzXFN-1nmDo3gwDktS7tJ8ZRudoysWQR-O79IdBsLZ5xLmDO6gZkAdXNxmhM64=)
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "music122005bot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5954282840")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
