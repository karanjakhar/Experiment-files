import cv2
import numpy as np

im = np.array([[100,100,100,100],[255,255,255,255],[0,0,0,0],[255,255,255,255]])
cv2.imshow('kj',im)
cv2.waitKey(0)
cv2.destroyAllWindows()
