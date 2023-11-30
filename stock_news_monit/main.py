import requests
from twilio.rest import Client
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
NEWS_API_KEY = "f6afe3854fe84560a79eff15d424dc62"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
"""Daily limit 25 request for API """
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": "7S8OZIMG7QUSMF6R",
    "datatype": "json"
}

# stock_response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
# stock_response.raise_for_status()
# stock_data = stock_response.json()
# day_prev_close = float(stock_data['Time Series (Daily)']['2023-11-29']['4. close'])
# two_day_close = float(stock_data['Time Series (Daily)']['2023-11-28']['4. close'])


day_prev_close = 247.680
two_day_close = 235.236
absolut_diff = abs(day_prev_close - two_day_close)
percent_diff = (absolut_diff / day_prev_close) * 100
print(percent_diff)

news_parameters ={
    "apiKey": NEWS_API_KEY,
    "q": "Tesla ",
    "searchIn": "title",
    "pageSize": 3,
    "from": '2023-11-30',
    "to": '2023-11-29',
    "language": "en",
    "sortBy": "popularity",
    "totalResults": 3,
}
news_response = requests.get("https://newsapi.org/v2/everything", params=news_parameters)
news_response.raise_for_status()
news_data = news_response.json()

news_title = (news_data["articles"][0]['title'])


def send_SMS():
    account_sid = "ACe35debc71d618db5205a60f98130c727"
    auth_token = "897ceea7e411db18dbd7e555e3e4c79b"
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_="+19562699689",
        body=f"W dniu 2023-11-30 aukcje firmy {COMPANY_NAME} 🔻 5%   \n"
             f"Jest to spowodowane prawdopodobnie faktem który znalazłem w sieci : \n"
             f"{news_title} ",
        to="+48519193352"
    )
    print(message.status)

if percent_diff > 5:
    print("Get News")
    send_SMS()

"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

