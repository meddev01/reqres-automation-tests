from selenium.webdriver.common.by import By


class ModalPage:
    def __init__(self, driver):
        self.driver = driver

    OPEN_BUTTON = (By.ID, "modal-button")
    CLOSE_BUTTON = (By.ID, "close-button")

    def open_modal(self):
        self.driver.find_element(*self.OPEN_BUTTON).click()

    def close_modal(self):
        self.driver.find_element(*self.CLOSE_BUTTON).click()
