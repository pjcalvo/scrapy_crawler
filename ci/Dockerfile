FROM python:3.7
WORKDIR /usr/src/app

COPY app-code .
RUN pip3 install -r app-code/requirements.txt
CMD ["make","spider"]

# environment variables
# DYNACONF_NAME 
# DYNACONF_ALLOWED_DOMAINS
# DYNACONF_START_URLS='@json ["baserul", "baseurl2"]'