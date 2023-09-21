from unittest.mock import Mock
from lib.cat_facts import CatFacts

def test_cat_fact():
    requester = Mock(name="requester")
    response = Mock(name="response")

    requester.get.return_value = response
    response.json.return_value = {"fact": "This is a test fact"}

    cat_fact = CatFacts(requester)
    assert cat_fact.provide() == "Cat fact: This is a test fact"