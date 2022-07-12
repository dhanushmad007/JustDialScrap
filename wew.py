from csv import writer
import urllib.request
from bs4 import BeautifulSoup

class JustDail:
    def __init__(self):
        self.filename="ENTER YOUR FILE >CSV"
        with open(self.filename, 'w', encoding='utf8', newline='') as f:
            thewriter = writer(f)
            header = ['Name', 'Phone Number', 'Address']
            thewriter.writerow(header)
            self.name, self.address, self.phone = [], [], []
    def PhoneNumDecode(self,x):
        t = (str(x[-1].text).split('.icon-'))
        count = 0
        dic = {}
        for i in t[1:]:
            dic[i[:3]] = str(count)
            count += 1
        return dic
    def PhoneNum(self,dic,i):
        content = i.find('p', class_='contact-info')
        try:
            numberTags = (content.find('a'))
            number = []
            if "+(" in numberTags:
                list = (numberTags.find_all('span'))
                count = 0
                number.append(" +(")
                for i in range(len(list)):
                    count += 1
                    if count == 3:
                        number.append(')-')
                    number.append(dic[list[i].get('class')[1].split('-')[1]])
                self.phone.append(''.join(number))
            else:
                list = (numberTags.find_all('span'))
                for i in range(len(list)):
                    number.append(dic[list[i].get('class')[1].split('-')[1]])
                self.phone.append(''.join(number))
        except:
            self.phone.append("")
    def Name(self,i):
        return self.name.append(i.find('img').get('alt').split(' in ')[0])
    def Address(self,i):
        self.address.append(i.find('span', class_='cont_fl_addr').text)
    def Scrap(self,id_no,url):
        req = urllib.request.Request(f'{url}-{id_no}',
                                     headers={'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64)"})
        page = urllib.request.urlopen(req)
        soup = BeautifulSoup(page.read(), "html.parser")
        x = soup.find_all('style', type='text/css')
        dic=self.PhoneNumDecode(x)
        v = soup.find_all('li', class_='cntanr')

        for i in v:
            (self.PhoneNum(dic,i))
            (self.Address(i))
            (self.Name(i))
        for i in range(len(self.name)):
            print(self.name[i],self.address[i],self.phone[i])
    def convertToCSV(self):
        for i in range(len(self.name)):
            with open(self.filename, 'a', encoding='utf8', newline='') as f:
                thewriter = writer(f)
                row = (self.name[i],self.phone[i],self.address[i])
                thewriter.writerow(row)
obj = JustDail()
url =" YOUR URL "
firstPage= #Enter your First Page number
lastPage= #Enter your Last Page number
for i in range(firstPage,lastPage):
    obj.Scrap(i,url)
obj.convertToCSV()