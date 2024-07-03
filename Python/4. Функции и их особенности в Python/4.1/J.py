def merge(tuple1, tuple2):
    merged = []
    i = 0
    j = 0

    while i < len(tuple1) and j < len(tuple2):
        if tuple1[i] <= tuple2[j]:
            merged.append(tuple1[i])
            i += 1
        else:
            merged.append(tuple2[j])
            j += 1

    while i < len(tuple1):
        merged.append(tuple1[i])
        i += 1

    while j < len(tuple2):
        merged.append(tuple2[j])
        j += 1

    return tuple(merged)
