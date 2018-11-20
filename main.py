import base64
import json
import logging
import os

from elasticsearch import Elasticsearch


es = Elasticsearch([os.getenv('ES_HOST')])


def handle_message(event, context):
    """Triggered from a message on a Cloud Pub/Sub topic.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    if 'data' not in event:
        logging.warn("No 'data' field in pub/sub message")
        return

    data = json.loads(base64.b64decode(event['data']).decode('utf-8'))
    msg_type = data.get('type')
    if not msg_type:
        logging.warn("No 'type' field in pub/sub message")
        return

    if msg_type == 'LOG':
        es.index(index=os.getenv('ES_INDEX'), doc_type='log',
                 body=data.get('payload'))
    else:
        logging.warn("Unknown message type '{}'".format(msg_type))

    return None
