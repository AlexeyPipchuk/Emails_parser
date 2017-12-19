import requests
import re
# from BeautifulSoup import BeautifulSoup
url_list = []
e_mails = []
url = 'https://www.mosigra.ru/'
count = 0
def  parsing(pageUrl):
    global url_list
    global count
    global e_mails
    count += 1
    ans = requests.get(pageUrl)
    print(ans)
    result = re.findall('href="(.*?)"', ans.text)
    result2 = re.findall(r"[a-zA-Z0-9_.+]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", ans.text)
    urlsnew = list(set(result))
    mailsnew = list(set(result2))
    for mail in mailsnew:
        e_mails.append(mail)
    if len(urlsnew) > 0:
        for url in urlsnew:
            if url.find('mail') != -1:
                url = url[7:]
                if url not in url_list:
                    url_list.append(url)
            elif len(url) > 0 and url[0] == '#':
                url = 'http://www.mosigra.ru/' + url
                if url not in url_list:
                    url_list.append(url)
            else:
                if url not in url_list:
                    url_list.append(url)
                    if url[:18] == 'http://www.mosigra' and count <= 1 and url.find('mode') == -1:
                        parsing(url)
                        count -= 1
parsing(url)
e_mails = set(e_mails)
file = open("result_1lab.txt", "w")
for i in e_mails:
    file.write(i)
    file.write("\n")
file.close()
