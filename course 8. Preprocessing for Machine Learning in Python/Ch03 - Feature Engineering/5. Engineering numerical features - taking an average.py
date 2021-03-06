'''
A good use case for taking an aggregate statistic to create a new feature is to take the mean of columns. Here, you have a DataFrame of running times named running_times_5k. For each name in the dataset, take the mean of their 5 run times.
'''

# Create a list of the columns to average
run_columns = ['run1', 'run2', 'run3', 'run4', 'run5']

# Use apply to create a mean column
running_times_5k["mean"] = running_times_5k.apply(lambda row: row[run_columns].mean(), axis=1)

# Take a look at the results
print(running_times_5k)




<script.py> output:
          name  run1  run2  run3  run4  run5   mean
    0      Sue  20.1  18.5  19.6  20.3  18.3  19.36
    1     Mark  16.5  17.1  16.9  17.6  17.3  17.08
    2     Sean  23.5  25.1  25.2  24.6  23.9  24.46
    3     Erin  21.7  21.1  20.9  22.1  22.2  21.60
    4    Jenny  25.8  27.1  26.1  26.7  26.9  26.52
    5  Russell  30.9  29.6  31.4  30.4  29.9  30.44
