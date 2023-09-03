
planets = {
            'sun':{'deg':3,'sign':12,'min':3,'syb':"sun"},
            'mon':{'deg':11,'sign':11,'min':3,'syb':"mon"},
            }
tsit = { 
        'sun':{'deg':14,'sign':1,'min':3,'syb':"sun"},
        'mon':{'deg':25,'sign':5,'min':3,'syb':"mon"}, #to the inner world measurement
        }


zodiac = {1:360, 2:30, 3:60, 4:90, 5:120, 6:150, 7:180, 8:210, 9:240, 10:270, 11:300, 12:330}


elements = ( (range(0, 30), 'F', 'cadinal', 'AR'), (range(120, 150), 'F', 'fixed', 'LE'), (range(240, 250), 'F', 'mutable', 'SG'),
             (range(270, 300),'E','cadinal','CP'), (range(30, 60),'A','fixed','TA'), (range(150, 180),'A','mutable','VI'),
             (range(180, 210),'A','cadinal','LI'), (range(300, 330),'A','fixed','AQ'), (range(60, 90),'A','mutable','GE'),
             (range(90, 120),'W','cadinal','CN'), (range(210, 240),'W','fixed','SC'), (range(300, 360),'W','mutable','PI'),
             )

class Universe:
    #def __init___(self, elements, planets):
        #self.elements = elements
        #self.planets = planets
    #    pass
    
    def state_of_planet(self, planet):
        
        natpt = planets[planet] #{'deg':3,'sign':12,'min':3,'syb':"sun"}
        natplanetdeg = natpt['deg'] #3
        natplanetsign = natpt['sign'] #12
        
        #get the zodiac point
        w_planet_pt = zodiac[natplanetsign] + natplanetdeg #330 pi

        
        #convert to vedic
        vpt = w_planet_pt - 23 # 333 - 23 = 310
        #print(f'{w_planet_pt} {vpt}')
        for range_pt, elem, tripc, psign in elements:
            if vpt in range_pt:
                result = (elem,tripc,psign)
                break
        
        #print(f'{natpt}')
        return result
                

horoscope = Universe()
print(horoscope.state_of_planet('sun'))
horoscope.state_of_planet('mon')
