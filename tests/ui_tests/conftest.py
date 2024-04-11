import pytest
from utilities.webdriver import WebDriverClass
from utilities.enums import Driver

driver = WebDriverClass(Driver.CHROME).get_driver()


@pytest.fixture(autouse=True)
def browser():
    yield driver
    driver.quit()

print(12312312312312312312312)