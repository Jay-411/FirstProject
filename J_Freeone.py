
import requests
import re
from urllib.parse import urljoin
from bs4 import BeautifulSoup
base_url = "https://www.freeones.com/html/index_prof.shtml?text=1"


# open url
r = requests.get(base_url)
# parse website
doc = BeautifulSoup(r.text,"html.parser")
pstar_liste = []

for col in doc.select(".BI3col"):
    for link in col.select(".textlink"):
        if not link.select("a")[2].text[0].isdigit():
            pstar_name = link.select("a")[2].text
            pstar_link = link.select("a")[2].attrs["href"].lstrip("/")
            pstar_liste.append([pstar_name, pstar_link])


pstar_liste = []
pstar_liste.append(["A.J. Cook","www.freeones.com/html/a_links/A.J._Cook/"])
for pstar_name, pstar_link in pstar_liste:
    pstar_link = "https://" + pstar_link
    r = requests.get(pstar_link)
    doc = BeautifulSoup(r.text,"html.parser")
    if doc.select_one("#MenuBarBiography") != None:
        pstar_link = "https://" + doc.select_one("#MenuBarBiography").select_one("a").attrs["href"].lstrip("/")
        r = requests.get(pstar_link)
        doc = BeautifulSoup(r.text,"html.parser")
        bio = {}
        for row in doc.select(".paramname"):
            param = row.text.strip().strip(":")
            if param == "Height":
                value = row.parent.select_one(".paramvalue").text.strip()
                value = re.search('.*([0-9]{3}) cm.*', value).group(1)
            elif param == "Weight":
                value = row.parent.select_one(".paramvalue").text.strip()
                value = re.search('.*\'([0-9][0-9]|[0-9][0-9][0-9]) kg.*', value).group(1)
            elif param == "Career Start And End":
                value = row.parent.select_one(".paramvalue").text.strip()
                value = re.search(r'(.*)', value).group(1)
            elif param == "Shoe Size":
                value = row.parent.select_one(".paramvalue").text.strip()
                value = re.search(r"\'([0-9]|[0-9].*)\'", value).group(1)
            elif param == "Fan Club Address":
                continue
            elif param == "Social Network Links":
                continue
            elif param == "Babe Rank on Freeones":
                continue
            else:
                value = row.parent.select_one(".paramvalue").text.strip()
            bio[param] = value
        print(bio)
    else:
        print("\n\n keine bio für " + pstar_name + "\n\n")