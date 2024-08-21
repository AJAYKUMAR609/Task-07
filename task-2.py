
# Task-7
import requests

class CountryInfo:
    def __init__(self, url):
        self.url = url
        self.data = self.fetch_data()

    def fetch_data(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Raise an exception for non-200 status codes
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching data: {e}")
            return None

    def display_country_info(self):
        if self.data is not None:
            for country in self.data:
                name = country.get("name", "N/A")
                currencies = country.get("currencies", [])
                if currencies:
                    if isinstance(currencies, list):
                        for currency in currencies:
                            currency_name = currency.get("name", "N/A")
                            currency_symbol = currency.get("symbol", "N/A")
                            print(f"Country: {name}, Currency: {currency_name}, Symbol: {currency_symbol}")
                    else:
                        print(f"Country: {name}, Currencies: N/A")
                else:
                    print(f"Country: {name}, Currency: N/A, Symbol: N/A")
        else:
            print("Error: No data retrieved from API")

    def filter_by_currency(self, currency_code):
        filtered_countries = [country for country in self.data if any(
            isinstance(currency, dict) and currency.get("code") == currency_code
            for currency in country.get("currencies", [])
        )]
        return filtered_countries


if __name__ == "__main__":
    url = "https://restcountries.com/v3.1/all"
    country_info = CountryInfo(url)

    # Display all country information with error handling
    country_info.display_country_info()

    # Filter countries with dollar as currency
    dollar_countries = country_info.filter_by_currency("USD")
    print("\nCountries with dollar as currency:")
    for country in dollar_countries:
        print(country["name"])

    # Filter countries with euro as currency
    euro_countries = country_info.filter_by_currency("EUR")
    print("\nCountries with euro as currency:")
    for country in euro_countries:
        print(country["name"])

#
import requests

def fetch_breweries_by_state(state):
    url = f"https://api.openbrewerydb.org/v1/breweries?by_state={state}"
    response = requests.get(url)
    return response.json()

def main():
    states = ["Alaska", "Maine", "New York"]

    for state in states:
        breweries = fetch_breweries_by_state(state)
        print(f"Breweries in {state}:")
        for brewery in breweries:
            print(f"- {brewery['name']}")

        print(f"Total breweries in {state}: {len(breweries)}\n")

if __name__ == "__main__":
    main()


