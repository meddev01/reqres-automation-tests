import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from pages.home_page import HomePage
from pages.form_page import FormPage


def test_complete_form(driver, base_url):
    home = HomePage(driver)
    form = FormPage(driver)

    home.open(base_url)
    home.go_to_form()

    form.fill_form("Mohamed", "Benchekroun", "QA Engineer")
    form.submit()

    assert (
        "thanks" in driver.page_source.lower()
    ), "Le message de validation n'apparaît pas"
