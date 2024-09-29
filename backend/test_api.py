import unittest
from main import create_app
from config import TestConfig
from exts import db

class APITestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()
            
    def test_signup(self):
        signup_response = self.client.post(
            '/auth/signup',
            json={
                "username": "testuser",
                "email": "testuser@test.com",
                "password": "password"
            }
        )
        self.assertEqual(signup_response.status_code, 201)
        
    def test_login(self):
         signup_response = self.client.post(
            '/auth/signup',
            json={
                "username": "testuser",
                "email": "testuser@test.com",
                "password": "password"
            }
        )
         
         login_response = self.client.post(
             '/auth/login',
             json={
                "username": "testuser",
                "password": "password"
             }
         )
         
         self.assertEqual(login_response.status_code, 200)
         
    def test_get_all_recipes(self):
        """Test untuk mendapatkan semua resep"""
        response = self.client.get('/recipe/recipes')
        self.assertEqual(response.status_code, 200)
    
    def test_get_one_recipe(self):
        id = 1
        response = self.client.get(f'/recipe/recipes/{id}')
        self.assertEqual(response.status_code, 404)
    
    def test_create_recipe(self):
         signup_response = self.client.post(
            '/auth/signup',
            json={
                "username": "testuser",
                "email": "testuser@test.com",
                "password": "password"
            }
        )
         
         login_response = self.client.post(
             '/auth/login',
             json={
                "username": "testuser",
                "password": "password"
             }
         )
         
         access_token = login_response.json["access_token"]
         
         create_recipe_response = self.client.post(
             '/recipe/recipes',
             json={
                 "title": "test cookie",
                 "description": "test description"
             },
             headers={
                 "Authorization": f"Bearer {access_token}"
             }
         )
         
         self.assertEqual(create_recipe_response.status_code, 201)
    
    def test_update_recipe(self):
        pass
    
    def test_delete_recipe(self):
        pass

    def test_hello_world(self):
        hello_response = self.client.get('/recipe/hello')
        json = hello_response.json
        self.assertEqual(json, {"message": "Hello World"})

if __name__ == "__main__":
    unittest.main()
