from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os

SELENIUM_HOST = os.environ.get('SELENIUM_GRID_HOST', 'localhost')
print(f'Selenium Host : {SELENIUM_HOST}')
SELENIUM_PORT = '4444'

def init_driver():
    driver = webdriver.Remote(  command_executor=f'http://{SELENIUM_HOST}:{SELENIUM_PORT}',
                                desired_capabilities=DesiredCapabilities.CHROME )
                                
    return driver


