import matplotlib.pyplot as plt
def readfileData():
    filePath=input("Entere the data file path-->")
    try:
     fileObject=open(filePath,"r")
    except :
      print(f"Error with file:'{filePath}'! Invalid file path or name.")
    else:
      ycroods=[]
      list1=[]
      list2=[]
      monthsNames=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
      for line in fileObject:
       sline=line.split(',')
       month=str(sline[0])
       amount=float(sline[1])
       list1=[month,amount]
       list2.append(list1)
      for m in range(len(monthsNames)):
        eachMonth=[item for item in list2 if item[0]==monthsNames[m]]
        for j in range (len(eachMonth)):
          eachMonthNumber=[item[1] for item in eachMonth ]
          eachMonthAverage=sum(eachMonthNumber)/len(eachMonthNumber)
        ycroods.append(eachMonthAverage)
      xcroods=[item for item in monthsNames]
      plt.bar(xcroods,ycroods)     
      plt.show()
    
readfileData()
