
from __future__ import print_function, division
from capSubs import capSub, aquaSub

nat = { 'asc':{'deg':16,'sign':9,'min':15,'syb':"A"},
        'sun':{'deg':3,'sign':12,'min':3,'syb':"sun"},
        'mon':{'deg':11,'sign':11,'min':3,'syb':"mon"},
        'merc':{'deg':6,'sign':11,'min':40,'syb':"merc"},
        'ven':{'deg':25,'sign':10,'min':41,'syb':"ven"},
        'mars':{'deg':19,'sign':7,'min':10,'syb':"mars"},
        'jup':{'deg':10,'sign':8,'min':19,'syb':"jup"},
        'sat':{'deg':21,'sign':7,'min':50,'syb':"sat"},
        'rahu':{'deg':21,'sign':4,'min':56,'syb':"rahu"},
        'ketu':{'deg':21,'sign':10,'min':56,'syb':"ketu"},
        #'ura':{'deg':4,'sign':9,'min':30,'syb':"ura"},
        
        #'test':{'deg':4,'sign':1,'min':30,'syb':"test"},
        #nep:{deg:26,sign:9,min:41,syb:"nep"},
        #plu:{deg:26,sign:7,min:46,syb:"plu"},
        #nod:{deg:21,sign:4,min:56,syb:"nod"},
        #pat:{deg:8,sign:10,min:15,syb:"pat"},
     }

transit = {
            'sat':{'deg':6, 'sign':12, 'min':29, 'syb':'tsat'} #to the materal world measurement
            }

prog = { 
        'sun':{'deg':14,'sign':1,'min':3,'syb':"sun"},
        'mon':{'deg':25,'sign':5,'min':3,'syb':"mon"}, #to the inner world measurement
        }

west_to_vedic = {0:[7 ,-1],1:[8,-1],2:[9,-1],3:[10,-1],4:[11,-1],5:[12,-1],6:[12,-1],7:[14,-1],8:[15,-1],9:[16,-1],10:[17,-1],
                 11:[18,-1],12:[19,-1],13:[20,-1],14:[21,-1],15:[22,-1],16:[23,-1],17:[24,-1],18:[25,-1],19:[26,-1],20:[27,-1],
                 21:[28,-1],22:[29,-1],23:[0,0],24:[1,0],25:[2,0],26:[3,0],27:[4,0],28:[5,0],29:[6,0]}

convert = [0,"ari","tua","gem","can","leo","vir","lib","sco","sag","cap","aqu","pis"];


#for houses
ari = {'ari':360,'tua':30,'gem':60,'can':90,'leo':120,'vir':150,'lib':180,'sco':210,'sag':240,'cap':270,'aqu':300,'pis':330}
pis = {'pis':360,'ari':30,'tua':60,'gem':90,'can':120,'leo':150,'vir':180,'lib':210,'sco':240,'sag':270,'cap':300,'aqu':330}
tua = {'tua':360,'gem':30,'can':60,'leo':90,'vir':120,'lib':150,'sco':180,'sag':210,'cap':240,'aqu':270,'pis':300,'ari':330}
gem = {'gem':360,'can':30,'leo':60,'vir':90,'lib':120,'sco':150,'sag':180,'cap':210,'aqu':240,'pis':270,'ari':300,'tua':330}
can = {'can':360,'leo':30,'vir':60,'lib':90,'sco':120,'sag':150,'cap':180,'aqu':210,'pis':240,'ari':270,'tua':300,'gem':330}
leo = {'leo':360,'vir':30,'lib':60,'sco':90,'sag':120,'cap':150,'aqu':180,'pis':210,'ari':240,'tua':270,'gem':300,'can':330}
vir = {'vir':360,'lib':30,'sco':60,'sag':90,'cap':120,'aqu':150,'pis':180,'ari':210,'tua':240,'gem':270,'can':300,'leo':330}
lib = {'lib':360,'sco':30,'sag':60,'cap':90,'aqu':120,'pis':150,'ari':180,'tua':210,'gem':240,'can':270,'leo':300,'vir':330}
sco = {'sco':360,'sag':30,'cap':60,'aqu':90,'pis':120,'ari':150,'tua':180,'gem':210,'can':240,'leo':270,'vir':300,'lib':330}
sag = {'sag':360,'cap':30,'aqu':60,'pis':90,'ari':120,'tua':150,'gem':180,'can':210,'leo':240,'vir':270,'lib':300,'sco':330}
cap = {'cap':360,'aqu':30,'pis':60,'ari':90,'tua':120,'gem':150,'can':180,'leo':210,'vir':240,'lib':270,'sco':300,'sag':330}
aqu = {'aqu':360,'pis':30,'ari':60,'tua':90,'gem':120,'can':150,'leo':180,'vir':210,'lib':240,'sco':270,'sag':300,'cap':330}

zodiac = {1:360, 2:30, 3:60, 4:90, 5:120, 6:150, 7:180, 8:210, 9:240, 10:270, 11:300, 12:330}

house_tuple = ((range(0, 30),'h1'),(range(30, 60), 'h2'),(range(60, 90), 'h3'),
            (range(90, 120), 'h4'), (range(120, 150), 'h5'), (range(150, 180), 'h6'),
            (range(180, 210), 'h7'),(range(210, 240), 'h8'), (range(240, 270), 'h9'),
            (range(270, 300), 'h10'), (range(300, 330), 'h11'),(range(330, 360), 'h12')
            )

class VediChart:
    '''vars'''
    def __init__(self, natal, transit_):
        self.nat = natal
        self.transit = transit_
        
    def _vedicpt(self, planet):
        #get the west deg
        w_deg = self.nat[planet]['deg'] #mon = 11
        #convert to vedic
        w2v = west_to_vedic[w_deg] # [2, -1]
        
        #since it is in another sign so (sign - 1)
        
        return (w2v[0], self.nat[planet]['sign'] + w2v[1]) #returns(18, 10)
    
    def _vedicPointDeg(self, natPlanet_, name_):
        #get the sign num of planet and convert num to str
        a_planet_pt = convert[natPlanet_[name_]['sign']] #cap
        
        #creat the moon chart from CAP
        monChart = convert[self._vedicpt('mon')[1]] #returns (18, 10) - cap - so the chart begins from cap
        
        #then call cap(planet pt) from cap(mon asc)
        w_planet_deg = eval(monChart)[a_planet_pt] #60
        
        #add deg
        planet_deg = w_planet_deg + natPlanet_[name_]['deg'] #23
        
        #make it vedic
        return planet_deg - 23
    
    
    def houseOf(self, natPlanet, name):
        
        vpt_deg = self._vedicPointDeg(natPlanet, name) #returns 287
    
        #find it in house tuple
        for h_tup, name_ in house_tuple:
            if vpt_deg in h_tup:
                result = name_
                break 
        
        return result
    
    def house(self):
        #print(convert[self.vedicpt('mon')[1]])
        #self.house_dict = ((range(vedicpt('mon')-1, vedicpt('mon')),1), (), (), (), (), (), ())
        pass
    
        
    def constellationOf(self, _natPlanet, _name, asc='mon'):
        constellation = ((range(0, 14),'ketu'),(range(15, 27), 'ven'),(range(27, 41), 'sun'),
                         (range(41, 59), 'mon'),(range(59, 67), 'mars'),(range(67, 81), 'rahu'),
                         (range(81, 94), 'jup'),(range(94, 107), 'sat'),(range(107, 121), 'merc'),
                         
                         (range(121, 134),'ketu'),(range(134, 147), 'ven'),(range(147, 161), 'sun'),
                         (range(161, 174), 'mon'),(range(174, 187), 'mars'),(range(187, 201), 'rahu'),
                         (range(201, 214), 'jup'),(range(214, 227), 'sat'),(range(227, 241), 'merc'),
                         
                         (range(241, 254),'ketu'),(range(254, 267), 'ven'),(range(267, 281), 'sun'),
                         (range(281, 294), 'mon'),(range(294, 307), 'mars'),(range(307, 321), 'rahu'),
                         (range(321, 334), 'jup'),(range(334, 347), 'sat'),(range(347, 360), 'merc')
                         )
        
        #b = ari['ari']
        vpt_deg_ = (ari[convert[_natPlanet[_name]['sign']]] + _natPlanet[_name]['deg']) - 23
        #print(f'vpt_deg_ = {vpt_deg_}')
        
        #find it in house tuple
        for const, name in constellation:
            if vpt_deg_ in const:
                result_ = name #jup
                break 
        
        #which house ruled
        houseRulers = {'sun':5, 'mon':4, 'merc':[3, 6], 'ven':[2, 7], 'mars':[1, 8], 'jup':[9, 12], 'sat':[10, 11]}
        
        #if mon in 
        if result_ in ['sun', 'mon']:
            #convert num to sign name
            houseR = convert[houseRulers[result_]] #can
            
            #create mon chart
            inMonChart = convert[self._vedicpt(asc)[1]] #cap - so the chart begins from cap moon sign
            
            #planet degree in the moons chart
            '''            cap[can]'''
            planetH = eval(inMonChart)[houseR] #180
            
            #search in house tuple for name
            for h_tup, name in house_tuple:
                if planetH in h_tup:
                    houseName = name
                    break 
            return result_, houseName #moon, rule house but in
        
        elif result_ in ['merc', 'ven', 'mars', 'jup', 'sat']:
            houseR = convert[houseRulers[result_][0]],convert[houseRulers[result_][1]]
            
            #create mon chart
            inMonChart = convert[self._vedicpt(asc)[1]] #cap - so the moon begins from cap
            
            housesInChart = []
            houseNames = []
            
            #degree in the moons chart
            for hou in houseR:
                housesInChart.append(eval(inMonChart)[hou])
            
            #search in house tuple for name
            for h_tup, name in house_tuple:
                for hous in housesInChart:
                    if hous in h_tup:
                        houseNames.append(name)
                        break
              
            return result_, houseName #moon, rule house but in
        else:
            return ('jup', 'h9', range(281, 294))
        
    def subOf(self, _natPlanet, _name):
        
        def tI(hour=0, minute=0, second=0):
            minutes = hour * 60 + minute
            seconds = minutes * 60 + second
            return seconds
        
        #what is degre of planet in 360 then convert to vedic
        vedicPlanetDeg = (zodiac[_natPlanet[_name]['sign']] + _natPlanet[_name]['deg']) - 23 #returns 283
        #print(f'vedicPlanetDeg = {vedicPlanetDeg}')
        
        #what is the constellationOf planet
        planetConst = self.constellationOf(_natPlanet, _name, asc='asc') #returns ('mon', 'h9', range(281, 294))
        print(f'planetConst = {planetConst}')
        
        
        for sub, range_ in capSub:
            #if tI(283, 11)
            if tI(vedicPlanetDeg, _natPlanet[_name]['min']) in range_:
                resulttt = sub
                break
        
        
        oracle_1 = f"{_name} is in {planetConst[0]} const, {planetConst[0]} rules {planetConst[1]},"
        oracle_2 = f"so {_name} will give the result of {planetConst[1]}."
        oracle_3 = f"But will the {planetConst[1]} be good or bad? My answer: the {planetConst[1]} will be challenging b/c {_name} sub {sub} is in 12H"
                
        return {'oracle_1':oracle_1, 'oracle_2':oracle_2, 'oracle_3':oracle_3}  
    
    def __str__(self):
        return f'self.nat is {self.transit}'

inMoonChart = VediChart(nat, prog)
#print(inMoonChart._vedicpt('mon'))
#print(inMoonChart.houseOf(nat, 'jup'))
#print(inMoonChart.constellationOf(nat, 'mars'))
print(inMoonChart.subOf(nat, 'rahu'))
