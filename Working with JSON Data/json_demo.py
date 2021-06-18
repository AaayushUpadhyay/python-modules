import json

# loading json file into python object
with open('states.json') as f:
	data=json.load(f)

for state in data['states']:
	# print(state['name'],state['abbreviation'])
	del(state['area_codes'])

# writing json data into a new file
with open('new_states.json','w') as f:
	json.dump(data,f,indent=2)