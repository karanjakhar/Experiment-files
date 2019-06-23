from sklearn import tree
from sklearn.ensemble import RandomForestClassifier


X = [[0,0],[0,1],[1,1]]
y = [0,0,1]

clf = tree.DecisionTreeClassifier(random_state = 0,criterion = 'entropy',max_depth = None)

clf.fit(X,y)
Rclf = RandomForestClassifier(n_estimators = 10,criterion = 'entropy',max_depth = None)
Rclf.fit(X,y)
print(clf.predict([[2,2]]),Rclf.predict([[2,2]]))

with open('tree.dot','w') as file:
    tree.export_graphviz(clf,out_file = file)
    
number = 5
def f():
 print(number)
def g():
 number = 3
 print(number)
 
def h():
 global number
 print(number)
 number = 3
f()
g()
g()
h()
h()
#5
#5
#5
#5
#3
