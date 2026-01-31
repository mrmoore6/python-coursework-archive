"""
Author: Michael Moore
Date: 10/25/20
This program scrapes url for data and returns it in a pretty form.
"""

import requests, bs4
url = 'https://www.dmacc.edu/programs/Pages/welcome.aspx'
response = requests.get(url)
html = response.content
f = open("request_result.txt","w+")
f.writelines(str(html))
soup = bs4.BeautifulSoup(open("request_result.txt"), 'html.parser')
print(soup.prettify())

