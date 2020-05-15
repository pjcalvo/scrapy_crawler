# Webscraper that checks for errors and reports back to a csv file

Python General Stuff
```sh
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

* Use the 'Makefile' to execute the checker
* Configuration under `settings.py`



# For the redirect script
Make a coma separated file with <column1,column2> in which column1 is the original url and column2 is the expected redirect result.

```csv
/fr/about-us-fr,/about-us
/fr/candidates-fr,/candidates
/fr/careers-fr,/about-us/careers
/fr/careers-fr/experienced-professionals-fr,/about-us/careers/experienced-professionals
/fr/careers-fr/new-graduates-fr,/about-us/careers/new-graduates
```

1) Place the source.csv file in the root directory.
2) Run `make redirect`.
3) The result will be added to the results folder