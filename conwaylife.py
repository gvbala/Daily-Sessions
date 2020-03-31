import numpy as np 
import collections
from matplotlib import animation, rc
import matplotlib.pyplot as plt

#np.random.seed(15)
siza = 20
sizb = 20
init_arr = np.random.randint(2,size=(siza,sizb))

a = init_arr
#print("INIT = ", init_arr[:,:])
#print("A Shape = ", np.shape(a))

count = 1
while count < 10:
    print("ITER = ", count)
    a = np.dstack((a,np.zeros((siza,sizb))))
    #print("New A Shape = ", np.shape(a))
    for i in range(np.shape(init_arr)[0]):
        for j in range(np.shape(init_arr)[1]):
            if i != 0 and i != np.shape(init_arr)[0]-1 and j != 0 and j != np.shape(init_arr)[1]-1:
                temp = np.ravel(a[i-1:i+2,j-1:j+2,count-1])
                temp = np.delete(temp, 4)
                counter = collections.Counter(temp)
                #print("TEMP = ", temp)
                #print("Count = ", counter[1])
                if counter[1] < 2 or counter[1] > 3:
                    a[i,j,count] = 0
                elif counter[1] == 3:
                    a[i,j,count] = 1
            elif i == 0:
                if j == 0:
                    temp = np.ravel(a[i:i+2,j:j+2,count-1])
                    temp = np.delete(temp, 0)
                elif j == np.shape(init_arr)[1]-1:
                    temp = np.ravel(a[i:i+2,j-1:,count-1])
                    temp = np.delete(temp, 0)
                else:
                    temp = np.ravel(a[i:i+2,j-1:j+2,count-1])
                    temp = np.delete(temp,1)
                counter = collections.Counter(temp)
                #print("TEMP = ", temp)
                if counter[1] < 2 or counter[1] > 3:
                    a[i,j,count] = 0
                elif counter[1] == 3:
                    a[i,j,count] = 1
            elif i == np.shape(init_arr)[0]-1:
                if j == 0:
                    temp = np.ravel(a[i-1:,j:j+2,count-1])
                    temp = np.delete(temp, 3)
                elif j == np.shape(init_arr)[1]-1:
                    temp = np.ravel(a[i-1:,j-1:,count-1])
                    temp = np.delete(temp, 3)
                else:
                    temp = np.ravel(a[i-1:,j-1:j+2,count-1])
                    temp = np.delete(temp,4)
                counter = collections.Counter(temp)
                #print("TEMP = ", temp)
                if counter[1] < 2 or counter[1] > 3:
                    a[i,j,count] = 0
                elif counter[1] == 3:
                    a[i,j,count] = 1
    #print("ARR = ", a[:,:,count]) 
    count += 1

fig = plt.figure()
ax = plt.axes(xlim=(-1, siza), ylim=(-1, sizb))

for i in range(np.shape(a)[2]):
    x = np.arange(siza)
    y = np.arange(sizb)
    x, y = np.meshgrid(x,y)
    plt.scatter(x,y,c=a[x,y,i])
    plt.pause(0.5)

plt.show()