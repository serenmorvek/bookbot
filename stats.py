def get_num_words(text):
    return len(text.split())

def get_num_chars(text):
    str_count = {}
    lowercase = text.lower()
    for i in lowercase:
        if i in str_count:
            str_count[i] += 1
        else:
            str_count[i] = 1
    return str_count

def sort_on(chars):
    return chars["num"]

def get_sorted_list(chars):
    sorted_list = []
    for char in chars:
        if not char.isalpha():
            continue
        sorted_list.append({"char": char, "num": chars[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list