def get_word_count(text):
    words = text.split()
    return len(words)

def char_counts(text):
    text = text.lower()
    counts = {}
    for char in text:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts

def sort_on(items):
    return items["num"]

def sort_counts(counts):
    sorted = []
    for key, value in counts.items():
        sorted.append({"char": key, "num": value})
    sorted.sort(reverse=True,key=sort_on)
    return sorted