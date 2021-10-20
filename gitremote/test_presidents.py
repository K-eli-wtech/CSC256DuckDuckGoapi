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


@pytest.mark.parametrize("presidents", ["George Washington", "John Adams", "Thomas Jefferson", "James Madison",
                                        "James Monroe", "John Quincy Adams", "Andrew Jackson", "Martin van Buren",
                                        "William Henry Harrison", "John Tyler", "James Polk", "Zachary Taylor",
                                        "Millard Fillmore", "Franklin Pierce", "James Buchanan", "Abraham Lincoln",
                                        "Andrew Johnson", "Ulysses S. Grant", "Rutherford B. Hayes", "James Abram Garfield",
                                        "Chester Alan Arthur", "Grover Cleveland", "Benjamin Harrison", "Grover Cleveland",
                                        "William McKinley", "Theodore Roosevelt", "William Howard Taft", "Woodrow (Thomas) Wilson",
                                        "Warren Gamaliel Harding", "Calvin (John) Coolidge", "Herbert Clark Hoover", "Franklin Delano Roosevelt",
                                        "Harry S. Truman", "Dwight (David) Eisenhower", "John Fitzgerald Kennedy", "Lyndon Baines Johnson",
                                        "Richard Milhouse Nixon", "Gerald Rudolph Ford", "Jimmy Carter", "Ronald Wilson Reagan",
                                        "George Herbert Walker Bush", "William (Bill) Jefferson Clinton", "George Walker Bush", "Barack Hussein Obama",
                                        "Donald Trump", "Joseph Robinette Biden Jr"])
def test_ddg0(presidents):
    resp = requests.get(url_ddg + "/?q=presidents of the united states, " + presidents + "&format=json")
    rsp_data = resp.json()
    assert "DuckDuckGo" in rsp_data["Heading"]
