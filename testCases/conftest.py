import pytest
from selenium import webdriver


@pytest.fixture
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome(executable_path=r'C:\Users\NaazA\PycharmProjects\AmazonProject\Browsers'
                                                  r'\chromedriver.exe')
    elif browser == "edge":
        driver = webdriver.Edge(
            executable_path="C:\\Users\\NaazA\\PycharmProjects\\AmazonProject\\Browsers\\msedgedriver.exe")
    else:
        driver = webdriver.Chrome(executable_path=r'C:\Users\NaazA\PycharmProjects\AmazonProject\Browsers'
                                                  r'\chromedriver.exe')
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


################################################## HTML REports #########################################

def pytest_configure(config):
    config._metadata['Project Name'] = 'Amazon'
    config._metadata['Module Name'] = 'Login'
    config._metadata['Tester'] = 'Naaz'


@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
