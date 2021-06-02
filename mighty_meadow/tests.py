import pytest
from django.core.cache import cache


def test_memcache_functionality():
    cache.get("foo")
    cache.set("foo", "bar")
    assert cache.get("foo") == "bar"
    assert True == True
