class MoonChart:
    def __init__(self, natal, transit):
        self.natal = natal
        self.transit = transit
        self.sun = natal['sun']
        self.mon = natal['mon']
        self.tsat = transit['sat']
        self.house = ''
        self.sign = ''
        self.zodiac = {1:360, 2:30, 3:60, 4:90, 5:120, 6:150, 7:180, 8:210, 9:240, 10:270, 11:300, 12:330}
        self.elements_tup = (
                    (range(0, 30), 'F', 'cadinal', 'AR'), (range(120, 150), 'F', 'fixed', 'LE'),
                    (range(240, 250), 'F', 'mutable', 'SG'),(range(270, 300),'E','cadinal','CP'),
                    (range(30, 60),'A','fixed','TA'), (range(150, 180),'A','mutable','VI'),
                    (range(180, 210),'A','cadinal','LI'), (range(300, 330),'A','fixed','AQ'),
                    (range(60, 90),'A','mutable','GE'),(range(90, 120),'W','cadinal','CN'),
                    (range(210, 240),'W','fixed','SC'), (range(300, 360),'W','mutable','PI'),
                     )
        
    def __repr__(self):
        return "('A', 'fixed', 'AQ')"
        
    def elementOf(self, planet):
        
        #{'deg':3,'sign':12,'min':3,'syb':"sun"}
        planet_deg, planet_sign = self.sun['deg'], self.sun['sign'] #12
        
        #get the western zodiac point
        w_planet_pt = self.zodiac[planet_sign] + planet_deg #330 pi

        
        #convert to vedic
        vpt = w_planet_pt - 23 # 333 - 23 = 310
        #print(f'{w_planet_pt} {vpt}')
        for range_pt, elem, tripc, psign in self.elements_tup:
            if vpt in range_pt:
                result = (elem,tripc,psign)
                break
        
        #print(f'{natpt}')
        return result
        
    def houseOf(self, planet):
        pass
    
    def signOf(self, planet):
        pass
    
    def aspectsOf(self, planet):
        pass
    
    def transitInHouse(self, planet):
        pass
    
    def transitInSign(self, planet):
        pass





planets = {
            'sun':{'deg':3,'sign':12,'min':3,'syb':"sun"},
            'mon':{'deg':11,'sign':11,'min':3,'syb':"mon"},
            }
tsit = { 
        'sun':{'deg':14,'sign':1,'min':3,'syb':"sun"},
        'mon':{'deg':25,'sign':5,'min':3,'syb':"mon"}, #to the inner world measurement
        'sat':{'deg':5,'sign':12,'min':3,'syb':"sat"}
        }

oracle = MoonChart(planets, tsit)
print(oracle)
print(oracle.elementOf('sun'))