import requests


class CurrencyConverter:

    def __init__(self, api_key: str = None):
        # Uses the free Open Access endpoint that requires no API key
        self.base_url = "https://er-api.com"

    def convert(
        self, amount: float, from_currency: str, to_currency: str
    ) -> float:
        url = f"{self.base_url}{from_currency.upper()}"
        response = requests.get(url)
        data = response.json()

        if data.get("result") != "success":
            raise Exception(f"API call failed: {data}")

        rates = data.get("rates", {})
        if to_currency.upper() not in rates:
            raise ValueError(f"{to_currency} not found in exchange rates.")

        return float(amount) * rates[to_currency.upper()]
