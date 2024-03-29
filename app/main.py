from fastapi import FastAPI
import csv
from functools import lru_cache

app = FastAPI()


@lru_cache()
def import_csv(file):
    data = {}
    try:
        with open(file) as csvFile:
            csvReader = csv.DictReader(csvFile)
            for rows in csvReader:
                movie = rows["movie"]
                data[movie] = rows
        return data
    except IOError:
        return "File not found. There was an error with loading the Data!"


@app.get("/")
async def root():
    return import_csv("files/mhcu-movies.csv")
