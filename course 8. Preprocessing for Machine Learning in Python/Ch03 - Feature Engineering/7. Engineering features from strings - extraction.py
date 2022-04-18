'''
The Length column in the hiking dataset is a column of strings, but contained in the column is the mileage for the hike. We're going to extract this mileage using regular expressions, and then use a lambda in Pandas to apply the extraction to the DataFrame.
'''

# Write a pattern to extract numbers and decimals
def return_mileage(length):
    pattern = re.compile(r"\d+\.\d+")
    
    # Search the text for matches
    mile = re.match(pattern, length)
    
    # If a value is returned, use group(0) to return the found value
    if mile is not None:
        return float(mile.group(0))
        
# Apply the function to the Length column and take a look at both columns
hiking["Length_num"] = hiking["Length"].apply(lambda row: return_mileage(row))
print(hiking[["Length", "Length_num"]].head())



<script.py> output:
           Length  Length_num
    0   0.8 miles        0.80
    1    1.0 mile        1.00
    2  0.75 miles        0.75
    3   0.5 miles        0.50
    4   0.5 miles        0.50
