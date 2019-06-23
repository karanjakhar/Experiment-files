
import pandas as pd

pf = pd.DataFrame()
print(pf)

data = [1,2,3,4,5]
pf = pd.DataFrame(data)
print(pf)

data = [['A',1],['B',2],['C',3],['D',4],]
pf = pd.DataFrame(data,columns=['Name','Number'],dtype = float)
print(pf)


data = {'NO':[1,2,3,4],'Name':['A','B','C','D'],'Number':[1,2,3,4],}
pf = pd.DataFrame(data)
print(pf)

data = {'NO':[1,2,3,4],'Name':['A','B','C','D'],'Number':[1,2,3,4],}
pf = pd.DataFrame(data,index = ['a','b','c','d'])
print(pf)

data = [ {'a':1.5,'b':2.5},{'a':4.5,'b':5.5,'c':1.23}]
pf = pd.DataFrame(data,index = ['first','second'])
print(pf)









