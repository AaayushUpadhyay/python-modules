from bs4 import BeautifulSoup
import requests

# with open('simple.html')as html_file:
#     soup=BeautifulSoup(html_file,'lxml')

# print(soup) #we get unindented html
# print(soup.prettify())

# to get a tag

# print(soup.title) # agar kai saare titles hai toh yeh sirf pehla title dega
# print(soup.title.text)

# kisi ek particular class ya id ke element ko lene ke liye
# print(soup.find('div',class_='footer'))

# .find footer class ka sabse pehla div lake dega
# footer class ke saare divs lane ke liye we will use find_all

# articles = soup.find_all('div',class_="article")
# # python mei class ek keyword hota hai isliye we write class_ , id ke liye simple id likhenge
# for article in articles:
#     title=article.h2.a.text
#     summary=article.p.text
#     print(title)
#     print(summary)
#     print()


source=requests.get('https://coreyms.com/').text
soup=BeautifulSoup(source,'lxml')

articles=soup.find_all('article')
# print(articles)

for article in articles:
    title=article.header.h2.a.text
    summary=article.div.p.text
    print(title)
    print(summary)
    print()
    try:
        vid_src = article.find('iframe', class_='youtube-player')['src']

        vid_id = vid_src.split('/')[4]
        vid_id = vid_id.split('?')[0]

        yt_link = f'https://youtube.com/watch?v={vid_id}'
    except Exception as e:
        yt_link = None

    print(yt_link)
