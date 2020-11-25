import matplotlib.pyplot as plt

# Wedge Properties
wp = {"linewidth" : 2 , "edgecolor" : "Black"}

# Explode Value
explode = (0.1, 0.0, 0.2) 

slices = [120 , 80 , 140]
labelList = ["Label 1" , "Label 2" , "Label 3"]
plt.pie(slices , labels = labelList , wedgeprops= wp ,explode= explode , colors = ["Black" , "DeepPink" , "Crimson"] , shadow= True)

plt.show()

"""
Argument List
-------------
explode = divides the graph into parts by the desired value
wp = edge colors are used to adjust values ​​such as edge thickness.
colors = As the name suggests, it is used to color parts.
shadow = It adds a shadow effect to the pieces and also makes the more pieces more distinct.
"""
