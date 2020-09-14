### PROBLEM 1

def main():
    filename='aravg.ann.land_ocean.90S.90N.v5.0.0.202007.asc'
    filedata = {'year': [], 'temperature': []} 
    TY= {}
    with open(filename, "r") as f: 
      alist =f.read().splitlines()
      
      #Method 1 for-each
      for line in alist:
        #print(line)
        filedata['year'].append(int(line.split( )[0]))
        filedata['temperature'].append (float(line.split( )[1]))
        TY[float(line.split( )[1])]= int(line.split( )[0])
    
      ListTemp= (sorted (filedata['temperature'],reverse=True))
      ListTemp= ListTemp[:10]
    
      for Temps in ListTemp:
        print(Temps,TY[Temps])
      #ANSWER:
#0.719495 2020
# 0.683394 2016
# 0.637247 2019
# 0.617925 2015
# 0.598438 2017
# 0.515222 2018
# 0.428476 2014
# 0.413727 2010
# 0.363765 2013
# 0.35654 2005

      #print(alist[2].split( )[0])
   


if __name__ == "__main__":
    main()