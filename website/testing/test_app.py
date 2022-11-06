import unittest
import pytest
import requests
import flask
from website.app import app, create_app


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()

@pytest.fixture()
def test_index_route():
    response = app.test_client().get('/')
    assert response.status_code == 200

def test_login_redirect(client):
    response = client.get("/home")
    assert len(response.history) == 1
    assert response.request.path == "/login"


class myTestCase(unittest.TestCase):

    def testCreateApp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.client = self.app.test_client()

    def testTearDown(self):
        self.app = None

    @pytest.fixture()
    def client(self):
        return app.client()

    def testSignUp(self):
        response = self.client.post('/sign-up', data={
            'first_name': 'Jane',
            'surname': 'Doe',
            'username': 'jdoe',
            'fav_team': 'Arsenal',
            'email': 'jdoe@gmail.com',
            'password1': 'password1',
            'password2': 'password1'
        }, follow_redirects=True)

        assert response.status_code == 200
        assert response.request.path == '/user_home'


if __name__ == '__main__':
    unittest.main()
