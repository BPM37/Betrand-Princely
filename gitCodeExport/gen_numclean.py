
from dateofbirth import DateOfBirth

class CreateNumbersFor:
    
    def __init__(self, names, dob, whichYear): #princely okwuego, 22/02/1982, 2023
        self.names = names
        self.dob = dob
        self.whichYear = whichYear
        self.expressions = ExpressionFor(self.names)
        self.dobNum = DateOfBirth(dob, whichYear)
            
    
oracle = CreateNumbersFor('Princely Okwuego Emeka', '26/04/1992', 'forNow')
read = {4:'consolidate'}
#d = {'ReadExp':read[oracle.expression()], 'readSoulUrge':read[oracle.soulUrge()],
     #'PersonalYearNum':read[oracle.pathNum()['yearNum']['core']]}

#print(read[oracle.pathNum()['yearNum']['core']])

print(oracle.dobNum.lifePath()['yearNum'])


