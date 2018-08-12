#Promotable Project 4: Python | Taylor Alcantar

#For this project, I'm going to continue looking at the Chicago Airbnb dataset (renamed 'data'), that I began looking at in my SQL project.

# Import libraries

import numpy as np
import pandas as pd

# Open CSV file
df = pd.read_csv('data.csv')

# Describe Data

df.describe()

# Results
               price 	minimum_nights 	        number_of_reviews 	reviews_per_month 	calculated_host_listings_count 	availability_365
count 	6877.000000 	6877.000000 	        6877.000000 	    5992.000000 	          6877.000000 	            6877.000000
mean 	134.671659  	3.245310 	            30.439000 	        2.261869 	              6.270031 	                145.614076
std 	146.939220 	    11.334021 	            46.581891 	        2.943107 	              15.697111 	            128.653908
min 	0.000000 	    1.000000 	            0.000000 	        0.020000 	              1.000000 	                0.000000
25% 	60.000000 	    1.000000 	            3.000000 	        0.630000 	              1.000000 	                20.000000
50% 	99.000000 	    2.000000 	            12.000000 	        1.605000 	              1.000000 	                112.000000
75% 	150.000000 	    2.000000 	            38.000000 	        3.192500 	              4.000000 	                281.000000
max 	4137.000000 	365.000000 	            490.000000 	        96.870000 	              94.000000 	            365.000000


# I think that 'reviews per month' and 'availability_365' could be colinear, which brings me to my hypothesis.My hypothesis is that there will be a high corelation between 'reviews per month' and availability ('availability 365'), because more availability could mean more stays per airbnb, which could lead to more reviews.

# Extract 'reviews per month' and 'availability 365' columns
data = df.take([6, 10], axis='columns')

# Fill in missing data with 0's
data.fillna(0, axis='columns')

# Create dummy variable for listings with over 100 reviews
data['over_100_reviews'] = data['number_of_reviews'] > 100

# Get the correlation between the data sets
print(data.corr())

#                   number_of_reviews  availability_365  over_100_reviews
# number_of_reviews           1.000000          0.131938  0.797708
# availability_365            0.131938          1.000000  0.098980
# over_100                    0.797708          0.098980  1.000000

# When I looked at the correlation between number of reviews and days available out of the year, I found that there was a .13 correlation
# It would seem that they are not actually correlated afterall.