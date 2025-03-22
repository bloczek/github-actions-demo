# from app.src.main import return_backwards_string, get_mode
# import unittest
# import os

# class TestMain(unittest.TestCase):
#     def test_return_backwards_string(self):
#         random_string = "Hello World"
#         random_string_reversed = "dlroW olleH"
#         self.assertEqual(random_string_reversed,
#                          return_backwards_string(random_string))
        
#     def test_get_env(self):
#         self.assertEqual(os.environ.get("MODE"), get_mode())

# if __name__ == "__main__":
#     unittest.main()


import os
import pytest
from app.src.main import app
from flask import Flask
from dotenv import load_dotenv
# Tworzenie aplikacji bezpośrednio w pliku testowym

def create_app():
    load_dotenv()
    app = Flask(__name__)
    
    @app.route('/<random_string>')
    def return_backwards_string(random_string):
        return "".join(reversed(random_string))
    
    @app.route('/get-mode')
    def get_mode():
        return os.getenv('MODE')
    
    return app

@pytest.fixture
def app():
    """Fixture zwracający aplikację Flask."""
    return create_app()

@pytest.fixture
def client(app):
    """Konfiguracja klienta testowego."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_return_backwards_string(client):
    test_string = "hello"
    expected = "olleh"
    response = client.get(f'/{test_string}')
    assert response.status_code == 200
    # response.data zwraca bajty, dlatego dekodujemy
    assert response.data.decode() == expected

def test_get_mode(client, monkeypatch):
    # Ustawienie zmiennej środowiskowej MODE dla testu
    expected_mode = "test"
    monkeypatch.setenv("MODE", expected_mode)
    response = client.get("/get-mode")
    assert response.status_code == 200
    assert response.data.decode() == expected_mode


