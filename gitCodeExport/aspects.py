from __future__ import print_function, division
from sunMonConnection import sunMon

nat = { 'asc':{'deg':16,'sign':9,'min':15,'syb':"A"},
        'sun':{'deg':3,'sign':12,'min':3,'syb':"sun"},
        'mon':{'deg':11,'sign':11,'min':3,'syb':"mon"},
        'mec':{'deg':6,'sign':11,'min':40,'syb':"mec"},
        'ven':{'deg':25,'sign':10,'min':41,'syb':"ven"},
        'mars':{'deg':19,'sign':7,'min':10,'syb':"mars"},
        'jup':{'deg':10,'sign':8,'min':19,'syb':"jup"},
        'sat':{'deg':21,'sign':7,'min':50,'syb':"sat"},
        'ura':{'deg':4,'sign':9,'min':30,'syb':"ura"},
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


zodiac = {1:360, 2:30, 3:60, 4:90, 5:120, 6:150, 7:180, 8:210, 9:240, 10:270, 11:300, 12:330}

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
cap = {'cap':0,'aqu':30,'pis':60,'ari':90,'tua':120,'gem':150,'can':180,'leo':210,'vir':240,'lib':270,'sco':300,'sag':330}
aqu = {'aqu':360,'pis':30,'ari':60,'tua':90,'gem':120,'can':150,'leo':180,'vir':210,'lib':240,'sco':270,'sag':300,'cap':330}


west_to_vedic = {0:[7,-1],1:[8,-1],2:[9,-1],3:[10,-1],4:[11,-1],5:[12,-1],6:[12,-1],7:[14,-1],8:[15,-1],9:[16,-1],10:[17,-1],
                 11:[18,-1],12:[19,-1],13:[20,-1],14:[21,-1],15:[22,-1],16:[23,-1],17:[24,-1],18:[25,-1],19:[26,-1],20:[27,-1],
                 21:[28,-1],22:[29,-1],23:[0,0],24:[1,0],25:[2,0],26:[3,0],27:[4,0],28:[5,0],29:[6,0]}

convert = [0,"ari","tua","gem","can","leo","vir","lib","sco","sag","cap","aqu","pis"];

def Aspects(xpts,ypts,orbs):
    #get the zodiac deg of planet and add its deg
    x_zodiac_deg = zodiac[xpts['sign']] + xpts['deg']#ven 270 + 25 = 295
    y_zodiac_deg = zodiac[ypts['sign']] + ypts['deg']#sat 180 + 21 = 201
    
    #subtract yplanet from yplanet to get aspect point
    aspt = abs(x_zodiac_deg - y_zodiac_deg) #94
    
    #print(f'sun = {x_zodiac_deg}, moon = {y_zodiac_deg} and pts = {aspt}')
    
    aspects_tuple = ((range(360 - orbs, 360 + orbs), 360 ,'conj'), (range(30 - orbs, 30 + orbs), 30, 'semisex'),
                 (range(45 - orbs, 45 + orbs), 45, 'semisq'),(range(60 - orbs, 60 + orbs), 60, 'sex'),
                 (range(90 - orbs, 90 + orbs), 90, 'sqr'), (range(120 - orbs, 120 + orbs), 120, 'tri'),
                 (range(135 - orbs, 135 + orbs), 135, 'sesq'), (range(150 - orbs, 150 + orbs), 150, 'inc'),
                 (range(180 - orbs, 180 + orbs), 180, 'opp'),(range(210 - orbs, 210 + orbs), 210, 'inc_e'),
                 (range(225 - orbs, 225 + orbs), 225, 'sesq_e'), (range(240 - orbs, 240 + orbs), 240, 'tri_e'),
                 (range(270 - orbs, 270 + orbs), 270, 'sqr_e'), (range(300 - orbs, 300 + orbs), 300, 'sex_e'),
                 (range(315 - orbs, 315 + orbs), 315, 'semisq_e'),(range(330 - orbs, 330 + orbs), 330, 'semisex_e'))


    
    #find it in aspects tuple
    for aspt_tup, num, name in aspects_tuple:
        if aspt in aspt_tup:
            #print(f'if {aspt} in {aspt_tup}')
            
            #findout if its applying or separating
            app_sep = aspt - num
            result = (name, app_sep)
            break
        
        '''testing inside'''
        #else:
        #    print(f'if {aspt} in {aspt_tup}')
    else:
        result = (0, 0)   
    
    return result

#when calling, add 1 to your orbs to accomodate 0 degree
#print(Aspects(nat['sun'], nat['mon'], 4))

discord_aspts = ['semisqr', 'sqr', 'opp']
harmony_aspts = ['semisex', 'sex', 'tri']
connection_aspts = ['conj', 'sesq', 'inc']
tumb_aspts = ['semisqr', 'sesq']
tumb_sign = [11, 2, 5, 8]

class Vedic(object):
    '''vars'''
    def __init__(self, natal, transit):
        self.nat = natal
        self.transit = transit
        
    def vedicpt(self, planet):
        #get the west deg
        w_deg = self.nat[planet]['deg'] #ven = 25
        #convert to vedic
        w2v = west_to_vedic[w_deg] # [2, -1]
        
        #since it is in another sign so (sign - 1)
        
        return (w2v[0], self.nat[planet]['sign'] + w2v[1])
    
    
    def in_house(self, wplanet, xpts):
        #get the sign num of planet and convert num to str
        a_planet_pt = convert[wplanet[xpts]['sign']] #cap
        
        #call it in the moons house
        mon_asc = convert[self.vedicpt('mon')[1]] #cap - so the moon begins from cap
        
        #then call cap(planet pt) from cap(mon asc)
        w_planet_deg = eval(mon_asc)[a_planet_pt] #60 = pis western, so we need to - 23
        
        #planet_deg = abs(w_planet_deg - 23)
        planet_deg = w_planet_deg + wplanet[xpts]['deg']
        print(f'planet_deg = {planet_deg} as w_planet_deg = {w_planet_deg}')
        
        #convert the deg to vedic
        #w2v_deg = self.vedicpt(nat[xpts]['syb'])  #[2, -1]            
        #print(f'w2v_deg = {w2v_deg}')
        
        #add to planet deg
        vpt_deg = planet_deg - 23 #w2v_deg[0] #60 + 2
        #print(f'vpt_deg = {vpt_deg}')
        h_tuple = (
                    (range(0, 29),'h1'),(range(30, 30 + 29), 'h2'),(range(60, 60 + 29), 'h3'),
                    (range(90, 90 + 29), 'h4'), (range(120, 120 + 29), 'h5'), (range(150, 150 + 29), 'h6'),
                     (range(180, 180 + 29), 'h7'),(range(210, 210 + 29), 'h8'), (range(240, 240 + 29), 'h9'),
                     (range(270, 270 + 29), 'h10'), (range(300, 300 + 29), 'h11'),(range(330, 330 + 29), 'h12'),
                    
            '''
                    (range(360, 360 + 29),'h1'),(range(30, 30 + 29), 'h2'),(range(60, 60 + 29), 'h3'),
                    (range(90, 90 + 29), 'h4'), (range(120, 120 + 29), 'h5'), (range(150, 150 + 29), 'h6'),
                     (range(180, 180 + 29), 'h7'),(range(210, 210 + 29), 'h8'), (range(240, 240 + 29), 'h9'),
                     (range(270, 270 + 29), 'h10'), (range(300, 300 + 29), 'h11'),(range(330, 330 + 29), '12'),
                     '''
                     )


        
        #find it in house tuple
        for h_tup, name in h_tuple:
            if vpt_deg in h_tup:
                result = name
                break 
        
        return result
    
    def house(self):
        print(convert[self.vedicpt('mon')[1]])
        #self.house_dict = ((range(vedicpt('mon')-1, vedicpt('mon')),1), (), (), (), (), (), ())
    
    def __str__(self):
        return f'self.nat is {self.transit}'

moon = Vedic(nat, prog)
#print(moon.vedicpt('mon'))
print(moon.in_house(transit,'sat'))



def judge(xpts,ypts,orbs):
    #sun moon relationship
    connection = Aspects(xpts,ypts,orbs)[0] #('sqr', 1) or (0, 0)
    if connection in ['conj', 'semisex', 'semisqr', 'sex', 'sqr', 'tri', 'sesq', 'inc', 'opp']:
        reading = sunMon['light']
    else:
        reading = sunMon['dark']

    contact = Aspects(xpts,ypts,orbs)[0]
    if contact in ['conj', 'semisqr', 'sqr', 'sesq', 'opp']:
        nextReading = sunMon['afflicted']
    elif connection in ['conj', 'semisex', 'sex', 'tri']:
        nextReading = 'good contact'
    else:
        nextReading = sunMon['no_contact']
        
    transit_now = Aspects(xpts,ypts,orbs)
    #print(f'transit_now = {transit_now}')
    if transit_now[0] in harmony_aspts:
        tnow = 'is Good times'
    else:
        tnow = 'take caution'
    
    return {'reading':reading, 'nextReading':nextReading, 'tnow':tnow}
    
#print(judge(nat['mec'], transit['sat'], 3)['reading'])



def star(planet):
    #get the western deg eg moon
    deg = planet['deg'] #11
    sign = planet['sign']
    
    #convert to vedic
    v_deg = west_to_vedic[deg][0] #
    print(f'v_deg = {v_deg}')
      
    v_pt = (v_deg, sign + west_to_vedic[deg][1])
    print(f'v_pt = {v_pt}')
    
star(nat['mon'])
    

"""
class VedicMoon(object):
    '''vars'''
    def __init__(self, planet):
        self.deg = planet['deg']
        self.sign = planet['sign']
        self.syb = planet['syb']
        
    def vedicpt(self):    
        #convert to vedic 
        return (west_to_vedic[self.deg][0], self.sign + west_to_vedic[self.deg][1])
    
    def house(self, plt):
    
    def __str__(self):
        return f'{self.syb} is {self.deg}'

moon = VedicMoon(nat['mon'])
print(moon.vedicpt())
"""
