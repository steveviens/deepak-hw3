#
#  Copyright 2019-2020 Viens Consulting, LLC. All Rights Reserved.
#

from datetime import datetime
import hw3_lambda
import logging
import pytz
import sys

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler(sys.stdout))

event = {
  "client_id": "tues",
  "bucket_name": "tues.857154852951",
  "source_key": "tues-gzmo-5088734",
  "provider_id": "gzmo",
  "source_id": "5088734",
  "source_type": "survey",
  "product_id": "rh01"
}

# Override defaults
#event['month_offset'] = 2
#event['target_month'] = '2020-11'
#event['email_filename'] = 'report_email_test.json'
#event['email_filename'] = 'report_email_weekly.json'
#event['email_filename'] = 'report_email_month_end.json'

timezone = pytz.timezone('US/Eastern')
timestamp = datetime.now(timezone)
started = datetime.now(timezone)
response = hw3_lambda.lambda_handler(event, context={})
status = response.get('statusCode')
results = response.get('results')
ended = datetime.now(timezone)
print("--------------------------")
print("HTTP STATUS  = {}".format(status))
print("RESULTS      = {}".format(results))
print("STARTED      = {}".format(started.strftime('%Y-%m-%d %H:%M:%S %Z')))
print("ENDED        = {}".format(ended.strftime('%Y-%m-%d %H:%M:%S %Z')))
print("DURATION     = {}".format(ended - started))
