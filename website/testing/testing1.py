
import unittest
import pytest


from website.app import create_app, app
from website.app import create_database, db



# @pytest.fixture()
# def app():
#     app = create_app()
#     app.config.update({
#         "TESTING": True,
#     })
#
#     yield app
#
#
# @pytest.fixture()
# def client(app):
#     return app.test_client()



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



