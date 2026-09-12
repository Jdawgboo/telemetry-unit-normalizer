FACTORS={('celsius','fahrenheit'):(9/5,32),('meters','centimeters'):(100,0)}
def convert(value:float,source:str,target:str)->float:
 if source==target:return value
 factor,offset=FACTORS[(source,target)]
 return value*factor+offset
