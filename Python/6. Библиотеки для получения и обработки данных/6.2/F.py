import pandas as pd


def best(journal):
    return journal[journal.apply(lambda row: all(row[1:] >= 4), axis=1)]
