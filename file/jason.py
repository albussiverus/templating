import json

data = [{'my': "yours", 'two': (1,2,3,4,5)}]

data_formated = json.dumps(data)

print(data_formated)


with open("dump.json", mode='w') as fid:
    json.dump(data_formated, fid)

with open("dump.json", mode='r') as fid:
    txt = json.load(fid)

print(txt)
