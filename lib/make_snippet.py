def make_snippet(string):
    words = string.split(' ')
    if len(words) > 5:
        first_five_words = words[:5]
        snippet = " ".join(first_five_words) + "..."
        return snippet
    return string