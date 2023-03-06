from fastapi.testclient import TestClient
from uuid import UUID
import unittest

from main import app

# unittest.defaultTestLoader.sortTestMethodsUsing = lambda *args: -1

class TestAPI(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = TestClient(app)
        cls.BASE_URL = "/api/v1/notes"
        cls.test_id = ""

    def test_1_empty_list(self):
        self.assertEqual(self.client.get(self.BASE_URL).json(), [])
    
    def test_2_create_item(self):
        url = f"{self.BASE_URL}/create"

        data = {
            "title": "TestTitle",
            "text": "TestText",
            "date_completion": "2020-10-10"
        }

        response = self.client.post(url, json=data)

        self.assertEqual(response.json()["title"], "TestTitle")
        self.assertEqual(response.json()["text"], "TestText")
        self.assertEqual(response.json()["date_completion"], "2020-10-10")
        self.assertEqual(response.json()["is_completed"], False)
    
    def test_3_get_item(self):
        test_id = self.client.get(self.BASE_URL).json()[0]["id"]
        
        url = f"{self.BASE_URL}/{test_id}"

        response = self.client.get(url)

        self.assertEqual(response.json()["title"], "TestTitle")
        self.assertEqual(response.json()["text"], "TestText")
        self.assertEqual(response.json()["id"], test_id)
        self.assertEqual(response.json()["date_completion"], "2020-10-10")
        self.assertEqual(response.json()["is_completed"], False)

    def test_4_make_completed_item(self):
        test_id = self.client.get(self.BASE_URL).json()[0]["id"]

        url = f"{self.BASE_URL}/{test_id}/complete"

        self.client.patch(url)

        response = self.client.get(f"{self.BASE_URL}/{test_id}")
        
        self.assertEqual(response.json()["is_completed"], True)

    def test_5_delete_item(self):
        test_id = self.client.get(self.BASE_URL).json()[0]["id"]

        url = f"{self.BASE_URL}/{test_id}/delete"

        self.client.delete(url)

        response = self.client.get(self.BASE_URL)

        self.assertEqual(response.json(), [])
 

if __name__ == "__main__":
  unittest.main()




