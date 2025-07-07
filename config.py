#!/usr/bin/env python

import os
from dotenv import load_dotenv
import ee

# Load environment variables from a .env file if present
load_dotenv()

def get_env_var(name):
    value = os.environ.get(name)
    if value is None:
        raise EnvironmentError(f"Missing required environment variable: {name}")
    return value

EE_ACCOUNT = get_env_var('EE_ACCOUNT')
EE_PRIVATE_KEY_FILE = get_env_var('EE_PRIVATE_KEY_FILE')
GOOGLE_MAPS_API_KEY = get_env_var('GOOGLE_MAPS_API_KEY')
MAPBOX_ACCESS_KEY = get_env_var('MAPBOX_ACCESS_KEY')
CHATGPT_API_KEY = get_env_var('CHATGPT_API_KEY')

EE_CREDENTIALS = ee.ServiceAccountCredentials(EE_ACCOUNT, EE_PRIVATE_KEY_FILE)
