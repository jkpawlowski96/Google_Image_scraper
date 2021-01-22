from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
from src.search_properties import SearchProperties
from src.image import ImageBase64

def find_thumbnail_urls(driver, properties:SearchProperties):
    driver.get("https://www.google.pl/imghp?hl=en")
    elem = driver.find_element_by_name("q")
    elem.send_keys(properties.key)
    elem.send_keys(Keys.RETURN)
    SCROLL_PAUSE_TIME = 1
    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")
    found_images = []
    while True:
        images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
        for image in images:
            if image not in found_images:
                found_images.append(image)
        if len(found_images) >= properties.max:
            found_images = found_images[:properties.max]
            break
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            pass
            try:
                driver.find_element_by_css_selector(".mye4qd").click()
            except:
                break
        last_height = new_height


    for image in found_images:
        image_src = image.get_attribute("src")
        image_base_64 = ImageBase64(image_src)
        yield image_base_64
        
    


