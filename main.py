import requests # first library
from bs4 import BeautifulSoup

# the first step is to download a specific data which helps me build a prediction model
years = list(range(1991, 2023))  # build an array where I will put data for each year/season.
print(years)

url_start = "https://www.basketball-reference.com/awards/awards_{}.html" # I use requests library
for year in years:
    url = url_start.format(year)
    data = requests.get(url)  # Use requests.get to retrieve the web page.

    with open("mvp/{}.html".format(year), "w+",  encoding="utf-8") as f:
       f.write(data.text)  # now create directory "mvp" where i put data from webside. i must change code format on utf-8

with open("mvp/1991.html",encoding="utf-8") as f:
    page = f.read()

soup= BeautifulSoup(page,"html.parser")
soup.find('sr', class_= 'over_header').decompose()
mvp_table = soup.find_all(id = 'mvp')
print(mvp_table)