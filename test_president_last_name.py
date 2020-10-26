import requests
import pytest

response = requests.get("https://api.duckduckgo.com/?q=presidents of the united states,&format=json")
response_data = response.json()

for i in range(44):
    if "Bibliography" in response_data["RelatedTopics"][i]["Text"]:
        del response_data["RelatedTopics"][i]

    if "Lifespan" in response_data["RelatedTopics"][i]["Text"]:
        del response_data["RelatedTopics"][i]

    if "Lifespan" in response_data["RelatedTopics"][i]["Text"]:
        del response_data["RelatedTopics"][i]

    if "Mesonoemacheilus menoni" in response_data["RelatedTopics"][i]["Text"]:
        del response_data["RelatedTopics"][i]

    if "Historical rankings" in response_data["RelatedTopics"][i]["Text"]:
        del response_data["RelatedTopics"][i]

    if "head of state and head of government" in response_data["RelatedTopics"][i]["Text"]:
        del response_data["RelatedTopics"][i]

    if "Sid Sriram" in response_data["RelatedTopics"][i]["Text"]:
        del response_data["RelatedTopics"][i]
    if "Frederick Manton" in response_data["RelatedTopics"][i]["Text"]:
        del response_data["RelatedTopics"][i]

def test_president_Lincoln():
    assert "Lincoln" in response_data["RelatedTopics"][0]["Text"]
def test_president_Jackson():
    assert "Jackson" in response_data["RelatedTopics"][1]["Text"]
def test_president_Johnson0():
    assert "Johnson" in response_data["RelatedTopics"][2]["Text"]
def test_president_Obama():
    assert "Obama" in response_data["RelatedTopics"][3]["Text"]
def test_president_Harrison0():
    assert "Harrison" in response_data["RelatedTopics"][4]["Text"]
def test_president_Clinton():
    assert "Clinton" in response_data["RelatedTopics"][5]["Text"]
def test_president_Coolidge():
    assert "Coolidge" in response_data["RelatedTopics"][6]["Text"]
def test_president_Arthur():
    assert "Arthur" in response_data["RelatedTopics"][7]["Text"]
def test_president_Trump():
    assert "Trump" in response_data["RelatedTopics"][8]["Text"]
def test_president_Eisenhower():
    assert "Eisenhower" in response_data["RelatedTopics"][9]["Text"]
def test_president_Roosevelt0():
    assert "Roosevelt" in response_data["RelatedTopics"][10]["Text"]
def test_president_Pierce():
    assert "Pierce" in response_data["RelatedTopics"][11]["Text"]
def test_president_Bush0():
    assert "Bush" in response_data["RelatedTopics"][12]["Text"]
def test_president_Washington():
    assert "Washington" in response_data["RelatedTopics"][13]["Text"]
def test_president_Bush1():
    assert "Bush" in response_data["RelatedTopics"][14]["Text"]
def test_president_Ford():
    assert "Ford" in response_data["RelatedTopics"][15]["Text"]
def test_president_Cleveland():
    assert "Cleveland" in response_data["RelatedTopics"][16]["Text"]
def test_president_Truman():
    assert "Truman" in response_data["RelatedTopics"][17]["Text"]
def test_president_Hoover():
    assert "Hoover" in response_data["RelatedTopics"][18]["Text"]
def test_president_Garfield():
    assert "Garfield" in response_data["RelatedTopics"][19]["Text"]
def test_president_Buchanan():
    assert "Buchanan" in response_data["RelatedTopics"][20]["Text"]
def test_president_Polk():
    assert "Polk" in response_data["RelatedTopics"][21]["Text"]
def test_president_Madison():
    assert "Madison" in response_data["RelatedTopics"][22]["Text"]
def test_president_Monroe():
    assert "Monroe" in response_data["RelatedTopics"][23]["Text"]
def test_president_Carter():
    assert "Carter" in response_data["RelatedTopics"][24]["Text"]
def test_president_Adams0():
    assert "Adams" in response_data["RelatedTopics"][25]["Text"]
def test_president_Kennedy():
    assert "Kennedy" in response_data["RelatedTopics"][26]["Text"]
def test_president_Adams1():
    assert "Adams" in response_data["RelatedTopics"][27]["Text"]
def test_president_Tyler():
    assert "Tyler" in response_data["RelatedTopics"][28]["Text"]
def test_president_Johnson1():
    assert "Johnson" in response_data["RelatedTopics"][29]["Text"]
def test_president_Buren():
    assert "Buren" in response_data["RelatedTopics"][30]["Text"]
def test_president_Fillmore():
    assert "Fillmore" in response_data["RelatedTopics"][31]["Text"]
def test_president_Nixon():
    assert "Nixon" in response_data["RelatedTopics"][32]["Text"]
def test_president_Reagan():
    assert "Reagan" in response_data["RelatedTopics"][33]["Text"]
def test_president_Hayes():
    assert "Hayes" in response_data["RelatedTopics"][34]["Text"]
def test_president_Roosevelt1():
    assert "Roosevelt" in response_data["RelatedTopics"][35]["Text"]
def test_president_Jefferson():
    assert "Jefferson" in response_data["RelatedTopics"][36]["Text"]
def test_president_Grant():
    assert "Grant" in response_data["RelatedTopics"][37]["Text"]
def test_president_Harding():
    assert "Harding" in response_data["RelatedTopics"][38]["Text"]
def test_president_Harrison1():
    assert "Harrison" in response_data["RelatedTopics"][39]["Text"]
def test_president_Taft():
    assert "Taft" in response_data["RelatedTopics"][40]["Text"]
def test_president_Mckinley():
    assert "McKinley" in response_data["RelatedTopics"][41]["Text"]
def test_president_Wilson():
    assert "Wilson" in response_data["RelatedTopics"][42]["Text"]
def test_president_Taylor():
    assert "Taylor" in response_data["RelatedTopics"][43]["Text"]
