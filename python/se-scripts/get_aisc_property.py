import json

with open('shape_database.json') as shape_properties:
    shape_db = json.load(shape_properties)

while 1:    
    select_size = input('Enter a size: ').upper().strip(' ')
    if select_size in shape_db.keys():
        while 1:
            select_property = input('Enter a property: ').strip(' ')
            if select_property in shape_db[select_size].keys():
                print(f"The {select_property} for {select_size} is {shape_db[select_size][select_property]}.")
                break
            else:
                print(f"{select_property} is not a valid property. Please try again.")
        break
    else:
        print(f"{select_size} is not a valid size. Please try again.")
