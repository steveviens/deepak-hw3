#
#  Copyright 2020-2021 Viens Consulting, LLC. All Rights Reserved.
#

import json
import datetime
from datetime import datetime


# Utility functions
def converter(obj):
    # datetime type is not json serializable so convert to string
    if isinstance(obj, datetime):
        return obj.__str__()


def prettyprint(jsonObj):
    print('{}'.format(json.dumps(jsonObj, indent=2, sort_keys=False, default=converter)))


def timestamp():
    now = datetime.now()  # current date and time
    return now.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3]


"""
# TEST DRIVER
data = {
    'name': 'Steve Viens',      # string
    'age': 52,                  # numeric
    'isAwesome': True,          # boolean
    'now': datetime.now(),      # datetime type (not json serializable)
    'timeStamp': timestamp()    # test timestamp() function
}

prettyprint(data)
"""
