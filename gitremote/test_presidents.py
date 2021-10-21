"""
File: test_presidents.py
Author: Kaleb White
Date modified: 10/20/2021
A program made for testing for all presidents.
"""
# Imports
import pytest
import requests

url_ddg = "https://api.duckduckgo.com"


@pytest.mark.parametrize("presidents", ["Washington", "Adams", "Jefferson", "Madison", "Monroe", "Jackson",
                                        "Buren", "Harrison", "Tyler", "Polk", "Taylor", "Fillmore", "Pierce",
                                        "Buchanan", "Lincoln", "Johnson", "Grant", "Hayes", "Garfield", "Arthur",
                                        "Cleveland", "McKinley", "Roosevelt", "Taft", "Wilson", "Harding", "Coolidge",
                                        "Hoover", "Truman", "Eisenhower", "Kennedy", "Johnson", "Nixon", "Ford",
                                        "Carter", "Reagan", "Bush", "Clinton", "Obama", "Trump", "Biden Jr"])
def test_ddg0(presidents):
    resp = requests.get(url_ddg + "/?q=presidents+of+the+united+states&format=json")
    rsp_data = resp.json()
    rt = rsp_data["RelatedTopics"]
    text = rt[3]
    assert presidents in text
