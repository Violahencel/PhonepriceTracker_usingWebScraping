import requests
from bs4 import BeautifulSoup
import csv
import time

def scrape_amazon(phone_model):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.88 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
    }
    url = f"https://www.amazon.in/s?k={phone_model.replace(' ', '+')}"
    
    for _ in range(3):  # Retry logic, try up to 3 times
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            products = []

            for item in soup.select(".s-main-slot .s-result-item"):
                name = item.select_one("h2 .a-link-normal")
                price_whole = item.select_one(".a-price-whole")
                price_fraction = item.select_one(".a-price-fraction")
                link = item.select_one("h2 .a-link-normal")

                if name and price_whole and link:
                    price = f"{price_whole.text.strip()}{price_fraction.text.strip() if price_fraction else ''}"
                    products.append({
                        "website": "Amazon",
                        "name": name.text.strip(),
                        "price": price,
                        "link": "https://www.amazon.in" + link['href']
                    })
            return products
        
        elif response.status_code == 503:
            print(f"Service unavailable for {phone_model}, retrying...")
            time.sleep(5)  # Wait before retrying
    
    print(f"Failed to fetch data for {phone_model} after multiple attempts.")
    return []

def scrape_and_save_data():
    phone_models = ["iphone 14", "iphone 15", "iphone 15 Pro ","iphone 16", "iphone 16 Pro ", "oneplus", "samsung", "redmi", "realme", "vivo", "oppo"]
    with open('phone_prices.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Website", "Phone Name", "Price", "Link"])
        for phone_model in phone_models:
            print(f"Scraping data for: {phone_model}")
            products = scrape_amazon(phone_model)
            if products:
                for product in products:
                    writer.writerow([product["website"], product["name"], product["price"], product["link"]])
            time.sleep(10)  # Increase delay to avoid getting blocked

if __name__ == "__main__":
    scrape_and_save_data()
