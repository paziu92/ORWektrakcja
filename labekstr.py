import requests
from bs4 import BeautifulSoup


url = "http://allegro.pl/listing/listing.php?order=m&string=rower&bmatch=engagement-v6-promo-sm-sqm-dyn-fuzzy-v1-spo-1-5-0118"
r = requests.get(url)

soup = BeautifulSoup(r.content)

#links = soup.find_all("a")

#for link in links:
   #  print "<a href='%s'>%s</a>" %(link.get("href"), link.text)

g_data = soup.find_all("a", {"class": "offer-title"})

for item in g_data:
    print item.contents
    
