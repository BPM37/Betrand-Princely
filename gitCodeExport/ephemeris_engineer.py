from __future__ import print_function, division

import datetime

start_date = datetime.date(2023, 7, 19)
start_time = ('17 54') #UT/GMT

start_ephem = { 'asc':{'deg':16,'sign':9,'min':15,'syb':"A"},
        'sun':{'deg':26,'sign':4,'min':49.12,'syb':"sun"},
        'mon':{'deg':18,'sign':5,'min':29.41,'syb':"mon"},
                
        #'mec':{'deg':6,'sign':11,'min':40,'syb':"mec"},
        #'ven':{'deg':25,'sign':10,'min':41,'syb':"ven"},
        #'mars':{'deg':19,'sign':7,'min':10,'syb':"mas"},
        #jup:{deg:10,sign:8,min:19,syb:"jup"},
        #'sat':{'deg':21,'sign':7,'min':50,'syb':"sat"},
        #'ura':{'deg':4,'sign':9,'min':30,'syb':"ura"},
        #nep:{deg:26,sign:9,min:41,syb:"nep"},
        #plu:{deg:26,sign:7,min:46,syb:"plu"},
        #nod:{deg:21,sign:4,min:56,syb:"nod"},
        #pat:{deg:8,sign:10,min:15,syb:"pat"},
     }

                        #(yyyy, mm, day)
next_date = datetime.date(2023, 2, 5)

n_days = abs((next_date - start_date).days) #- or +

print(f'num of days = {n_days}')

#one Month
next_sun_deg = n_days + start_ephem['sun']['deg'] #31 + 26 = 57
print(f'next_sun_deg = {next_sun_deg}')

#divide by 30 to get the signs
next_sign = next_sun_deg // 30

#get the remainder which is the deg
#rem = next_sun_deg % 30
rem = (next_sign * 30) - next_sun_deg

#Two Years
#num_of_rev = n_days % 360 #762 % 360 = 42
print(f'next_sign = {next_sign}, rem = {next_sign}')

next_sun_deg = rem + start_ephem['sun']['deg'] #31 + 26 = 57
print(f'rem + start_ephemsundeg = {next_sun_deg}')

if next_sun_deg > 30:
    print(f'next_sun_deg > 30')
    s_deg = next_sun_deg - 30
    s_sign = (start_ephem['sun']['sign'] - 1) + next_sign
else:
    s_deg = next_sun_deg
    s_sign = (start_ephem['sun']['sign'] - 1) + next_sign
    
print(f'({s_deg}, {s_sign})')