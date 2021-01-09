from flask import Flask
import selenium_driver

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/task')
def task():
    driver = selenium_driver.init_driver()
    driver.quit()
    return 'driver works'

