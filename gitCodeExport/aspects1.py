def Aspects(xDeg,xSign,yDeg,ySign,orbs):
    xSignName = convert[xSign] #pis
    ySignName = convert[ySign] #aqu

    ySignDeg = eval(xSignName)[ySignName] #330

    xPt = 360 + xDeg;
    yPt = ySignDeg + yDeg;

    if yPt in range(360 - orbs,360 + orbs) and yPt < 360:
        r = "yes"
            #return "conj "+ " " + " S"
            
    elif yPt in range(60 - 8, 60 + 8):
        r = "sex"
        
    elif yPt in range(90-8,90+8):
        r = "sqr"
        
    elif  yPt in range(120-8,120+8):
        r = "trin"
        
    elif yPt in range(150 - 8, 150 + 8):
        r = "150"
    else:
        r = "opp"
        
    return r