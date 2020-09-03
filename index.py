# -*- coding: utf-8 -*-
import logging
import requests
import json



def handler(event, context):
  logger = logging.getLogger()
  evt = json.loads(event)
  logger.info(evt)

  response = requests.request(evt.get('method', 'GET'), evt['url'], params=evt.get('params'), headers=evt.get('headers'), data = evt.get('data'))
  return response.json()