import requests
from bs4 import BeautifulSoup

site="http://www.dictionary.com/browse/"
    
for i in range(5):
    word=str(raw_input("WORD:"))
    data=requests.get(site+word)
    print word.upper().center(180,'-')
    print "\n"
    soup= BeautifulSoup(data.content,"lxml")
    data00=(soup.find_all('div',{'class':"def-content"}))

    for i in range (2):
        print i+1,":",data00[i].text
        print "\n"
    print "END OF DEFINITION".center(180,'-')

print "GOOD DAY".center(180,'-')
