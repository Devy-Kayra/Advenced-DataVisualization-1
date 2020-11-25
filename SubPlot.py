import matplotlib.pyplot as plt

x = [1 , 2 , 3 , 4 , 5 , 6]
y = [10 , 20 , 30 , 40 , 50 , 60]
z = [20 , 30 , 40 , 50 , 60 , 70]

plt.subplot(2 , 2 , 1) # we seperate 2 part and we select first part
plt.plot(x , y) # we create on first part

plt.subplot(2 , 2 , 2) # we select seconda part
plt.bar(x , z) # we create on second part

plt.show()
