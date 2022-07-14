from bs4 import BeautifulSoup
import bs4 as soup
import requests as req
import sys,lxml

HTMLFile = open("HTML/220.html", "r", encoding='utf-8')

index = HTMLFile.read()
  
# Creating a BeautifulSoup object and specifying the parser
soup = BeautifulSoup(index, 'lxml')
  
# Using the select-one method to find the second element from the li tag
content=soup.findAll('div',class_='col-lg-12')
for i in content[0].findAll('p',class_='rvps526'):
    print(i.unwrap())
print(content[0].a.decompose())
print(content)