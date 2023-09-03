
from __future__ import print_function, division

nat = { 'asc':{'deg':16,'sign':9,'min':15,'syb':"A"},
        'sun':{'deg':3,'sign':12,'min':3,'syb':"sun"},
        'mon':{'deg':11,'sign':11,'min':3,'syb':"mon"},
        'mec':{'deg':6,'sign':11,'min':40,'syb':"mec"},
        'ven':{'deg':25,'sign':10,'min':41,'syb':"ven"},
        'mars':{'deg':19,'sign':7,'min':10,'syb':"mars"},
        'jup':{'deg':10,'sign':8,'min':19,'syb':"jup"},
        'sat':{'deg':21,'sign':7,'min':50,'syb':"sat"},
        'ura':{'deg':4,'sign':9,'min':30,'syb':"ura"},
        
        'test':{'deg':4,'sign':1,'min':30,'syb':"test"},
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

house_tuple = ((range(0, 29),'h1'),(range(30, 30 + 29), 'h2'),(range(60, 60 + 29), 'h3'),
            (range(90, 90 + 29), 'h4'), (range(120, 120 + 29), 'h5'), (range(150, 150 + 29), 'h6'),
            (range(180, 180 + 29), 'h7'),(range(210, 210 + 29), 'h8'), (range(240, 240 + 29), 'h9'),
            (range(270, 270 + 29), 'h10'), (range(300, 300 + 29), 'h11'),(range(330, 330 + 29), 'h12')
            )

class Vedic:
    '''vars'''
    def __init__(self, natal, transit):
        self.nat = natal
        self.transit = transit
        
    def _vedicpt(self, planet):
        #get the west deg
        w_deg = self.nat[planet]['deg'] #ven = 25
        #convert to vedic
        w2v = west_to_vedic[w_deg] # [2, -1]
        
        #since it is in another sign so (sign - 1)
        
        return (w2v[0], self.nat[planet]['sign'] + w2v[1])
    
    def _vedicPointDeg(self, natPlanet_, name_):
        #get the sign num of planet and convert num to str
        a_planet_pt = convert[natPlanet_[name_]['sign']] #cap
        
        #call it in the moons house
        mon_asc = convert[self._vedicpt('mon')[1]] #cap - so the moon begins from cap
        
        #then call cap(planet pt) from cap(mon asc)
        w_planet_deg = eval(mon_asc)[a_planet_pt] #60 = pis western, so we need to - 23
        
        #planet_deg = abs(w_planet_deg - 23)
        planet_deg = w_planet_deg + natPlanet_[name_]['deg']
        
        #add to planet deg
        return planet_deg - 23 #w2v_deg[0] #60 + 2
    
    
    def houseOf(self, natPlanet, name):
        
        vpt_deg = self._vedicPointDeg(natPlanet, name)
    
        #find it in house tuple
        for h_tup, name in house_tuple:
            if vpt_deg in h_tup:
                result = name
                break 
        
        return result
    
    def house(self):
        print(convert[self.vedicpt('mon')[1]])
        #self.house_dict = ((range(vedicpt('mon')-1, vedicpt('mon')),1), (), (), (), (), (), ())
        
    """To ascertain, first of all, one is to take

    each planet and consider in which constellation it is,
    the lord of the constellation and
    note in which houses the lord of the constellation is, 
    ownership and
    find out the matters signified by the lord of the 
    constellation according to its ownership of the Bhava
    """
    
    def constellationOf(self, _natPlanet, _name):
        constellation = ((range(0, 14),'ketu'),(range(14, 27), 'ven'),(range(26, 40), 'sun'),
                         (range(38, 53), 'moon'),(range(52, 66), 'mars'),(range(65, 79), 'rahu'),
                         (range(78, 91), 'jup'),(range(90, 104), 'sat'),(range(103, 117), 'merc'),
                         
                         (range(116, 130),'ketu'),(range(129, 143), 'ven'),(range(142, 156), 'sun'),
                         (range(155, 169), 'moon'),(range(168, 181), 'mars'),(range(180, 194), 'rahu'),
                         (range(193, 207), 'jup'),(range(206, 220), 'sat'),(range(219, 233), 'merc'),
                         
                         (range(232, 246),'ketu'),(range(245, 259), 'ven'),(range(258, 271), 'sun'),
                         (range(270, 284), 'moon'),(range(283, 297), 'mars'),(range(296, 310), 'rahu'),
                         (range(309, 323), 'jup'),(range(322, 335), 'sat'),(range(334, 348), 'merc')
                         )
        
        #b = ari['ari']
        vpt_deg_ = (ari[convert[_natPlanet[_name]['sign']]] + _natPlanet[_name]['deg']) - 23   #self._vedicpt(_name)
        #print(f'vpt_deg_ = {vpt_deg_}')
        
        #find it in house tuple
        for const, name in constellation:
            if vpt_deg_ in const:
                result_ = name
                break 
        
        #which house ruled
        houseRulers = {'sun':5, 'mon':4, 'merc':[3, 6], 'ven':[2, 7], 'mars':[1, 8], 'jup':[9, 12], 'sat':[10, 11]}
        
        #convert num to sign name
        if result_ in ['sun', 'mon']:
            houseR = convert[houseRulers[result_]] #cap
            
            #create mon chart
            inMonChart = convert[self._vedicpt('mon')[1]] #cap - so the moon begins from cap
            
            #degree in the moons chart
            planetH = eval(inMonChart)[houseR] #60
            print(f'planetH = {planetH}')
            
            #search in house tuple for name
            for h_tup, name in house_tuple:
                if planetH in h_tup:
                    houseName = name
                    break 
            #print(f'houseName = {houseName}')
            return result_, houseName
        else:
            houseR = convert[houseRulers[result_][0]],convert[houseRulers[result_][1]]
            
            #create mon chart
            inMonChart = convert[self._vedicpt('mon')[1]] #cap - so the moon begins from cap
            
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
              
            return result_, houseNames
        
    
    def __str__(self):
        return f'self.nat is {self.transit}'

moon = Vedic(nat, prog)
#print(moon.vedicpt('mon'))
print(moon.houseOf(nat,'mon'))
print(moon.constellationOf(nat,'mon'))