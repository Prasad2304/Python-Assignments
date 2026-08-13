#run-length encoding
#compress a string  by counting consecutive characters 

def run_length_encoding(s):
    if not s:
        return ""
    
    encoded = []
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            encoded.append(f"{s[i - 1]}{count}")
            count = 1
            
    encoded.append(f"{s[-1]}{count}")  
    return ''.join(encoded)