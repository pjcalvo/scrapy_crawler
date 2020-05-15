import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from time import sleep
from dynaconf import settings

SOURCE_FILE = settings.SOURCE_FILE
OUTCOME_FILE = settings.RESULTS_FILE
BASE_URL = settings.REDIRECTS_BASE_URL
FAILURE_CODES = settings.REPORT_IF

def run_script():

    # to handle retries when the server refuses to reply
    session = requests.Session()
    retry = Retry(connect=3, backoff_factor=0.5)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)

    # read the file
    with open(SOURCE_FILE) as file:
        # python magic here: for each row, split it and return origin and destination
        for origin, dest in map(lambda line: line.rstrip('\n').split(','), file):
            # open the file to write
            with open(OUTCOME_FILE, 'a') as outcome_file:
                # URL is base + origin
                requested_url = f'{BASE_URL}{origin}'
                print (f'* Request: {requested_url}')
                try:
                    req = session.get(requested_url)
                except Exception as ex:
                    print (ex)
                    outcome_file.write(f'ERROR: TOO many redirects: {dest}. ')
                    continue
                print (f' Response: {req.url}')
                # if result URL is not expected or there is an error then failure
                if (f'{BASE_URL}{dest}' != req.url) or req.status_code in FAILURE_CODES:        
                        outcome_file.write(f'Failed redirect: {dest}. ActualURL: {req.url}. ResponseCode: {req.status_code}\n')

if __name__=="__main__":
  run_script()
