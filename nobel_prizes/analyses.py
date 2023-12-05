import json
from geopy.geocoders import Nominatim
import matplotlib.pyplot as plt

def getMostFreqName(laureates):
    names = []
    namesOcc = []
    for person in laureates:
        if 'givenName' in person:
            if person['givenName']['en'] in names:
                namesOcc[names.index(person['givenName']['en'])] += 1
            else:
                names.append(person['givenName']['en'])
                namesOcc.append(1)

    max_count = max(namesOcc)
    return names[namesOcc.index(max_count)]

def plotBirthplaces(laureates):
    places = []
    names = []
    for person in laureates:
        if 'birth' in person and 'place' in person['birth'] and 'country' in person['birth']['place'] and 'givenName' in person:
            places.append(person['birth']['place']['country']['en'])
            names.append(person['givenName']['en'])

    #lat, long
    for i in range(0, len(places)):
        place_name = places[i].split(",")[0] if ',' in places[i] else places[i] 
        places[i] = place_name        

    places_set = list(set(places))
    places_occ = []
    for elem in places_set:
        places_occ.append([elem, places.count(elem)])

    sorted_places = sorted(places_occ, key=lambda l:l[1])
    
    for elem in sorted_places:
        print(elem[0], elem[1])
    
    #occs = [x[1] for x in sorted_places]
    #fig = plt.figure()
    #ax = fig.add_axes([0,0,1,1])
    #ax.bar(places_set, occs)
    #plt.xticks(places_set)
    #plt.show()

with open("json_laureates.json", "r") as file:
    laureates = json.load(file)
    #for person in laureates:
    #    print(person)
    #    break    
    plotBirthplaces(laureates=laureates)   
    