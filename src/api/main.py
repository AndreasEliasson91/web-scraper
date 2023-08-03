import json
import os

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from typing import Any

from linkedin import linkedin_run

app = FastAPI()


@app.get('/')
async def index() -> RedirectResponse:
    return RedirectResponse('/web-scraper')

@app.get('/web-scraper')
async def web_scraper() -> Any:
    json_file = './test.json'
    df = linkedin_run(['digital', 'marketing'], ['malmö'])
    df.to_json(json_file)

    with open(json_file, 'r') as file:
        data = json.load(file)

    os.remove(json_file)
    return data
