import requests

# requesting a web page
# r=requests.get('https://docs.python-requests.org/en/master/')
# print(r) 
# we get a response object <Response [200]>

# if you want to know the functions of an object use dir(object) or help(object)

# to get response in form of text
# print(r.text)

# to get response in form of bytes (used when downloading images,videos,etc)

# Downloading an image
# r=requests.get('http://imgs.xkcd.com/comics/python.png')
# with open('pic.png','wb') as f:
# 	f.write(r.content)

# to get all the headers from the response
# r=requests.get('http://imgs.xkcd.com/comics/python.png')
# print(r.headers)

# sending get request
# payload={'count':2,'page':25}
# r=requests.get('http://httpbin.org/get',params=payload)
# print(r.text) json response on sending a get request
# print(r.url)
# http://httpbin.org/get?count=2&page=25

# Downloading an image
r=requests.get('http://imgs.xkcd.com/comics/python.png')
with open('pic.png','wb') as f:
	f.write(r.content)