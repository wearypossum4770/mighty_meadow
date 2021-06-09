from unittest import TestCase
import asyncio
from django.conf import settings
import aiohttp
import pytest
from django.core.cache import cache

from mighty_meadow.mighty_meadow_requests import requests
from users.views import registration
request_object = {}
def test_memcache_functionality():
    cache.get("foo")
    cache.set("foo", "bar")
    assert cache.get("foo") == "bar"
    assert True == True
 
class TestSiteOperation(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.response = requests()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()

    def test_homepage_page_connection(self):
        assert self.response.get("/") == 200

    def test_about_page_connection(self):
        assert self.response.get("/about/") == 200

    def test_registration_page_connection(self):
        assert self.response.get("/register/") == 200

    def test_password_reset_page_connection(self):
        assert self.response.get("/password-reset/") == 200

    def test_new_user_registration(self):
        assert self.response.get('http://127.0.0.1:8000/register/') == ""

# requests = ['test_new_user_registration']
# async def main():
#     async with aiohttp.ClientSession() as session:
#         for request in requests:
#             async with session.post(**request) as usePost:
#                 request_object[request.get('url')] = usePost.status
#                 print(usePost)

# # http://127.0.0.1:8000/register/


# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())