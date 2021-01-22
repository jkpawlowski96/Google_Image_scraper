from flask import render_template, send_file
from src import crawling, selenium_driver, app, utils
from src.search_properties import SearchProperties

@app.route('/')
def home():
    return render_template('index.html',)

@app.route('/task')
def task(methods = ['GET','POST']):
    driver = selenium_driver.init_driver()
    prop = SearchProperties()
    images = crawling.find_thumbnail_urls(driver,prop)
    tmp_dir = utils.create_tmp_dir()
    utils.save_base64_images(images, tmp_dir)
    driver.quit()
    zip_path = utils.make_zip(tmp_dir)
    download_name = 'data.zip'
    return send_file(zip_path, attachment_filename = download_name, as_attachment = True)



