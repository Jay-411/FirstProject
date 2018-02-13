from datetime import datetime
from multiprocessing import Pool
import requests
import re
from urllib.parse import urljoin
from bs4 import BeautifulSoup

y = 0

def scrape_links(pstar_link):
    # for pstar_link in pstar_list:
    #print(pstar_link)
    pstar_link = "https://" + pstar_link
    r = requests.get(pstar_link)
    doc = BeautifulSoup(r.text, "html.parser")
    if doc.select_one("#MenuBarBiography") != None:
        pstar_link = "https://" + doc.select_one("#MenuBarBiography").select_one("a").attrs["href"].lstrip("/")
        r = requests.get(pstar_link)
        doc = BeautifulSoup(r.text, "html.parser")
        bio = {}
        for row in doc.select(".paramname"):
            param = row.text.strip().strip(":")
            if param == "Height":
                value = row.parent.select_one(".paramvalue").text.strip()
                if re.search('.*([0-9]{3}) cm.*', value) != None:
                    value = re.search('.*([0-9]{3}) cm.*', value).group(1)
            elif param == "Weight":
                value = row.parent.select_one(".paramvalue").text.strip()
                if re.search('.*\'([0-9][0-9]|[0-9][0-9][0-9]) kg.*', value) != None:
                    value = re.search('.*\'([0-9][0-9]|[0-9][0-9][0-9]) kg.*', value).group(1)
            elif param == "Career Start And End":
                value = row.parent.select_one(".paramvalue").text.strip()
                if re.search(r'(.*)', value) != None:
                    value = re.search(r'(.*)', value).group(1)
            elif param == "Shoe Size":
                value = row.parent.select_one(".paramvalue").text.strip()
                if re.search(r"\'([0-9]|[0-9].*)\'", value) != None:
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


def funktion(testtext):
    print(testtext)


base_url = "https://www.freeones.com/html/index_prof.shtml?text=1"

# open url
r = requests.get(base_url)
# parse website
doc = BeautifulSoup(r.text, "html.parser")
pstar_list = []

x = 0
x_max = 200
# website has 3 columns with links as content
for col in doc.select(".BI3col"):
    # select the links inside a column
    for link in col.select(".textlink"):
        # only save links that are names which means is does not begin with a digit
        if not link.select("a")[2].text[0].isdigit():
            pstar_name = link.select("a")[2].text
            pstar_link = link.select("a")[2].attrs["href"].lstrip("/")
            pstar_list.append(pstar_link)
            x += 1
        if x >= x_max:
            break;

#print(pstar_list)
#print("\n\n")

# link list for testing
# pstar_list = []
# pstar_list.append(["A.J. Cook","www.freeones.com/html/a_links/A.J._Cook/"])

start_time = datetime.now()
# scrape_links(pstar_list)

testliste = ["eins", "zwei", "drei"]


if __name__ == '__main__':
    p = Pool(20)
    p.map(scrape_links,pstar_list)
    #p.map(funktion, testliste)
    p.terminate()
    p.join()

end_time = datetime.now()
duration = end_time - start_time
print("%d.%06d" % (duration.seconds, duration.microseconds))

