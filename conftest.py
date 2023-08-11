import pytest
from selenium import webdriver
from views.home import Home

# Set commands line options
def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome')

@pytest.fixture
def browser(request):
    brow = request.config.getoption('browser').lower()
    if brow not in ['chrome', 'firefox', 'opera']:
        raise ValueError('--Browser value must be chrome, firefox or opera')
    return brow

@pytest.fixture
def driver(browser):
    
    if(browser == 'firefox'):
        driver = webdriver.Firefox()
    # Opera is not supported   
    #elif(args.browser.lower() == 'opera'):
    else:
        driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
    
@pytest.fixture
def home(driver):
    return Home(driver)

