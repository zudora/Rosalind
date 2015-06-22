class my_class(object):
    
    def build_comp(inString):
        outString = ""
        for index in range(0, len(inString)):
            if inString[index] == "A":
                outString += "T"
            elif inString[index] == "T":
                outString += "A"
            elif inString[index] == "C":
                outString += "G"
            else:
                outString += "C"            
        
        return outString

    startString = "CCAGATC"
    complement = build_comp(startString)
    reversed = complement[::-1]
    print reversed
