from bs4 import BeautifulSoup
  
# Opening the html file
HTMLFile = open("HTML/710.html", "r", encoding="UTF 8")
  
# Reading the file
index = HTMLFile.read()
  
# Creating a BeautifulSoup object and specifying the parser
soup = BeautifulSoup(index, 'lxml')

content=soup.findAll('div', class_='col-lg-12')

def delite_a(content):
    try:
        for i in content[0].select('p',class_='rvps526'):
            try:
                if i.a.get_text()!='':
                    text=i.a.get_text()
                    i.a.unwrap()
            except:
                continue
        for i in content[0].select('a'):
            i['href']='#'
    except:    
        print(content[0].select('a'))
        for i in content[0].select('a'):
            i['href']='#'
    
    # print(content[0])

def replace_image(content):
    for i in content[0].select('img'):
        name=i['src'][-13:]
        i['style']="vertical-align: middle;"
        i['src']="{% static 'project/images/"+name+"' %}"
        try:
            del i['width']
            del i['height']
        except:
            continue
        # print(i)
        # print(name)
    # print(content)
            

delite_a(content)
replace_image(content)
print(content[0])
# print(content)