from cellSegmentation.logger import logging
from cellSegmentation.exception import AppException
import sys

logging.info("welcome to cell segmentation")

try:
    a=5/"2"
except Exception as e:
    raise AppException(e,sys)