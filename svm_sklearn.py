import glob
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import svm
import numpy as np
import cv2
import pickle



def create_batches():

      
      images = []
      labels = []
      count = 0
      img = []
      for im in glob.glob('/home/karan/Videos/ml_material/data/svm_kj_har/*.jpg'):
      
          i = cv2.imread(im)
          
          #i = cv2.cvtColor(i,cv2.COLOR_BGR2GRAY)
          #plt.imshow(i)
          #plt.show()
          #img.append(i)
          r = 28/i.shape[0]
          w = int(i.shape[1]*r)
          ir = cv2.resize(i,(28,28))
          #print(ir)
          #x = np.linspace(1,1,784)
          ir = ir.flatten()
          #plt.plot(ir,x,'o')
          #plt.show()
          images.append(ir)
          #count+=1
          if 'harnoor' in im:
          	labels.append(0)
          else:
          	labels.append(1)
      
      #plt.plot(images,labels)
      #plt.show()
      #images = np.array(images)
      #labels = np.array(labels)
      return images,labels












x,y = create_batches()
#x = x.reshape(-1,1)
#print(x)

#np.squeeze(x,axis = 0).shape
#print(x.ndim,y.ndim)
clf = svm.SVC(gamma = 0.0001,C = 100)
clf.fit(x,y)
with open('svm.pickle','wb') as f:
     pickle.dump(clf,f)
#i = cv2.imread('/home/karan/Videos/ml_material/data/svm_kj_ab/abhay1.jpg',cv2.IMREAD_GRAYSCALE)
#data = cv2.resize(i,(28,28))
#value = clf.predict(np.array(data).reshape(1,-1))
#print(value)

#plt.imshow(i)
#plt.show()
'''
with open('svm.pickle','rb') as f:
      clf2 = pickle.load(f)
cap=cv2.VideoCapture(0)
ret,img=cap.read()
cap.release()
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
data = cv2.resize(img,(28,28))
#print(clf2.predict(np.array(data).reshape(1,-1)))
value = int(clf2.predict(np.array(data).reshape(1,-1)))
print(value)
plt.imshow(img)
if value == 1:
      plt.title("Karan")
else:
      plt.title("Harnoor")
plt.show()
#acc = round(clf.score(x,y)*100,2)
#print(acc)
'''
