import matplotlib.pyplot as plt
def readPoweballData(filepath):
    dataSet=[]
    try:
        fileObj=open(filepath,"r")
        for line in fileObj:
            rawList=line.strip()
            dataSet.append([int(rawList[0]),int(rawList[1]),int(rawList[2]),int(rawList[3]),int(rawList[4]),int(rawList[5]),rawList[6]])
    except Exception as err:
        print(f"Error {err} with file: {filepath}")
        return None
    return dataSet
def displayPoweballNumberFrequencies(filepath):
 pd=readPoweballData(filepath)
 pdLists=[]
 for i in range(1,27):
    pdLists.append([item for item in pd if item[5]==i])
 pdListSize=[]
 for i in range(1,27):
    pdListSize.append([len(pdLists[i-1]),i])
 plt.bar([row[1] for row in pdListSize],[row[0] for row in pdListSize])
 pdListSize.sort(reverse=True)
 print(f"The most common powerball number is: {pdListSize[0][1]} happening {pdListSize[0][0]} times")
 plt.show()
displayPoweballNumberFrequencies("D:\PowerballData.csv")