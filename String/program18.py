#Remove duplicates Characters
#Remove duplicates characters  while maintaining order

def remove_duplicates(s):
    result = ""
    seen = set()
    
    for char in s:
        if char not in seen:
            seen.add(char)
            result += char
            
    return result