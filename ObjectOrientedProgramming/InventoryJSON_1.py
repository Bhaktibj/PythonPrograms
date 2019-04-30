""" 1. JSON Inventory Data Management of Rice, Pulses and Wheat
Desc -> Create a JSON file having Inventory Details for Rice,
Pulses and Wheat with properties name, weight, price per kg.
Use Library : Python JSON Library
I/P -> read in JSON File
Logic -> Get JSON Object in Python Calculate the value for every Inventory.
O/P -> Create the JSON from Inventory Object and output the JSON String
 """

import json

with open('/home/shadowk/PycharmProjects/Programs_BridgeLab/Week3_Practice/Inventory.json',"r") as f:
    data1=json.load(f)
    print(data1)

for d_id, d_info in data1.items():
    print("Product is:", d_id,)

    for key in d_info:
        print(key + ':', d_info[ key ])

rice_weight = data1['Rice']['Weight']
rice_price = data1['Rice']['Price']
pulses_weight = data1['Pulses']['Weight']
pulses_price = data1['Pulses']['Price']
wheat_weight = data1['Wheat']['Weight']
wheat_price = data1['Wheat']['Price']

rice_total = rice_weight * rice_price
pulses_total = pulses_weight * pulses_price
wheat_total = wheat_weight * wheat_price


print("total cost of Rice is= ", rice_total)
print("total cost of Pulses is= ", pulses_total)
print("total cost of Wheat is= ", wheat_total)








