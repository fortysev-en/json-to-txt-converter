import json

person_dict = {}
final_dict = ""


#import json file and load the content in person_dict as a dictionary
with open('input.json') as f:
    person_dict.update(json.load(f))
    #get the first list from the json(person_dict)
    first = list(person_dict['Raspberry'])
    for data in first:
        try:
            final_dict = final_dict + ("Country: " + data[str('Country')] + "\n")
            final_dict = final_dict + ("State: " + data[str('State')] + "\n")
            final_dict = final_dict + ("City: " + data[str('City')] + "\n")
            final_dict = final_dict + ("====================================" + "\n")
        except:
            pass
        try:
            final_dict = final_dict + ("Id: " + data[str('ID')] + "\n")
            final_dict = final_dict + ("Latitude: " + data[str('LAT')] + "\n")
            final_dict = final_dict + ("Longitude: " + data[str('LONG')] + "\n")
            final_dict = final_dict + ("------------------------------------" + "\n")
        except:
            pass

text_file = open("sample.txt", "w") # write output as a txt
n = text_file.write(final_dict)
text_file.close()