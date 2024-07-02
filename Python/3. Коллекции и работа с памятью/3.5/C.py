import sys

for line in sys.stdin:
    cleaned_line = line.split('#')[0].rstrip()
    if cleaned_line:
        print(cleaned_line)
