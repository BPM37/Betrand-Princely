#import pandas as pd
#import numpy as np

#from flask import Blueprint, redirect, render_template, request, url_for

from num_defineUP1 import ExpressionFor, DateOfBirth

import collections
from collections import OrderedDict

class CreateNumbersFor:
    
    def __init__(self, names, dob, whichYear): #princely okwuego, 22/02/1982, 2023
        self.names = names
        self.dob = dob
        self.whichYear = whichYear
        self.expressions = ExpressionFor(self.names)
        self.dobNum = DateOfBirth(dob, whichYear)
            
    
    ##########going for expression or desiney number #{'expr': (0, 22), 's_urge': (0, 6), 'imager': (16, 7)}
    '''
    def nameDict(self):
        general = self.expressions.forFirstName()
        exp = general['expr']['core']
        expKarma = general['expr']['karma']
    '''
    
    def expression(self):
        expr = self.expressions.forFirstName()
        return expr['expr']['core']
    
    #is there karma in expr or desiney number
    def expressionKarma(self):
        expr = self.expressions.forFirstName()
        return expr['expr']['karma']
    

    ##########going for soul urge or heart desire number
    
    def soulUrge(self):
        sUrge = self.expressions.forFirstName()
        return sUrge['s_urg']['core']
    
    #is there karma in sUrge
    def soulUrgeKarma(self):
        sUrgeKarma = self.expressions.forFirstName()
        return sUrgeKarma['s_urg']['karma']
    
    
    
    ##########going for image or personality number
    def imageNum(self):
        imageN = self.expressions.forFirstName()
        return imageN['imager']['core']
    
    #is there karma in image
    def imageKarma(self):
        imageK = self.expressions.forFirstName()
        return imageK['imager']['karma']

    #s_urge and personality brigde
    def soulUrgeImageBrig(self):
        urge = self.soulUrge()
        img = self.imageNum()
        return abs(urge - img)

    #{'lifePath': {'core': 8, 'coreKarma': 0}, 'subelem': 0, 'yearNum': {'core': 4, 'coreKarma': 13}}
    def pathNum(self):
        lp = self.dobNum.lifePath()
        return lp
    
    #Your Life Path - Expression Bridge
    def LPEBrig(self):
        #Your Life Path - Expression Bridge
        return abs(self.pathNum()['lifePath']['core'] - self.expression())
    
oracle = CreateNumbersFor('Okwuego Emeka', '26/04/1992', 'forNow')
read = {4:'consolidate'}
#d = {'ReadExp':read[oracle.expression()], 'readSoulUrge':read[oracle.soulUrge()],
     #'PersonalYearNum':read[oracle.pathNum()['yearNum']['core']]}

print(read[oracle.pathNum()['yearNum']['core']])


