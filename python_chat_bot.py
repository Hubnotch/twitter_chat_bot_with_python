from selenium  import webdriver
from selenium.webdriver.common.keys import Keys
import time

class TwitterBot:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/')
        time.sleep(10)
        email = bot.find_element_by_name('session[username_or_email]')
        password = bot.find_element_by_name('session[password]')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(10)


def like_tweet(self,hashtag):
    bot = self.bot
    bot.get('https://twitter.com/search?q='+hashtag+'&src=typed_query')
    time.sleep(10)
    for i in range(1,3):
        bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(3)
        tweets = bot.find_elements_by_class_name('tweet')

Ekene = TwitterBot('love2ekene@yahoo.com', 'ama2gouser')
Ekene.login()
Ekene.like_tweet('webdevelopment')

#ed =  TwitterBot('storyofedd@yahoo.com', 'dimitrimarco94')
#session[username_or_email]