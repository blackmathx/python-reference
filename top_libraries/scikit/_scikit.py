'''
SciKit-Learn is a robust library for machine learning in Python that provides tools for machine learning and 
statistical modleing including classificaiton, regression, clustering, and dimensionality reduction. Open Source, built
on NumPy, SciPy, and Matplotlib.

https://scikit-learn.org


'''

from sklearn import datasets
from sklearn import preprocessing
import numpy as np
import matplotlib.pyplot as plt

# scikit-learn has 'toy' datasets and digit datasets for easy importing

# loading a  preexisting smaple dataset
digits = datasets.load_digits()
features = digits.data
target = digits.target
print(features[1])  
print(features[2].size) # looks like array of 115008 arrays which are 64 long

# toy diabetes data
diabetes = datasets.load_diabetes()
print(diabetes.DESCR)
print(diabetes.data)

# generate features matrix target vector and the true coefficients
features, target, coefficients = datasets.make_regression(n_samples = 100,
                                                          n_features = 3, 
                                                          n_informative = 3,
                                                          n_targets = 1, 
                                                          noise = 0.0,
                                                          coef = True, 
                                                          random_state = 1)

# view feature matrix and target vector
print('Feature Matrix\n', features[:3])
print('Target Vector\n', target[:3])

# plot the data with matplotlib
plt.scatter(features[:, 0], features[:, 1], c=target)
plt.show()

# also able to generate for classification or clustering

##############################################################

# Feature Scaling of quant data. Common technique
feature = np.array([[-500.5],
                    [-100.1],
                    [0],
                    [100.1],
                    [900.9]])
minmax_scale = preprocessing.MinMaxScaler(feature_range=(0,1))
scaled_feature = minmax_scale.fit_transform(feature)
print('Scaling data between min and max:\n', scaled_feature)


# Feature Scaling to have a mean of 0 and standard deviation of 1. An alternative to min-max scaling. If there are 
# significant outliers it can negatively impact our standardization, so it  is helpful to rescale the feature using 
# the median and quartile range - in sklearn we do this using the RobustScalar
some_feature = np.array([[-100], [234], [500.5], [600.6], [9000.9]])
scaler = preprocessing.StandardScaler()
standardized = scaler.fit_transform(some_feature)
print('Standardized Feature:\n', standardized)
print('Mean: ', round(standardized.mean()))
print('Std: ', standardized.std())

