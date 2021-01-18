from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
from src.search_properties import SearchProperties

def find_thumbnail_urls(driver, properties:SearchProperties):
    driver.get("https://www.google.pl/imghp?hl=en")
    elem = driver.find_element_by_name("q")
    elem.send_keys(properties.key)
    elem.send_keys(Keys.RETURN)
    SCROLL_PAUSE_TIME = 1
    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            try:
                driver.find_element_by_css_selector(".mye4qd").click()
            except:
                break
        last_height = new_height

    images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
    for image in images:
        image_url = image.get_attribute("src")
        yield image_url
        


