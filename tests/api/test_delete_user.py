import pytest
import requests

BASE_URL = "https://reqres.in/api"


@pytest.mark.api
def test_delete_user():
    response = requests.delete(f"{BASE_URL}/users/2")
    print(f"🧾 Statut reçu : {response.status_code}")
    # L'API publique peut renvoyer 204 (succès) ou 401 (refus)
    assert response.status_code in [204, 401]
    if response.status_code == 204:
        print("✅ Utilisateur supprimé avec succès.")
    else:
        print("⚠️ Accès non autorisé à la suppression (réponse 401).")
