'''Code for IBM Applied Software Engineering Fundamentals'''

import os
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

#apikey = os.environ['apikey']
#url = os.environ['url']

apikey = 'x2fszQ5Bmac_kXRnU7H_0dGaJTelVBmZxY96x5mWq5rT'
url = 'https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/853977f7-d82e-45b0-a0d9-95ffc2615cfc'

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    '''English to French'''
    french_text = language_translator.translate(
    text=english_text,
    model_id='en-fr').get_result()
    print(json.dumps(french_text, indent=2, ensure_ascii=False))
    return french_text['translations'][0]['translation']

def french_to_english(french_text):
    '''French to English'''
    english_text = language_translator.translate(
    text=french_text,
    model_id='fr-en').get_result()
    print(json.dumps(english_text, indent=2, ensure_ascii=False))
    return english_text['translations'][0]['translation']
