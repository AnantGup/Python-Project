from selenium import webdriver
import time
import random

driver = webdriver.Chrome('/usr/bin/chromedriver')

videos = [
    "https://youtu.be/FRz_tUaTVJU",
    "https://youtu.be/FRz_tUaTVJU",
]

random_video = random.randint(0, 1)

for i in range(500):
    print("Running the Video for {} time".format(i))
    random_video = random.randint(0, 1)
    driver.get(videos[random_video])
    sleep_time = random.randint(10, 15)
    time.sleep(sleep_time)

driver.quit()
