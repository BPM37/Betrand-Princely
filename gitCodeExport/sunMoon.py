from __future__ import print_function, division

moon, sun = {'deg':11,'min':5,'sign':11}, {'deg':3,'min':3,'sign':12}

lunar , solar = [11, 12, 1, 2, 3, 4], [5,6,7,8,9,10]

moon_strenght = {'strong':0, 'exalted':[2, 3], 'weak':10} #tau 3 deg
sun_strenght = {'strong':8, 'exalted':[1,19], 'weak':11}


def planetStrenght(moonPt):
    if moon['sign'] in lunar:
        moon_strenght_1 = 'lunar'
        if moon['sign'] == moon_strenght['exalted'][0]:
            moon_strenght_2 = 'exalted'
        else: #moon['sign'] == moon_strenght.weak:
            moon_strenght_2 = 'weak'
            
    return moon_strenght_1, moon_strenght_2

def planetStrenghtclass(planetPt, planet_strenght):
    if planetPt['sign'] in lunar:
        planet_strenght_1 = 'lunar'
    else:
        planet_strenght_1 = 'solar'
        
    if planetPt['sign'] == planet_strenght['exalted'][0]:
        planet_strenght_2 = 'exalted'
        
    elif planetPt['sign'] == planet_strenght['strong']:
        planet_strenght_2 = 'strong'
        
    else: #moon['sign'] == moon_strenght.weak:
        planet_strenght_2 = 'weak'
    
            
    return planet_strenght_1, planet_strenght_2

#print(planetStrenght(moon))
print(planetStrenghtclass(sun, sun_strenght))

#when will  the moon come to  sun
#relationship moon and sun  aspects
#moon in house
#moon lord strenght
#sun in house
#moon in sign
#sun in sign
#sun lord strenght
