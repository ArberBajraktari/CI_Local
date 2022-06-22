from fastapi import FastAPI
import csv
import json
import os
from functools import lru_cache

app = FastAPI()


@lru_cache()
def import_csv():
    data = {}
    try:
        with open("mcu-movies.csv") as csvFile:
            csvReader = csv.DictReader(csvFile)
            for rows in csvReader:
                movie = rows["movie"]
                data[movie] = rows

        return data
    except IOError:
        return "File not found. There was an error with loading the Data!"


@app.get("/")
async def root():
    return import_csv()
