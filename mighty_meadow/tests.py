from unittest import TestCase

import pytest
from django.core.cache import cache

from mighty_meadow.mighty_meadow_requests import requests


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
