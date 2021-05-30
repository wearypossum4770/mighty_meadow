import pytest
from django.core.cache import cache


def test_memcache():
    cache.get("foo")
    cache.set("foo", "bar")
    assert cache.get("foo") == 'bar'