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





