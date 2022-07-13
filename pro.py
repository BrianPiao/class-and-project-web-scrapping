from bs4 import BeautifulSoup
import requests
import pandas as p

url = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
page = requests.get(url)
soup = BeautifulSoup(page.text,"html.parser")
star_table = soup.find_all("table")
temp = []
tablerows = star_table[7].find_all("tr")
for tr in tablerows:
    td = tr.find_all("td")
    row = [i.text.rstrip() for i in td]
    temp.append(row)
    
Star_names = []
Distance =[]
Mass = []
Radius =[]
for i in range(1,len(temp)):
    Star_names.append(temp[i][0])
    Distance.append(temp[i][5])
    Mass.append(temp[i][7])
    Radius.append(temp[i][8])
    
df = p.DataFrame(list(zip(Star_names,Distance,Mass,Radius,)),columns=['Star_name','Distance','Mass','Radius'])
df.to_csv("star.csv")