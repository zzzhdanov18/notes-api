from fastapi.testclient import TestClient
from uuid import UUID
import unittest

from main import app

# unittest.defaultTestLoader.sortTestMethodsUsing = lambda *args: -1

class TestAPI(unittest.TestCase):

    BASE_URL = "/api/v1/notes"
    test_id: str = ""

    def setUp(self):
        self.client = TestClient(app)

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

        self.test_id = response.json()["id"]

        self.assertEqual(response.json()["title"], "TestTitle")
        self.assertEqual(response.json()["text"], "TestText")
        self.assertEqual(response.json()["date_completion"], "2020-10-10")
    
    def test_3_get_item(self):
        url = f"{self.BASE_URL}/{self.test_id}"

        response = self.client.get(url)

        self.assertEqual(response.json()["title"], "TestTitle")
        self.assertEqual(response.json()["text"], "TestText")
        self.assertEqual(response.json()["id"], self.test_id)
        self.assertEqual(response.json()["date_completion"], "2020-10-10")
        self.assertEqual(response.json()["is_completed"], False)

    def test_4_make_completed_item(self):
        url = f"{self.BASE_URL}/{self.test_id}/complete"

        self.client.patch(url)

        response = self.client.get(f"{self.BASE_URL}/{self.test_id}")
        
        self.assertEqual(response.json()["is_completed"], True)

    def test_5_delete_item(self):
        url = f"{self.BASE_URL}/{self.test_id}/delete"

        self.client.delete(url)

        response = self.client.get(self.BASE_URL)

        self.assertEqual(response.json(), [])
        print(self.test_id, "TESTIDINF")
 

if __name__ == "__main__":
  unittest.main()
