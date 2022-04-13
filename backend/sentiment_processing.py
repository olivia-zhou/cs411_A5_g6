import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, SentimentOptions

def get_sentiment(target):

    f = open('watsoncreds.json')
    creds = json.load(f)
    # print(creds["apikey"])

    authenticator = IAMAuthenticator(creds["apikey"])
    natural_language_understanding = NaturalLanguageUnderstandingV1(
        version='2022-04-07',
        authenticator=authenticator
    )


    natural_language_understanding.set_service_url(creds["url"])

    response = natural_language_understanding.analyze(
        text = target,
        features=Features(sentiment=SentimentOptions())).get_result()

    return response["sentiment"]["document"]["score"]

# print(get_sentiment("Partly cloudy, with a low around 47. West wind around 6 mph."))