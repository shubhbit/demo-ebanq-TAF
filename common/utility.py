import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait_for_element_load(driver, timer, element):
    """
    custom utility function to wait for a particular element to be laoded
    driver object: driver to be used
    timer int: timeout
    element tuple: tuple of By and locator e.g. (By.XPATH, "XPATH")
    return bool: whether element is present or not.
    """
    try:
        WebDriverWait(driver, timer).until(
            EC.presence_of_element_located(element))
        return True
    except Exception as e:
        return False


def wait(timer):
    time.sleep(timer)
