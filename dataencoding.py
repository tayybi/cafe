import csv
import json

# reading and writing in CSV

#read csv file 
# with open("ford_escort.csv","r") as readerfile:
#     content = csv.reader(readerfile,delimiter=",")
#     for row in content:
#         print(row)

#write csv file
# with open("newfile.csv","w") as writerfile:
#     writer = csv.writer(writerfile,delimiter=",")

#     writer.writerow(['Joe', 'Bloggs', 40])
#     writer.writerow(['Jane', 'Smith', 50])

# append a line on csv file
# with open("newfile.csv","a") as writerfile:
#     writer = csv.writer(writerfile,delimiter=",")
#     writer.writerow(['Mike', 'Wazowski', 40])


# reading and writing in json
with open("example.json", "r") as write_file:
    jsonread = json.load(write_file)
    for dic in jsonread["menu"]["items"]:
        print(dic["id"])

#write in jason
# data = {
#  'president': {
#  'name': 'Zaphod Beeblebrox',
#  'species': 'Betelgeusian'
#  }
# }

# jsonstring = json.dumps(data)
# with open("newjsonfile.json", "w") as write_file:
#     write_file.write(jsonstring)
