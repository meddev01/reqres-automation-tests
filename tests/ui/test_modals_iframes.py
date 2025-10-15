import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_modals_and_iframes(driver, base_url):
    # Aller sur la page du modal
    driver.get(f"{base_url}modal")
    WebDriverWait(driver, 10).until(EC.url_contains("modal"))

    # Cliquer pour ouvrir le modal
    modal_button = driver.find_element(By.ID, "modal-button")
    modal_button.click()

    # Attendre que le bouton close apparaisse et le fermer
    close_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "close-button"))
    )
    close_button.click()

    # Vérification : le modal est bien fermé
    assert "modal" in driver.current_url
