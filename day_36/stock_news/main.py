import requests
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
params_stock = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_NAME,
    "apikey": "QD6JBK7BZZ7JHXXV.",
    "datatype": "json"
}
params_news = {
    "apiKey": "d18cee1e45c04d5ca7dad6f12b2a706d",
    'qInTitle': COMPANY_NAME,

}
response = requests.get(STOCK_ENDPOINT, params=params_stock)
response.raise_for_status()
data = response.json()['Time Series (Daily)']

data_list = [value for i, value in data.items()]
yesterday = data_list[0]['4. close']
day_before_yestarday = data_list[1]['4. close']

positive_difference = abs(float(yesterday) - float(day_before_yestarday))
difference_percent = (positive_difference/float(day_before_yestarday) * 100)

if difference_percent > 5:
    print("Get News")
    news_response = requests.get(NEWS_ENDPOINT, params=params_news)
    response.raise_for_status()
    articles = news_response.json()["articles"]
    three_articles = articles[:3]
    news = [({'title': i['title'],
              'description':i['description']}) for i in three_articles]
    print(news)
