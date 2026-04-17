import pytest
from selenium import webdriver
import os
from datetime import datetime


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver", None)

        if driver:
            os.makedirs("screenshots", exist_ok=True)

            file_name = f"{item.name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            driver.save_screenshot(f"screenshots/{file_name}")