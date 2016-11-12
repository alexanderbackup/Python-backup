def is_anagram(a, b):
    if sorted(a.lower()) == sorted(b.lower()):
        return True
    return False
print(is_anagram("TOP_CODER", "COTO_PRODE"))
