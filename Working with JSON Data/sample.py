# "JSON : Javascipt Object Notation"

import json



#  this is a python string that happens to be a valid json
people_string = '''
{
	"people": [
	{
	"name": "John Smith",
	"phone": "615-555-7164",
	"emails": ["johnsmith@bogusemail.com","john.smith@work-place.com"],
	"has_license": false 
	},
	{
	"name": "Jane Doe",
	"phone": "560-555-5153",
	"emails": null,
	"has_license": true
	}
	]
}
'''

# loading python string into a object
data=json.loads(people_string)


# .loads is used to load python string(that happens to be a valid json) into object

# print(type(data))
# print(data)

for people in data['people']:
	# print(people)
	pass

# modifying json and dumping it back into a string
# we are removing phone
for people in data['people']:
	del(people['phone'])

# new_data=json.dumps(data)
# formatting json
# if we want indentation
# new_data=json.dumps(data,indent=2)
# if we want keys to be sorted alphbetically
new_data=json.dumps(data,indent=2,sort_keys=True)
print(new_data)