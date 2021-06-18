import json
from urllib.request import urlopen

with urlopen("https://api.github.com/users") as response:
    source = response.read()

data=json.loads(source)

# print(json.dumps(data,indent=2))
# print(type(data))

for user in data:
	print(user['login'],user['id'])
	print()

