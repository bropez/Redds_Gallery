from bs4 import BeautifulSoup
import requests
import csv

# getting the table from the website to extract from
url = "https://www.thonky.com/animal-crossing-new-leaf/paintings-works-of-art"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
table = soup.find("table", {"class": "table table-bordered"})
data = table.find_all("td")
for td in data:
    print(str(td))
    # print(td.text)

with open("out.csv", "w") as f:
    wr = csv.writer(f)
    for td in data:
        wr.writerow(td)
