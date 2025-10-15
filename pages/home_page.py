from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    # Liens vers les différentes sections
    BUTTONS_LINK = (By.LINK_TEXT, "Buttons")

    FORM_LINK = (By.LINK_TEXT, "Complete Web Form")
    MODAL_LINK = (By.LINK_TEXT, "Modal")

    def open(self, base_url):
        self.driver.get(base_url)

    def go_to_buttons(self):
        self.driver.find_element(*self.BUTTONS_LINK).click()

    def go_to_form(self):
        self.driver.find_element(*self.FORM_LINK).click()

    def go_to_modal(self):
        self.driver.find_element(*self.MODAL_LINK).click()
