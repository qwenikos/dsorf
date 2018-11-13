
def readConfigFile(configFileName):
    configFile=open(configFileName,"r")
    confDict={}
    for aLine in configFile:
        cols=aLine.rstrip().split("=")
        if len(cols)==2:
            confDict[cols[0]]=cols[1].replace("'","").replace('"',"")
    return confDict

def truncate(number, digits):
    import math
    number=float(number)
    stepper = pow(10.0, digits)
    return math.trunc(stepper * number) / stepper
