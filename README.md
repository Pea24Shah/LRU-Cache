# LRU Cache in Python

A Least Recently Used (LRU) cache with O(1) `get` and `put`, built from a hash map and a doubly linked list.

## Approach

- A **dict** maps each key to its node in a linked list, so lookups are O(1).
- A **doubly linked list** keeps entries in order of use: the most recently used is at the front, the least recently used at the back. Because each node knows its `prev` and `next`, any node can be unlinked in O(1).
- Two dummy nodes (`head` and `tail`) remove the special cases for an empty list.
- `get(key)` moves the node to the front and returns its value, or `-1` if the key is missing.
- `put(key, value)` updates an existing key and moves it to the front, or adds a new node at the front. If the cache is over capacity, the node just before `tail` (the least recently used) is removed from both the list and the dict.

## Complexity

| Operation | Time | Space |
|-----------|------|-------|
| `get`     | O(1) | |
| `put`     | O(1) | |
| Overall   |      | O(capacity) |

## Usage

    from lru_cache import LRUCache

    cache = LRUCache(2)
    cache.put(1, "A")
    cache.put(2, "B")
    cache.get(1)       # "A" (1 is now the most recent)
    cache.put(3, "C")  # evicts 2, the least recently used
    cache.get(2)       # -1

## Running the tests

    pip install pytest
    pytest

The tests cover basic get/put, LRU eviction, updating an existing key, and capacity 1.
