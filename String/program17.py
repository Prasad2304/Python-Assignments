#Anagram Check
#A check whether two strings are anagrams

def are_anagrams(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    if len(str1) != len(str2):
        return False
    
    return sorted(str1) == sorted(str2)

print(are_anagrams("listen", "silent"))  # True
print(are_anagrams("hello", "bello"))    # False