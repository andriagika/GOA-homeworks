def name_shuffler(name):
    parts = name.split()    
    return ' '.join(parts[::-1])

def string_to_array(s):
    return s.split()

def reverse_words(text):
    return ' '.join(word[::-1] for word in text.split(' '))