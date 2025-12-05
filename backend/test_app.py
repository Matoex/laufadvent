import unittest
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import app
from database import init_db, get_db

class TestButtonGridAPI(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()
        app.config['TESTING'] = True
        
        test_db_path = os.path.join(os.path.dirname(__file__), 'instance', 'test_database.db')
        if os.path.exists(test_db_path):
            os.remove(test_db_path)
        
        init_db()
    
    def test_create_new_user(self):
        response = self.app.get('/api/testuser')
        self.assertEqual(response.status_code, 200)
        
        data = json.loads(response.data)
        self.assertEqual(data['username'], 'testuser')
        
        for i in range(1, 25):
            self.assertIn(str(i), data['button_states'])
            self.assertFalse(data['button_states'][str(i)])
    
    def test_get_existing_user(self):
        self.app.get('/api/existinguser')
        
        response = self.app.get('/api/existinguser')
        self.assertEqual(response.status_code, 200)
        
        data = json.loads(response.data)
        self.assertEqual(data['username'], 'existinguser')
    
    def test_update_button_state(self):
        self.app.get('/api/updatetest')
        
        response = self.app.post('/api/updatetest', 
                               data=json.dumps({'button_number': 5, 'is_on': True}),
                               content_type='application/json')
        self.assertEqual(response.status_code, 200)
        
        response = self.app.get('/api/updatetest')
        data = json.loads(response.data)
        self.assertTrue(data['button_states']['5'])
    
    def test_update_invalid_button(self):
        response = self.app.post('/api/testuser',
                               data=json.dumps({'button_number': 25, 'is_on': True}),
                               content_type='application/json')
        self.assertEqual(response.status_code, 200)
    
    def test_missing_data(self):
        response = self.app.post('/api/testuser',
                               data=json.dumps({}),
                               content_type='application/json')
        self.assertEqual(response.status_code, 400)
    
    def test_no_json_data(self):
        response = self.app.post('/api/testuser')
        self.assertEqual(response.status_code, 415)
    
    def test_overview_endpoint(self):
        self.app.get('/api/user1')
        self.app.get('/api/user2')
        
        response = self.app.get('/api/overview')
        self.assertEqual(response.status_code, 200)
        
        data = json.loads(response.data)
        self.assertIn('user1', data)
        self.assertIn('user2', data)
        self.assertIn('completed_days', data['user1'])
        self.assertIn('kilometers', data['user1'])

def tearDown(self):
        # Clear test data but keep real user data
        conn = get_db()
        cursor = conn.cursor()
        test_users = ['testuser', 'existinguser', 'updatetest', 'newtest']
        for user in test_users:
            cursor.execute('DELETE FROM button_states WHERE username = ?', (user,))
            cursor.execute('DELETE FROM users WHERE username = ?', (user,))
        conn.commit()
        conn.close()

if __name__ == '__main__':
    unittest.main()