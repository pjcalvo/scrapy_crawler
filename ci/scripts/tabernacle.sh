#!/bin/bash
# setup environment
ci/scripts/setup.sh

#prepare var

TIME_STAMP=`date "+%Y%m%d-%H%M%S"`
OUT_DIR="results"
OUTPUT_FILE="tabernacle_choir-${TIME_STAMP}.csv"

mkdir -p ${OUT_DIR}

scrapy runspider scripts/spider.py -t csv -o - > ${OUT_DIR}/spider-${OUTPUT_FILE}