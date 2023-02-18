import json

jsondata = open('sample-data.json').read()

json_obj = json.loads(jsondata)
print('''================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------''')
for i in json_obj["imdata"]:
        dn = i["l1PhysIf"]["attributes"]["dn"]
        descr = i["l1PhysIf"]["attributes"]["descr"]
        speed = i["l1PhysIf"]["attributes"]["speed"]
        mtu = i["l1PhysIf"]["attributes"]["mtu"]
        print("{0:50} {1:20} {2:9} {3:}".format(dn,descr,speed,mtu))
