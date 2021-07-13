from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import sys

if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Incorrect number of arguments. \nFormat: python yt_web_bot.py [video url] [file format (mp3 or mp4)]")
        quit()

    url = sys.argv[1]
    format = sys.argv[2]

    if format != "mp3" and format != "mp4":
        print("Please specify your desired file format (mp3 or mp4). \nFormat: python yt_web_bot.py [video url] [file format (mp3 or mp4)]")
        quit()

