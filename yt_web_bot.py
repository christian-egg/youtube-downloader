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

video_url = 'https://www.youtube.com/watch?v=fztKqreP1pk'
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

#Wait for page to load
time.sleep(5)

# Wait until either a download button or an error tag is found
is_done_loading = False
download_button = None

while (is_done_loading != True):
    # Check for download button
    try:
        download_button = driver.find_element_by_link_text("Download")
        is_done_loading = True
    except NoSuchElementException:
        try:
            error_message = driver.find_element_by_tag_name("error")
            print("Video could not be converted. Check that your URL is correct.")
            is_done_loading = True
        except NoSuchElementException:
            time.sleep(5)


if download_button != None:
    download_button.click()
