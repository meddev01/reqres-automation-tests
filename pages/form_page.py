from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FormPage:
    def __init__(self, driver):
        self.driver = driver

    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    JOB_TITLE = (By.ID, "job-title")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary")

    def fill_form(self, first, last, job):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.FIRST_NAME))
        self.driver.find_element(*self.FIRST_NAME).send_keys(first)
        self.driver.find_element(*self.LAST_NAME).send_keys(last)
        self.driver.find_element(*self.JOB_TITLE).send_keys(job)

    def submit(self):
        self.driver.find_element(*self.SUBMIT_BUTTON).click()
