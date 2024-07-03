import pandas as pd


def update(journal):
    journal['average'] = journal[['maths', 'physics', 'computer science']].mean(axis=1)
    return journal.sort_values(by=['average', 'name'], ascending=[False, True])
