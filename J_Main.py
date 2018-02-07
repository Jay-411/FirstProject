import J_Mysql as db

"""
with db.Database() as dbc:
    dbc.createTables()
    dbc.dropTables()
"""


import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
anzErg = "2"
base_url = "http://www.adultfilmdatabase.com/browse.cfm?type=actor&page=1&dsp=" + anzErg + "&sb=name&gf=&if=&dspas=list"

# open url
r = requests.get(base_url)

# parse website
doc = BeautifulSoup(r.text,"html.parser")
pstar_liste = []

# save pstar with link in list
for a in doc.select(".w3-table")[0].select("a"):
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




