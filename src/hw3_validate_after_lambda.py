import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):

    # Print formatted JSON event object to log
    logger.info(json.dumps(event, indent=2, sort_keys=False))

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from HW3 Validate After Lambda!')
    }
