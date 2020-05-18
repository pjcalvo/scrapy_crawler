# scrapy config
DOWNLOAD_DELAY = 0.2
CONCURRENT_REQUESTS_PER_DOMAIN = 10
AUTOTHROTTLE_ENABLED = True

# custom config
# status codes to be reported in CSV
REPORT_IF = [404,500,400]
# pass in a list of domains

DISALLOWED_DOMAINS = ['www.adobe.com']


#tabernacle
NAME = 'tabernacle'
ALLOWED_DOMAINS = ['youdidntspecifydomains']
START_URLS = ['starturl.com']

#redirects
REDIRECTS_BASE_URL = 'https://kornferry.com'
RESULTS_FILE = './results/results_for_redirect.csv'
SOURCE_FILE = './source.csv'
