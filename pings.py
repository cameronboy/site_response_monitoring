
import requests
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

def getCredentials(path_to_Credentials):
    scopes = ['https://spreadsheets.google.com/feeds']
    return ServiceAccountCredentials.from_json_keyfile_name(path_to_Credentials, scopes)

def main():
    # Retrieve the appropriate credentials object
    credentials = getCredentials('Gcred.json')
    # Authorize those credentials
    file = gspread.authorize(credentials)
    # Retrieve the sheets required
    sheet = file.open("Ping Monitoring").sheet1
    servers = file.open("Sites").sheet1.get_all_records()
    # Go through the servers and check their response time and write it to Ping Monitoring sheet
    for idx in range(len(servers)):
        url = servers[idx]["site"]
        provider = servers[idx]["provider"]
        typ = servers[idx]["type"]
        cat = servers[idx]["category"]
        response = requests.post(url).elapsed.total_seconds()
        time = str(datetime.now())
        sheet.append_row([site, typ, cat, provider, url, time, response])

if __name__ == '__main__':
    main()
