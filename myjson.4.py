import json
data ='''[
{"name" :"zino",
"id" :"09",
"x" :"12"
},
{"name" : "zine",
"id" : "05",
"x" : "4"}
]'''

info = json.loads(data)
for item in info:
    print("the name is  ",item["name"])