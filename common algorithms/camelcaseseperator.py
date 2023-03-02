def camelcase(s):
    # Write your code here

    camel_case_words : int = 0

    for letter_index in range(len(s)):
        if s[letter_index].isupper():
            camel_case_words += 1
    
    camel_case_words += 1
            
    return camel_case_words
        