"""
Translating f2e and e2f
"""
import os
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    """
    Translates given english text to french
    """
    if english_text in ("", None):
        return ""
    translation = json.dumps(language_translator.translate(text=english_text,
                                                model_id='en-fr').get_result())
    return json.loads(translation)["translations"][0]["translation"]
def french_to_english(french_text):
    """
    Translates given french text to english
    """
    if french_text in ("", None):
        return ""
    translation = json.dumps(language_translator.translate(text=french_text,
                                                model_id='fr-en').get_result())
    return json.loads(translation)["translations"][0]["translation"]
