import requests
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

with open('servers.json') as f:
    sites = json.load(f)

scope = ['https://spreadsheets.google.com/feeds']

credentials = ServiceAccountCredentials.from_json_keyfile_name('GCred.json', scope)

file = gspread.authorize(credentials)

sheet = file.open("Ping Monitoring").sheet1

for site in sites.keys():
    url = sites[site]["url"]
    provider = sites[site]["provider"]
    typ = sites[site]["type"]
    response = requests.post(url).elapsed.total_seconds()
    time = str(datetime.now())
    row = [site, typ, provider, url, time, response]
    sheet.append_row([site, typ, provider, url, time, response])
