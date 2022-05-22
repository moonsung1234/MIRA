
import json

json_file = json.load(open("user.json"))
target1 = input("ip : ")
target2 = input("file : ")

for user in json_file :
    if user == target1 :
        for obj in json_file[user] :
            for key in obj :
                if obj[key] == target2 :
                    print(obj["table"])