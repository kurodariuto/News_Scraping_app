import requests
import schedule
import json
import time
from scraping import news_data_url, news_data_title

# Set slack webhook  url
webhook_url = "Webhook url for your slack"

# Periodic execution function
def job():

    # Call the function of your own module
    news_ulr = news_data_url()
    news_text = news_data_title()

    # Send to Slack
    requests.post(webhook_url, data=json.dumps({
        "text": "ニュース一覧"
    }))
    result = 0
    while(result < len(news_ulr)):
        print(news_text[result])
        print(news_ulr[result])
        requests.post(webhook_url, data=json.dumps({
            "text": news_text[result] + news_ulr[result]
        }))
        result += 1

# Set to run regularly at 7 AM every day
schedule.every().day.at("07:00").do(job)
while True:
    schedule.run_pending()
    time.sleep(1)







