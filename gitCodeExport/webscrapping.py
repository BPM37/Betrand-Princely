from __future__ import print_function, division
import requests
from bs4 import BeautifulSoup
import os
import csv

month_to_num = ('jan','feb','mar','apr','may','june','july','aug','sept','oct','nov','dec','post')

#print('length of month to num[1] = ',month_to_num[1]) #13
        #print('month to num[1] = ',month_to_num[1])

def convert_to_csv(month, yr):

    #Convert to csv
    astro_elements_csv = []
    with open(f'ephemeris/{yr}/{yr}_{month_to_num[month]}.txt', "r") as file: #ephemeris/1983/1983_feb.txt
        lines = file.readlines()
        for line in lines:
            if 'DATE' not in line and line != '\n':
                word_list = line.strip().split()
                astro_elements_csv.append(word_list)


    with open(f'ephemeris/{yr}/{yr}_{month_to_num[month]}.csv',"w") as astro_elements_to_csv:
        writer = csv.writer(astro_elements_to_csv)
        #writer.writerow(['DATE','SID.TIME','SUN','MOON','MERCURY','VENUS','MARS','JUPITER','SATURN','URANUS','NEPTUNE','PLUTO','NODE'])
        writer.writerows(astro_elements_csv)


    '''Delete the text file'''
    os.remove(f'ephemeris/{yr}/{yr}_{month_to_num[month]}.txt')


def create_ephemeris(yr):
    """Downloads the ephemeris and process the file and save it as csv"""

    #saving the file so if the directory is not we creat it
    if not os.path.exists(f'ephemeris/{yr}'):
        os.mkdir(f'ephemeris/{yr}')

    #print('Calling URL ...')
    url = f'https://www.findyourfate.com/astrology/ephemeris/{yr}.html'

    """
    '''For testing '''
    print('Calling URL ...')
    url = f'http://127.0.0.1:5000/transit/scrap'
    """


    #using beautiful soup
    try:
        
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "html.parser")
        astro_ele = soup.find_all('pre')

        ele_list = []
        for ele in astro_ele:
            #we extract each element to a list, but years 2021 first element contains all the elem and 1982 is normal
            ele_list.append(ele.get_text())
        
        n = 0
        while n != len(month_to_num) - 1:
            with open(f'ephemeris/{yr}/{yr}_{month_to_num[n]}.txt', "w") as file:
                file.write(ele_list[n])
                n += 1

    
    except Exception as e:
        return "Connection failed due to {}".format(e)

    n = 0
    while n != len(month_to_num) - 1:
        convert_to_csv(n, yr)
        n += 1


#print(create_ephemeris(1985))