import json

with open ("sample_json.json") as f:
    python_dic =json.load(f)

    print(python_dic)
    for key,value in python_dic.items():
        print(key,'is',value)

        python_dic2 = {"mobile":"iphone","laptop":"lenovo","color":"red"}
        json_str=json.dumps(python_dic2)
        print(json_str)
        with open("data.json","w")as f:
            json.dump(python_dic2,f)