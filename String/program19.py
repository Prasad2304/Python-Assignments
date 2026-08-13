#Substring Search
#a check whether a given substring exists in the main string

def substring_search(main_string, substring):
    return substring in main_string

print(substring_search("Hello, World!", "World"))  
print(substring_search("Hello, World!", "Python")) 