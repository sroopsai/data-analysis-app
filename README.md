### Python Dictionaries

- #### Python Dicionary Methods
```python
# copying dictionaries
capitals = {"Andhra Pradesh": "Vijayawada", "Telangana": "Hyderabad"}
state_capitals = capitals.copy() # copy capitals -> state_capitals
# update dictionary / add new key-value pair
capitals.update({"Tamil Nadu": "Chennai"})
```



### How to open a text file
`file_object = open("file", "mode")`
- Different modes
    - Create mode
        
        `f = open("file_name.txt", "w+")`
        
        ```
        Opens the file with read and write permissions.
        ```
    
    - Append mode
        
        `f = open("file_name.txt", "a+")`
        
    - Read mode
        
        `f = open("file_name.txt", "r")`
        
    - __Important__
    
        + Use `readlines()` function to read the file with large content.
        
        + Use `read()` function to read the entire file (better for file with small content). 
    
### How to read a *CSV* File

- Using `reader()` function of `csv module`
```python
# import required modules
import csv
with open("filename.csv", "r") as f:
    data = csv.reader(f)
    for row in data:
        print(row)
```

- Using `DictReader()` function of `csv module`
```python
# import required modules
import csv

data= csv.DictReader(open("filename.csv", "r"))
for row in reader:
    print(row)
```

### How to write data to a csv file

- To iterate over the rows use `writerow()` function of `csv module`.

```python
import csv

with open("filename.csv", mode="w") as f:
    data_to_write = csv.writer(f, delimiter=",", quotechar = '"', quoting = csv.QUOTE_MINIMAL)
    data_to_write.writerow(["Heading1", "Heading2"])
    data_to_write.writerow(["row1data", "row2data"])
```
