
Python Package that performs Exploratory Data Analysis

#### exploredata is built on Pandas and Numpy. It gives an overview of a csv data file.
 - It imports csv file and returns the summary of the data in the file using the Pandas Dataframe.info() function.
 - It contains method (**null_cat and null_num**) that returns the number of missing categorical and numerical features respectively
 - It also has method that returns the number of numerical and categorical features as well the number of features containing outliers
 - It also contains method (**num_viz and cat_viz**) that plot histogram and boxplot for each numerical variable as well as the count plot for each categorical variables.

## Installing

pip install exploredata

## Usage

- **import exploredata as ep**   *#imports the exploredata package*

- **new_variable = ep.EDA(file path)**  *#calls the EDA module in the package. The module import your csv file and assign it as a pandas dataframe to the variable 'train'. It also returns the summarry of the data*
- **new_variable.df**  *#prints the pandas dataframe*   
- **new_variable.num_var()**      *#returns a tuple containing the number and the list of numerical variables in the dataframe*
- **train.null_var()**  *#returns a tuple containing the number and the list of numerical variables containing null values*
- **help(ep.EDA)**  *#provide information on all methods defined in the EDA module*


