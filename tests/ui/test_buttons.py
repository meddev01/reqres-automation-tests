import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pytest
from pages.home_page import HomePage

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_buttons_page(driver, base_url):
    home = HomePage(driver)
    home.open(base_url)
    home.go_to_buttons()

    # Attendre que la page Buttons soit bien chargée
    WebDriverWait(driver, 10).until(EC.url_contains("buttons"))

    # ✅ Cibler le bouton par sa classe CSS (et non par ID)
    wait = WebDriverWait(driver, 10)
    button = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".btn.btn-lg.btn-primary"))
    )

    assert (
        button.is_displayed()
    ), "❌ Le bouton 'Primary' n’a pas été trouvé sur la page Buttons"
    print("✅ Le bouton Primary a bien été détecté sur la page Buttons.")
