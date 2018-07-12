from bs4 import BeautifulSoup
import requests
import csv

# # getting the table from the website to extract from
url = "https://www.thonky.com/animal-crossing-new-leaf/paintings-works-of-art"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
[s.extract() for s in soup('em')]
table = soup.find("table", {"class": "table table-bordered"})
# table_row = table.find_all("tr")
# table_data = table.find_all("td")
print(table)
for tr in table:
    for td in tr:
            print(td.text)

# with open("out.csv", "w") as f:
#     wr = csv.writer(f)
#     for tr in table:
#         for td in tr:
#             wr.writerow(td)


# with open("out.csv", "w") as f:
#     wr = csv.writer(f)
#     for td in data:
#         wr.writerow(td)
