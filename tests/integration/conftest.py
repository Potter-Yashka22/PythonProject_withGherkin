
from src.sel import *

import pytest

@pytest.fixture(scope='function')
def start():
    options=Options()
    options.add_argument("--headless")
    driver=webdriver.Firefox(options=options)
    driver.set_page_load_timeout(4)
    driver.implicitly_wait(5)
    try:
        driver.get('https://www.saucedemo.com/')
    except TimeoutException:
        print('сайт не грузит до конца')
    yield driver
    driver.quit()