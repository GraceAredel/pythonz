import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--address", action="store",
                     default="https://pythoz.net/login", help="login page")
    parser.addoption("--browser", action="store",
                     default="firefox", help="browser name")


@pytest.fixture(scope="session", autouse=True)
def driver(request):
    browser = request.config.getoption("--browser")
    if browser == 'firefox':
        wd = webdriver.Firefox()
        wd.maximize_window()
    elif browser == 'chrome':
        wd = webdriver.Chrome()
        wd.maximize_window()
    else:
        wd = webdriver.Ie()

    wd.get(request.config.getoption("--address"))
    yield wd
    wd.quit()


@pytest.fixture(scope="session")
def pythonz_login_page(request):
    return request.config.getoption("--address")


@pytest.fixture(scope="session")
def login(driver, request):
    """login into your account"""
    url = request.config.getoption("--address")
    driver.get(url)
    login_register_page = LoginPage(driver)
    login_register_page.login(username="", password="")


@pytest.fixture(scope="function")
def refresh_page(driver):
    driver.refresh()
