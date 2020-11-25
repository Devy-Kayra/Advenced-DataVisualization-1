import matplotlib.pyplot as plt

slices = [120 , 80 , 140] # we create the degree of slices
labelList = ["Label 1" , "Label 2" , "Label 3"] # we add label according to the index
plt.pie(slices , labels = labelList) # we create graphic with slices and labels

plt.show()
