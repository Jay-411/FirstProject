import J_Mysql as db

"""
with db.Database() as dbc:
    dbc.createTables()
    dbc.dropTables()
"""


import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
base_url = "https://www.freeones.com/html/index_prof.shtml?text=1"

# open url
r = requests.get(base_url)

# parse website
doc = BeautifulSoup(r.text,"html.parser")
pstar_liste = []

# save pstar with link in list
for a in doc.select(".BI3col")[0].select("a"):
    pstar_name = a.attrs["title"]
    pstar_link = a.attrs["href"]
    pstar_liste.append([pstar_name,pstar_link])


# loop through pstar_list
for pstar in pstar_liste:
    pstar_url = urljoin(base_url,pstar[1])
    r = requests.get(pstar_url)
    doc = BeautifulSoup(r.text, "html.parser")
    print(pstar[0])
    for part in doc.select(".w3-white div"):
        #print(part.text)
        if part.text.strip() == "Appearance":
            print(part)
            print("\n")
            print(part.next(1))
            #print("\n\n")

    #break;




