'''
We know that the distribution of variables in the category_desc column in the volunteer dataset is uneven. If we wanted to train a model to try to predict category_desc, we would want to train the model on a sample of data that is representative of the entire dataset. Stratified sampling is a way to achieve this.
'''

# Create a data with all columns except category_desc
volunteer_X = volunteer.drop('category_desc', axis=1)

# Create a category_desc labels dataset
volunteer_y = volunteer[['category_desc']]

# Use stratified sampling to split up the dataset according to the volunteer_y dataset
X_train, X_test, y_train, y_test = train_test_split(volunteer_X, volunteer_y, stratify=volunteer_y)

# Print out the category_desc counts on the training y labels
print(y_train['category_desc'].value_counts())


'''
<script.py> output:
    Strengthening Communities    230
    Helping Neighbors in Need     89
    Education                     69
    Health                        39
    Environment                   24
    Emergency Preparedness        11
    Name: category_desc, dtype: int64
'''
