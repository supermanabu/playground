import matplotlib as plt
# Set the size of the plotting window. 
# MUST BE PUT BEFORE plt.plot() or plt.scatter()
# The figure() function controls the width, height, resolution 
#~and background color of the plot.
# The /figsize/ parameter takes a tuple, 
#~which tells matplotlib the dimensions of the plotting window in inches.
# The /dpi/ parameter (i.e. the system's resolution)
#~sets a plot size that makes effective use of the space available on your screen.
plt.figure(dpi=128, figsize=(10, 6))

# Option 1: plt.plot() to plot a line
# The /linewidth/ parameter controls the thickness of the line that plot() generates.
# The /label/ parameter labels the line.
plt.plot(x_values, y_values, linewidth=5, label='example')
# Option 2: plt.scatter() to plot discrete points
# The argument /s/ sets the size of the dots used to draw the graph.
# The argument /edgecolor='none' removes the outlines around points, 
#~which is the default - blue dots with a black outline.
# The argument /c/ changes the color of the points (c='red' or c=(0, 0, 0.8))
plt.scatter(x_values, y_values, s=40, edgecolor='none', c='red')
# Option 2.1: Using a Colormap: make smaller values a light color and larger values a darker color
plt.scatter(x_values, y_values, s=40, edgecolor='none', c=y_values, cmap=plt.cm.Blues)

# /fontsize/ controls the size of the text on the chart
plt.title("Square Numbers", fontsize=24)
# plt.xlabel() and plt.ylabel() allow you to set a title for each of the axes.
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# The function /tick_params()/ styles the tick marks.
# The argument /axes='both'/ enables affecting the tick marks on both the x- and y-axes.
# The argument /labelsize=14/ sets the font size of the tick mark labels to 14.
plt.tick_params(axis='both', labelsize=14)

# Set the range for each axis.
plt.axis([0, 1100, 0, 1100000])

# Remove the axes.
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)

# Legend
plt.legend(bbox_to_anchor=(0.188,0.993), loc="upper right", ncol=1, mode="None", borderaxespad=0, shadow=False, fancybox=True)

# plt.show() & plt.savefig()
# Option 1
plt.show()
# Option 2
# The argument /bbox_inches='tight'/ trims extra whitespace from the plot.
plt.savefig('mpl.png', bbox_inches='tight')

# Clear the current figure.
plt.clf()


# New

# Plot a horizontal line
plt.axhline(y=0.5, color='r', linestyle='-')
