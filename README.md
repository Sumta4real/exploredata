
Python Package that performs Exploratory Data Analysis

#### exploredata is built on Pandas and Numpy. It gives an overview of a csv data file.
 - It imports csv file and returns the summary of the data in the file using the Pandas Dataframe.info() function.
 - It contains method (null_cat and null_num) that returns the number of missing categorical and numerical features respectively
 - It also has method that returns the number of numerical and categorical features as well the number of features containing outliers
 - It also contains method (num_viz and cat_viz) that plot histogram and boxplot for each numerical variable as well as the count plot for each categorical variables.

## Installing

#conda
---
conda install exploredata


#pypi
---
pip install exploredata

