from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
import time
import sys

ytmp3_url = "https://ytmp3.cc/youtubemp3/"

#if len(sys.argv) != 2:
    #print("Incorrect number of arguments. \nFormat: python yt_web_bot.py [video url] [file format (mp3 or mp4)]")
    #quit()

video_url = 'empty'
#video_url = sys.argv[1]
#format = sys.argv[0]

#if format != "mp3" and format != "mp4":
    #print("Please specify your desired file format (mp3 or mp4). \nFormat: python yt_web_bot.py [video url] [file format (mp3 or mp4)]")
    #quit()

driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.GOOGLE).install())
driver.get(ytmp3_url)

# Fill in form with youtube link and click 'convert'
input_field = driver.find_element_by_id('input')
input_field.send_keys(video_url)

driver.find_element_by_id('submit').click()

# Make sure the link worked properly
try:
    driver.find_element_by_id('button')
except NoSuchElementException:
    print("Video could not be converted. Check that your URL is correct.")
    quit()

breakpoint()
