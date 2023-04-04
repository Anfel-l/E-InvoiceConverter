# Test script
# Packages Import

import xml.etree.ElementTree as Etree
import pandas as pd

# Loading input file
Tree = Etree.parse('Input.xml path file')
root = Tree.getroot() # Parsed

A = []

for element in root:
    # Saving data into a dictionary
    B = {} 
    for i in list(element):
        B.update({i.tag: i.text}) # Updating dictionary with (tag -> Columns, text -> row Data)
        A.append(B)

df = pd.DataFrame(A) # Creating dataframe to store information
df.drop_duplicates(keep='first', inplace=True) # Delete if any duplicates
df.reset_index(drop = True, inplace=True)
writer = pd.ExcelWriter('Output.xlsx', engine='xlsxwriter') # Creating Excel File

df.to_excel(writer, sheet_name='Sheet Name') # There may be some changes here

worksheet = writer.sheets['shhet1']
worksheet.set_column('B:Z', 30) # To add space
writer.save()
print("Done!")