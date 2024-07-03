import pandas as pd


def need_to_work_better(journal):
    return journal[journal.apply(lambda row: any(row[1:] == 2), axis=1)]
