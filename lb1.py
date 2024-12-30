import requests
import datetime
import matplotlib.pyplot as plt

# [Easy] Отримати курс валют із сайту НБУ за попередній тиждень з використанням python-бібліотеки requests

def fetch_exchange_rates():
    base_url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"
    end_date = datetime.datetime.now()
    start_date = end_date - datetime.timedelta(days=7)

    exchange_rates = {}

    for single_date in (start_date + datetime.timedelta(days=n) for n in range(8)):
        date_str = single_date.strftime("%Y%m%d")
        params = {"date": date_str, "json": ""}
        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            data = response.json()
            for item in data:
                currency = item["cc"]
                rate = item["rate"]
                if currency not in exchange_rates:
                    exchange_rates[currency] = []
                exchange_rates[currency].append((single_date.date(), rate))

    return exchange_rates

# [Easy-Medium] Побудувати графік зміни курсів валют за допомогою бібліотеки matplotlib

def plot_exchange_rates(exchange_rates, currencies_to_plot):
    plt.figure(figsize=(10, 6))

    for currency in currencies_to_plot:
        if currency in exchange_rates:
            dates, rates = zip(*exchange_rates[currency])
            plt.plot(dates, rates, label=currency)

    plt.xlabel("Date")
    plt.ylabel("Exchange Rate (UAH)")
    plt.title("Exchange Rate Trends")
    plt.legend()
    plt.grid()
    plt.show()

# Виконання скрипту
if __name__ == "__main__":
    rates = fetch_exchange_rates()
    print("Доступні валюти:", list(rates.keys()))

    # Оберіть валюти для побудови графіку
    selected_currencies = ["USD", "EUR"]  # Можна додати інші валюти
    plot_exchange_rates(rates, selected_currencies)
