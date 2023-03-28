import pytest
import requests

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

resp = requests.get("https://www.localeplanet.com/api/auto/langmap.json")
langs = resp.json().keys()

def typechecker(value):
    msg = "Incorrect langauge paramater; try again with correct one"
    if value not in langs:
        raise pytest.UsageError(msg)
    return value


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en', 
                     help='specify the browser language with --language=langauge, ex. --language=en', type=typechecker)
    

@pytest.fixture
def browser(request):
    options = Options()
    options.add_experimental_option('prefs',{'intl.accept_languages': request.config.getoption("--language")})
    #service = Service("/chromedriver/stable/chromedriver")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    #browser = webdriver.Chrome(options=options, service=service)
    browser = webdriver.Chrome(options=options)
    return browser