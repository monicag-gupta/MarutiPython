1. Line Chart : Display trends or changes over continuous intervals (e.g., time). Use Case: Stock prices, temperature change over time. Function: plt.plot(x, y)
2. Bar Chart : Compare quantities across different categories. Use Case: Sales by region, survey results. Function: plt.bar(x, height)
3. Histogram : Show distribution of numeric data. Use Case: Age distribution, test scores. Function: plt.hist(data, bins=number)
4. Pie Chart : Show proportions of a whole. Use Case: Market share, budget breakdown. Function: plt.pie(sizes, labels=labels)
5. Scatter Plot : Show relationship or correlation between two numeric variables. Use Case: Height vs. Weight, sales vs. advertising. Function: plt.scatter(x, y)
6. Box Plot (Box-and-Whisker Plot) : Show data distribution using five summary statistics. Use Case: Examining outliers, comparing distributions. Function: plt.boxplot(data)
7. Area Chart : Like a line chart but filled with color to represent volume. Use Case: Accumulated values over time. Function: plt.fill_between(x, y)
8. Stacked Bar Chart : Show parts of categories across different groups. Use Case: Sales by product lines over quarters. Function: plt.bar(..., bottom=...)
9. Heatmap (via seaborn or imshow) : Represent matrix values with color intensity. Use Case: Correlation matrix, grid-based data. Function: plt.imshow(data, cmap='hot')
10. Error Bar Plot : Show variability of data using error bars. Use Case: Scientific experiments, averages with uncertainty. Function: plt.errorbar(x, y, yerr=errors)
11. Stem Plot : Useful for discrete signal representation. Use Case: Signal processing, digital sampling. Function: plt.stem(x, y)
12. Step Plot : Display data with sudden changes (discrete steps). Use Case: Digital signal, decision boundaries. Function: plt.step(x, y)
13. Polar Plot : Display data in circular coordinates. Use Case: Wind direction, radar. Function: ax = plt.subplot(projection='polar')
14. 3D Plots : Visualize three-dimensional data. Use Case: Surface plots, 3D scatter. Function: Use mpl_toolkits.mplot3d



pip install matplotlib
pip install scikit-learn
pip install seaborn







#####


# Histograms are used to show the distribution of a dataset. It divides the data into bins and shows the frequency of data points in each bin.

import matplotlib.pyplot as plt
import numpy as np

# Generating random data
data = np.random.randn(1000)
# Generates 1000 random values from a standard normal distribution (mean=0, std=1).

# Plotting a histogram # Creates a histogram with 30 bins.
plt.hist(data, bins=30, color='skyblue', edgecolor='black')

# Adding titles and labels
plt.title('Histogram of Random Data')
plt.xlabel('Value')
plt.ylabel('Frequency')

# Displaying the plot
plt.show() # The plot is displayed using plt.show().




#####

# Bar charts are used to display categorical data and are typically used to compare values across different categories.

import matplotlib.pyplot as plt

# Data for the bar chart
categories = ['A', 'B', 'C', 'D', 'E']
values = [23, 45, 56, 78, 33]

# Plotting a bar chart
plt.bar(categories, values, color='lightgreen')
# Plots the bars using the given categories and their corresponding values.

# Adding titles and labels
plt.title('Bar Chart Example')
plt.xlabel('Categories')
plt.ylabel('Values')

# Displaying the plot
plt.show()

# You can customize the chart by setting colors, adding titles, and adjusting labels.


########

# Scatter plots are used to display the relationship between two continuous variables.

import matplotlib.pyplot as plt
import numpy as np

# Generating random data. Generates 50 random values between 0 and 1.
x = np.random.rand(50)
y = np.random.rand(50)
print(f"x:\n{x}\ny:\n{y}")

# Plotting a scatter plot. Plots the data as points on a scatter plot.
# alpha=0.7 means the points will be 70% opaque, so they are somewhat transparent.
plt.scatter(x, y, color='red', alpha=0.7)

# Adding titles and labels
plt.title('Scatter Plot Example')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Displaying the plot
plt.show()





######

# Box plots (or box-and-whisker plots) are useful for visualizing the spread and skewness of data, showing the median, quartiles, and outliers.

import matplotlib.pyplot as plt
import numpy as np

# Generating random data
data = np.random.randn(100)
print(data)

# Plotting a box plot
plt.boxplot(data, vert=False)
# Creates a box plot of the data. Vertical=false.
# The horizontal lines in the box plot represent the median, while the box shows the interquartile range (IQR).

# Adding titles and labels
plt.title('Box Plot Example')
plt.xlabel('Value')

# Displaying the plot
plt.show()





#####

# Heatmaps are used to represent matrix-like data where values are encoded as colors. This is useful when visualizing correlations between variables or patterns in large datasets.

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Generating random data
data = np.random.rand(10, 10)
print(data)

# Plotting a heatmap. 
sns.heatmap(data, annot=True, cmap='YlGnBu')
# Creates the heatmap using seaborn (which is built on top of matplotlib).
# cmap='YlGnBu': Specifies the color map
# annot=True: Annotates the heatmap cells with values.

# Adding titles and labels
plt.title('Heatmap Example')

# Displaying the plot
plt.show()




####

# Pair plots are used to visualize relationships between all pairs of variables in a dataset.

import seaborn as sns
import pandas as pd
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

# Loading Iris dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['Species'] = iris.target
pd.set_option('display.max_columns', None); pd.set_option('display.max_rows', None)
print(df)
pd.reset_option('display.max_columns'); pd.reset_option('display.max_rows')

# Plotting a pair plot
sns.pairplot(df, hue='Species', palette='coolwarm')
# Creates a pair plot for the dataset
# hue='Species': This argument will color the data points by the 'Species' column in the DataFrame, allowing you to visualize how the data points from different species are distributed across the scatter plots.
# palette='coolwarm': This specifies the color palette to be used for the hue. The 'coolwarm' palette is a gradient of colors from blue (cool) to red (warm).

# Displaying the plot
plt.show()








