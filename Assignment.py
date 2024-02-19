import pandas as pd

# Step 1: Import and parse the CSV file
df = pd.read_csv('problem_sheet.csv', skiprows=20)  # Skip the first 20 rows containing header information

# Step 2: Parse the "index2" column from the CSV file
index2_column = df['index2']
index2_column.to_csv('index2.csv', index = False)
result_df = pd.DataFrame()

# Step 3: Perform operations on each string in the "index2" column
for i in range(len(index2_column)):
    # A. Reverse the string
    reversed_string = index2_column[i][::-1]

    # B. Complement the reversed string
    complemented_reversed_string = ''.join(['A' if base == 'T' else 'T' if base == 'A' else 'G' if base == 'C' else 'C' for base in reversed_string])

    # Add the results to the new DataFrame
    result_df = result_df.append({'Original_string': index2_column[i], 'Reverse_complemented_string': complemented_reversed_string}, ignore_index=True)

# Save the results to a new CSV file
result_df.to_csv('final_data.csv', index=False)
