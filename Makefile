# Make file to make things easier
MKDIR_P = mkdir -p

OUT_DIR?=results
OUT_FILE?=report-file.csv
FILE_TYPE?=csv

check:
	${MKDIR_P} ${OUT_DIR}
	scrapy runspider scripts/script.py -t $(FILE_TYPE) -o - > ${OUT_DIR}/script-$(OUT_FILE)

spider:
	${MKDIR_P} ${OUT_DIR}
	scrapy runspider scripts/spider.py -t $(FILE_TYPE) -o - > ${OUT_DIR}/spider-$(OUT_FILE)

redirect:
	python scripts/redirects.py
