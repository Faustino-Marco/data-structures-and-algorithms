import pytest
from data_structures.hashtable import Hashtable


def test_exists():
    assert Hashtable

def test_get_returns_none_for_missing_key():
    hashtable = Hashtable()
    actual = hashtable.get("spam")
    expected = None
    assert actual == expected

def test_buckets_size():
    table = Hashtable()
    actual = len(table.buckets)
    expected = 1024
    assert actual == expected
    
def test_hash_in_range():
    table = Hashtable(size=2)
    keys = ["spam", "eggs", "bacon", "toast"]
    for key in keys:
        index = table.hash(key)
        assert 0 <= index < table.size

def test_set_does_not_blow_up():
    table = Hashtable()
    table.set("eggs", "bacon")
    assert True

def test_keys():
    table = Hashtable()
    table.set("eggs", "bacon")
    table.set("ping", "pong")
    keys = table.keys()
    actual = keys
    expected = ["eggs", "bacon"]
    assert actual == expected 
    
@pytest.mark.skip("TODO")
def test_buckets_size():
    table = Hashtable()

@pytest.mark.skip("TODO")
def test_get_apple():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    actual = hashtable.get("apple")
    expected = "Used for apple sauce"
    assert actual == expected


@pytest.mark.skip("TODO")
def test_internals():
    hashtable = Hashtable(1024)
    hashtable.set("ahmad", 30)
    hashtable.set("silent", True)
    hashtable.set("listen", "to me")

    actual = []

    # NOTE: purposely breaking encapsulation to test the "internals" of Hashmap
    for item in hashtable._buckets:
        if item:
            actual.append(item.display())

    expected = [[["silent", True], ["listen", "to me"]], [["ahmad", 30]]]

    assert actual == expected
