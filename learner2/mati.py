from pylab import figure, axes, pie, title, show
import matplotlib.pyplot as plt
import numpy as np
fig = figure(1, figsize=(6, 6))
# Make a square figure and axes
ax = axes([0.1, 0.1, 0.8, 0.8])

labels = 'Thinking', 'Resoning', 'Programmimg','Analytical skills'
fracs = [15, 30, 45, 10]

explode = (0, 0.05, 0, 0)
pie(fracs, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True)
title('Learner rating', bbox={'facecolor': '0.8', 'pad': 5})
fig.savefig('/home/unknown/Djangoweb/Django.1.8.5/learner2/foo.png') 
show() 
