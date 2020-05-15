# scrapy config
DOWNLOAD_DELAY = 0.2
CONCURRENT_REQUESTS_PER_DOMAIN = 10
AUTOTHROTTLE_ENABLED = True

# custom config
# status codes to be reported in CSV
REPORT_IF = [404,500,400]
NAME = 'scrapy'
# pass in a list of domains
ALLOWED_DOMAINS = ['http://www.thetabernaclechoir.org','https://www.thetabernaclechoir.org']
DISALLOWED_DOMAINS = ['www.adobe.com']
# pass in a single domain as string
START_URLS = ['https://www.thetabernaclechoir.org/music-spoken-word/history-of-music-and-the-spoken-word.html','https://www.thetabernaclechoir.org/music-spoken-word/history-of-music-and-the-spoken-word.html']

#redirects
REDIRECTS_BASE_URL = 'https://kornferry.com'
RESULTS_FILE = './results/results_for_redirect.csv'
SOURCE_FILE = './source.csv'
