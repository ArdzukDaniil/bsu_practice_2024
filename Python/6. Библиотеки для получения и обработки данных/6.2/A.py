import pandas as pd
import re


def length_stats(text):
    words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
    words.sort()
    lengths = [len(word) for word in words]
    return pd.Series(lengths, index=words)
