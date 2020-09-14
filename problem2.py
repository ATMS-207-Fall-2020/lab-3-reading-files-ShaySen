### PROBLEM 2

def main():
    filename= 'Aug2020_Champaign_Temperature_Dewpoint.csv'
    date= '2020-08-08'

    with open(filename, "r") as f: 
      alist =f.read().splitlines()

      for line in alist:
        #print(line)
        d=line.split(',')[0]
        if d == date: 
          #print(line)
        #this print includes the date with the data
          print(line.split(',')[1],line.split(',')[2],line.split(',')[3])
       #This is the data for the date without the date:
       

if __name__ == "__main__":
    main()