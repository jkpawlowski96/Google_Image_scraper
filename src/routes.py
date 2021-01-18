from flask import render_template
from src import crawling, selenium_driver, app
from src.search_properties import SearchProperties


@app.route('/')
def home():
    return render_template('index.html',)

@app.route('/task')
def task():
    driver = selenium_driver.init_driver()
    prop = SearchProperties()
    urls = crawling.find_thumbnail_urls(driver,prop)
    resp = 'table'
    resp += '<tr>\n'
    for url in urls:
        resp += f'<td> {url} </td>\n'
    resp += '</tr>'
    driver.quit()
    return resp


