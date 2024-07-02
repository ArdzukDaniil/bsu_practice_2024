{char.lower(): text.lower().count(char.lower()) for char in set(text.lower()) if char.isalpha()}
