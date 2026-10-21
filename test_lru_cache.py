import pytest

from lru_cache import LRUCache


def test_get_missing_key_returns_minus_one():
    cache = LRUCache(2)
    assert cache.get(42) == -1


def test_put_then_get():
    cache = LRUCache(2)
    cache.put(1, "A")
    assert cache.get(1) == "A"


def test_evicts_least_recently_used():
    cache = LRUCache(2)
    cache.put(1, "A")
    cache.put(2, "B")
    cache.put(3, "C")  # 1 is the oldest, so it goes
    assert cache.get(1) == -1
    assert cache.get(2) == "B"
    assert cache.get(3) == "C"


def test_get_marks_key_as_recently_used():
    cache = LRUCache(2)
    cache.put(1, "A")
    cache.put(2, "B")
    cache.get(1)       # now 2 is the least recent
    cache.put(3, "C")
    assert cache.get(2) == -1
    assert cache.get(1) == "A"


def test_update_existing_key_changes_value():
    cache = LRUCache(2)
    cache.put(1, "A")
    cache.put(1, "Z")
    assert cache.get(1) == "Z"


def test_update_existing_key_does_not_grow_cache():
    cache = LRUCache(2)
    cache.put(1, "A")
    cache.put(2, "B")
    cache.put(1, "Z")  # update, not a new item, so nothing is evicted
    assert cache.get(1) == "Z"
    assert cache.get(2) == "B"


def test_update_existing_key_marks_it_recently_used():
    cache = LRUCache(2)
    cache.put(1, "A")
    cache.put(2, "B")
    cache.put(1, "Z")  # now 2 is the least recent
    cache.put(3, "C")
    assert cache.get(2) == -1
    assert cache.get(1) == "Z"


def test_capacity_one():
    cache = LRUCache(1)
    cache.put(1, "A")
    assert cache.get(1) == "A"
    cache.put(2, "B")  # evicts 1
    assert cache.get(1) == -1
    assert cache.get(2) == "B"


def test_capacity_one_update_same_key():
    cache = LRUCache(1)
    cache.put(1, "A")
    cache.put(1, "B")
    assert cache.get(1) == "B"


def test_invalid_capacity_raises():
    with pytest.raises(ValueError):
        LRUCache(0)
