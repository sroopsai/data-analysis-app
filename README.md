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

```python
# import required modules
import csv
with open("filename.csv", "rt") as f:
    data = csv.reader(f)
    for row in data:
        print(row)
```
