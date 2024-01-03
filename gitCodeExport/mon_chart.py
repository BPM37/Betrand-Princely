from __future__ import print_function, division
from mon_chart_reading import reading

sign_tuple = ((range(0, 30),'AR'),(range(30, 60), 'TA'),(range(60, 90), 'GE'),
            (range(90, 120), 'CN'), (range(120, 150), 'LE'), (range(150, 180), 'VI'),
            (range(180, 210), 'LI'),(range(210, 240), 'SC'), (range(240, 270), 'SG'),
            (range(270, 300), 'CP'), (range(300, 330), 'AQ'),(range(330, 360), 'PI')
            )

zodiac = {'AR':0, 'TA':30, 'GE':60, 'CN':90, 'LE':120, 'VI':150, 'LI':180, 'SC':210, 'SG':240, 'CP':270,
          'AQ':300, 'PI':330}

zodiac_to_num = {'AR':1, 'TA':2, 'GE':3, 'CN':4, 'LE':5, 'VI':6, 'LI':7, 'SC':8, 'SG':9, 'CP':10,'AQ':11, 'PI':12}

elements = {'AR':'fire', 'TA':'earth', 'GE':'air', 'CN':'water', 'LE':'fire', 'VI':'earth', 'LI':'air', 'SC':'water',
            'SG':'fire', 'CP':'earth','AQ':'air', 'PI':'water'}

rulership = {'AR':'mas', 'TA':'ven', 'GE':'mec', 'CN':'mon', 'LE':'sun', 'VI':'mec', 'LI':'ven', 'SC':'mas',
             'SG':'jup', 'CP':'sat', 'AQ':'sat', 'PI':'jup'}

#for houses
AR = {'H1':'AR','H2':'TA','H3':'GE','H4':'CN','H5':'LE','H6':'VI',
      'H7':'LI','H8':'SC','H9':'SG','H10':'CP','H11':'AQ','H12':'PI'}
TA = {'H1':'TA','H2':'GE','H3':'CN','H4':'LE','H5':'VI','H6':'LI',
      'H7':'SC','H8':'SG','H9':'CP','H10':'AQ','H11':'PI','H12':'AR'}
GE = {'H1':'GE','H2':'CN','H3':'LE','H4':'VI','H5':'LI','H6':'SC',
      'H7':'SG','H8':'CP','H9':'AQ','H10':'PI','H11':'AR','H12':'TA'}
CN = {'H1':'CN','H2':'LE','H3':'VI','H4':'LI','H5':'SC','H6':'SG',
      'H7':'CP','H8':'AQ','H9':'PI','H10':'AR','H11':'TA','H12':'GE'}
LE = {'H1':'LE','H2':'VI','H3':'LI','H4':'SC','H5':'SG','H6':'CP',
      'H7':'AQ','H8':'PI','H9':'AR','H10':'TA','H11':'GE','H12':'CN'}
VI = {'H1':'VI','H2':'LI','H3':'SC','H4':'SG','H5':'CP','H6':'AQ',
      'H7':'PI','H8':'AR','H9':'TA','H10':'GE','H11':'CN','H12':'LE'}
LI = {'H1':'LI','H2':'SC','H3':'SG','H4':'CP','H5':'AQ','H6':'PI',
      'H7':'AR','H8':'TA','H9':'GE','H10':'CN','H11':'LE','H12':'VI'}
SC = {'H1':'SC','H2':'SG','H3':'CP','H4':'AQ','H5':'PI','H6':'AR',
      'H7':'TA','H8':'GE','H9':'CN','H10':'LE','H11':'VI','H12':'LI'}
SG = {'H1':'SG','H2':'CP','H3':'AQ','H4':'PI','H5':'AR','H6':'TA',
      'H7':'GE','H8':'CN','H9':'LE','H10':'VI','H11':'LI','H12':'SC'}
CP = {'H1':'CP','H2':'AQ','H3':'PI','H4':'AR','H5':'TA','H6':'GE',
      'H7':'CN','H8':'LE','H9':'VI','H10':'LI','H11':'SC','H12':'SG'}
AQ = {'H1':'AQ','H2':'PI','H3':'AR','H4':'TA','H5':'GE','H6':'CN',
      'H7':'LE','H8':'VI','H9':'LI','H10':'SC','H11':'SG','H12':'CP'}
PI = {'H1':'PI','H2':'AR','H3':'TA','H4':'GE','H5':'CN','H6':'LE',
      'H7':'VI','H8':'LI','H9':'SC','H10':'SG','H11':'CP','H12':'AQ'}



class MoonChart:
    '''vars'''
    def __init__(self, natal, transit_):
        self.nat = natal
        self.transit = transit_
        self.namesInnat = ('sun','mon','mec','ven','mas','jup','sat','rah','ket')#'asc',

    def _vedicpt(self, planet):
        """returns the planet vedic degree and sign"""
        
        zodiacDeg = (zodiac[self.nat[planet]['sign']] +  self.nat[planet]['deg']) - 23 #sun (330 + 3) - 23 = 310
       
        
        #get the range of 310
        for range_, name_ in sign_tuple:
            if zodiacDeg in range_:
                vedic_sign = name_ #AQ
                
        #                 310 - 300 = 10
        vedicDeg = zodiacDeg - zodiac[vedic_sign]
        #strenght = planetStrenght[vedic_sign].get(self.nat[planet]['syb'])
        
        
        #                10             aq                       310
        return {'deg':vedicDeg, 'sign':vedic_sign, 'zodiac_deg':zodiacDeg} 

    
    def _drawChart(self, asc='mon'): #planet_name
        
        ascSignName = self._vedicpt(asc)['sign'] #cap
        
        #creat the moon chart from CAP
        #to creat planet chart call for planet sign ie cap here
        natChart = eval(ascSignName)  #a dict of cap          [a_planet_pt] #60
        
        return natChart
    
    def kamajuruma_yoga(self, asc='mon'):
        
        kamaj_read_list = []
        
        
        #fourth and tenth
        with_moon = eval(self._vedicpt(asc)['sign'])['H1']
        fourth = eval(self._vedicpt(asc)['sign'])['H4']
        tenth = eval(self._vedicpt(asc)['sign'])['H10']
        
        kamaj_list = ('with_moon','fourth','tenth')
        
        #is the any planet with the moon?
        for name_kamaj in self.namesInnat:
            for kamaj in kamaj_list:
                
                if self._vedicpt(name_kamaj)['zodiac_deg'] in range(zodiac[eval(kamaj)],zodiac[eval(kamaj)] + 29) \
                   and name_kamaj not in ['asc', 'sun', 'rah', 'ket', 'mon']:
                    kamaj_read_list.append(f'{name_kamaj}_{kamaj}')

           
        return kamaj_read_list
        
    
    def moon_help__Houses(self, asc='mon'):
        read_list = []
        
        high_tide_list = [] #sixth seventh and eighth
        support_list = []
        resources_list = []
        
        #namesInnat = ('asc','sun','mon','mec','ven','mas','jup','sat','rah','ket')
        source_list = ('support','resources','sixth','seventh','eighth')
        
        
        support = eval(self._vedicpt(asc)['sign'])['H12'] #['AQ',range(30,59)]
        resources = eval(self._vedicpt(asc)['sign'])['H2']
        sixth = eval(self._vedicpt(asc)['sign'])['H6']
        seventh = eval(self._vedicpt(asc)['sign'])['H7']
        eighth = eval(self._vedicpt(asc)['sign'])['H8']
        
        #support
        for namee in self.namesInnat:
            for sources in source_list:
                if self._vedicpt(namee)['zodiac_deg'] in range(zodiac[eval(sources)],zodiac[eval(sources)] + 29) \
                   and namee not in ['asc', 'sun', 'rah', 'ket']:
                    
                    if namee in ['sixth','seventh','eighth']:
                        high_tide_list.append([high_tide, f'high_tide_{namee}'])
                    if namee == 'support':
                        support_list.append([support, f'support_{namee}'])
                    if namee == 'resources':
                        resources_list.append([resources, f'resources_{namee}'])
                        
        if support_list != []:
            read_list.append(reading[support_list[0]],reading[support_list[1]])
            
        if resources_list != []:
            read_list.append(reading[resources_list[0]],reading[resources_list[1]])
        
        if high_tide_list != []:
            read_list.append(reading[high_tide_list[0]],reading[high_tide_list[1]])
                        
        if high_tide_list == [] and support_list == [] and resources_list == []:
            check_planets_with_the_moon = ''
            read_list = self.kamajuruma_yoga()
        
        return read_list
    
    def fifth_and_ninth(self, asc='mon'):
        fifth_and_ninth_listt = []
        
        fifth = eval(self._vedicpt(asc)['sign'])['H5']
        ninth = eval(self._vedicpt(asc)['sign'])['H9']
        
        source_list = ('fifth','ninth')
        
        for namee in self.namesInnat:
            for sources in source_list:
                if self._vedicpt(namee)['zodiac_deg'] in range(zodiac[eval(sources)],zodiac[eval(sources)] + 29):
                    if namee in ['ven','mec','jup']:
                        fifth_and_ninth_listt.append('benefics_fifth_or_ninth')
                    if namee not in ['ven','mec','jup']:
                        fifth_and_ninth_listt.append(f'{namee}_fifth_or_ninth')
                    
        if fifth_and_ninth_listt != []:
            fifth_and_ninth_list = ['fifth_and_ninth_title'] + fifth_and_ninth_listt
                    
        return fifth_and_ninth_list
    
    def moon_sign_element(self, asc='mon'):
        signn = eval(self._vedicpt(asc)['sign'])['H1']
        return elements[signn]
    
    def house_matters(self, house, asc='mon'):
        any_planet_in_house = []
        planet_in_house_dict = {}
        aspect_dict = []
        occupied_by_benefic = []
        bhlords = []
        bhlord_aspects = []
        num_values = []
        
        benefics = ['mec', 'ven', 'jup']#'wax_mon'
        malifics = ['mas', 'sat', 'rah', 'ket', 'sun']#'wan_mon'
        
        house_sign = eval(self._vedicpt(asc)['sign'])[f'H{house}'] #AQ 2H
        house_range = range(zodiac[house_sign],zodiac[house_sign] + 29)
        hlord = rulership[house_sign] #3=jup   
        
        #if occupied by lord
        if hlord in house_range:
            lord_occupation = 'YES'
        lord_occupation = 'NO'
        
        #other ocuupants
        for planets in self.nat:
            vedic_deg = self._vedicpt(planets)['zodiac_deg'] #310 sun
            if vedic_deg in house_range and planets not in ['mon', 'asc']:
                any_planet_in_house.append(planets)
                
        for house_occupants in any_planet_in_house:
            if house_occupants in benefics:
                occupied_by_benefic.append('PASSED')
                #print(f'PASSED house_occupants = {house_occupants}')
            else:
                occupied_by_benefic.append(f'FAILED_{house_occupants}')
                #print(f'FAILED house_occupants = {house_occupants}')
                
        #occupied owners of benefics
        benefic_house_ranges = ('H1','H4', 'H5','H7','H9','H10')
        for Hs in benefic_house_ranges:
            bhlord = eval(self._vedicpt(asc)['sign'])[Hs]
            bhlords.append(bhlord)
            if bhlord in house_range:
                occupied_by_bh = 'YES'
            occupied_by_bh = 'NO'
        
        
        #aspected by benefics
        moon_house_ranges = ('H1', 'H2', 'H3', 'H4', 'H5', 'H6','H7', 'H8', 'H9', 'H10', 'H11', 'H12')
        
        for planets in self.nat:
            for houses in moon_house_ranges:
                range_ = range(zodiac[eval(self._vedicpt(asc)['sign'])[houses]],\
                               zodiac[eval(self._vedicpt(asc)['sign'])[houses]]+30)
                if self._vedicpt(planets)['zodiac_deg'] in range_:
                    planet_in_house_dict[planets] = eval(self._vedicpt(asc)['sign'])[houses]
        print(planet_in_house_dict)
        def aspects(planet, dicts):
            aspect_list = []
            
            sun = {'full':6,'special_1':0,'special_2':0}
            mon = {'full':6,'special_1':0,'special_2':0}
            mec = {'full':6,'special_1':0,'special_2':0}
            ven = {'full':6,'special_1':0,'special_2':0}
            mas = {'full':6,'special_1':3,'special_2':7}
            jup = {'full':6,'special_1':4,'special_2':8}
            sat = {'full':6,'special_1':2,'special_2':9}
            ket = {'full':6,'special_1':1,'special_2':3,'special_3':7}
            
            movable = [1,4,7,10]
            fixed = [2,5,8,11]
            mutables = [3,6,9,12]
            
            AR = [5,8,11]
            CN = [8,11,2]
            LI = [11,2,5]
            CP = [2,5,8]
            
            GE = [6,9,12]
            
            
            
            aspect_tup = ('full','special_1','special_2')
            
            for key, value in dicts.items():
                for asp in aspect_tup:
                    if key == planet:
                        aspectt = zodiac_to_num[value] + eval(planet)[asp]
                        if aspectt >= 13:
                            planet_aspect = aspectt - 12
                        else:
                            planet_aspect = aspectt 
                    
                        aspect_list.append(planet_aspect)
                
            if zodiac_to_num[house_sign] in aspect_list:
                return planet
                     
        #NOW is it aspected by benefics
        for beneficss in benefics:
            aspet = aspects(beneficss, planet_in_house_dict)
            if aspet != None:
                aspect_dict.append(aspet)
                
        #NOW is it aspected by benefics house lords
        for bhlordds in bhlords:
            aspet = aspects(bhlordds, planet_in_house_dict)
            if aspet != None:
                bhlord_aspects.append(aspet)
                
        #Now numerical values #is house lord in house
        if lord_occupation == 'NO':
            #{'sun': 'AQ', 'mon': 'CP', 'mec': 'CP', 'ven': 'CP', 'mas': 'VI', 'jup': 'LI', 'sat': 'VI', 'rah': 'GE'}
            #search the house to find it
            for k, v in eval(house_sign).items():
                if v == planet_in_house_dict[rulership[house_sign]]:
                    hlord_num_away_lag = int(k[1:])
                    hlord_num_away_h = hlord_num_away_lag - (house - 1)
            #hlord_num_away = planet_in_house_dict[rulership[house_sign]] #
            print('hlord_num_away_lag = ',hlord_num_away_lag)
            print('hlord_num_away_h = ',hlord_num_away_h)
            #num_values.append('YES')
            
        return {'occupied_by_benefic':occupied_by_benefic, 'aspected_by_benefics':aspect_dict,
                'occupied_by_lord':lord_occupation, 'aspected_by_lord':aspects(hlord, planet_in_house_dict),
                'occupied_by_bh':occupied_by_bh,'aspected_by_bhlord':bhlord_aspects}
    
    def house_occupant(self, house, asc='mon'):
        any_planet_in_house = []
        
        house_sign = eval(self._vedicpt(asc)['sign'])[f'H{house}'] #AQ 2H
        house_range = range(zodiac[house_sign],zodiac[house_sign] + 29)
        
         #other ocuupants
        for planets in self.nat:
            vedic_deg = self._vedicpt(planets)['zodiac_deg'] #310 sun
            if vedic_deg in house_range:
                any_planet_in_house.append(planets)
            
        #if any_planet_in_house == []:
         #   any_planet_in_house.append(f'lord_{rulership[house_sign]}')
         
         
        return any_planet_in_house
    
    def house_aspects(self, house, asc='mon'):
        aspect_list = []
        sight_aspect = []
        rashi_aspect = []
        planet_in_house_dictt = {}
        
        house_sign = eval(self._vedicpt(asc)['sign'])[f'H{house}']
        
        #aspected by benefics
        planet_house_ranges = ('H1', 'H2', 'H3', 'H4', 'H5', 'H6','H7', 'H8', 'H9', 'H10', 'H11', 'H12')
        
        for planets in self.nat:
            for houses in planet_house_ranges:
                range_ = range(zodiac[eval(self._vedicpt(asc)['sign'])[houses]],\
                               zodiac[eval(self._vedicpt(asc)['sign'])[houses]]+30)
                if self._vedicpt(planets)['zodiac_deg'] in range_ and planets not in ['asc','ket']:
                    planet_in_house_dictt[planets] = eval(self._vedicpt(asc)['sign'])[houses]
        #print(planet_in_house_dictt)
        
        
        
        sun = {'full':6,'special_1':0,'special_2':0}
        mon = {'full':6,'special_1':0,'special_2':0}
        mec = {'full':6,'special_1':0,'special_2':0}
        ven = {'full':6,'special_1':0,'special_2':0}
        mas = {'full':6,'special_1':3,'special_2':7}
        jup = {'full':6,'special_1':4,'special_2':8}
        sat = {'full':6,'special_1':2,'special_2':9}
        rah = {'full':6,'special_1':1,'special_2':3,'special_3':7}
        
        movable = [1,4,7,10]
        fixed = [2,5,8,11]
        mutables = [3,6,9,12]
        
        AR = [5,8,11]
        CN = [8,11,2]
        LI = [11,2,5]
        CP = [2,5,8]
        
        GE = [6,9,12]
        
        
        #ruler = eval(self._vedicpt(asc)['sign'])[f'H{house}']
        #print(house_sign)
        aspect_tup = ('full','special_1','special_2')
        print(planet_in_house_dictt)
        for key, value in planet_in_house_dictt.items():
            for asp in aspect_tup:
                aspectt = zodiac_to_num[value] + eval(key)[asp]#sun['full']
                print(aspectt)
                if aspectt >= 13:
                    planet_aspect = aspectt - 12
                else:
                    planet_aspect = aspectt
                print(zodiac_to_num[house_sign], planet_aspect, key)    
                if zodiac_to_num[house_sign] == planet_aspect:
                    sight_aspect.append(key)
                #then rashi aspects
                
        return sight_aspect
         
    def __str__(self):
        return """returns the planet vedic degree and sign"""
    






    
nat = { 'asc':{'deg':16,'sign':'SG','min':15,'syb':"A"},
        'sun':{'deg':3,'sign':'PI','min':3,'syb':"sun"},
        'mon':{'deg':11,'sign':'AQ','min':3,'syb':"mon"},
        'mec':{'deg':6,'sign':'AQ','min':40,'syb':"merc"},
        #'mec':{'deg':24,'sign':'LE','min':40,'syb':"merc"},
        'ven':{'deg':25,'sign':'CP','min':41,'syb':"ven"},
        'mas':{'deg':19,'sign':'LI','min':10,'syb':"mars"},
        'jup':{'deg':10,'sign':'SC','min':19,'syb':"jup"},
        'sat':{'deg':21,'sign':'LI','min':50,'syb':"sat"},
        'rah':{'deg':21,'sign':'CN','min':56,'syb':"rahu"},
        'ket':{'deg':21,'sign':'CP','min':56,'syb':"ketu"},
        #'p_fort':{'deg':8,'sign':'CP','min':15,'syb':"p_fort"},
        }

transit = {
        'sat':{'deg':1, 'sign':12, 'min':29, 'syb':'tsat'} #to the materal world measurement
        }

moon_chart = MoonChart(nat, transit)
#moon_chart_secret = moon_chart.moon_help__Houses()
#personality = moon_chart.moon_sign_element()
#house_effect_nat = moon_chart.house_matters(12, asc='asc')
house_effect = moon_chart.house_matters(4)
#print(house_effect) #moon_chart_secret,personality
#print()
print(house_effect,moon_chart.house_aspects(4))
