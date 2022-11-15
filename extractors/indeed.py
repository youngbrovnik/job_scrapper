# from requests import get
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from bs4 import BeautifulSoup

# options = Options()
# options.add_argument("--no-sandbox")
# options.add_argument("--disable-dev-shm-usage")

# browser = webdriver.Chrome(options = options)

# base_url = "https://kr.indeed.com/jobs?q="
# search_term = "python"

# browser.get(f"{base_url}{search_term}")

# print(browser.page_source)

# response = get(f"{base_url}{search_term}")

# if response.status_code != 200:
#     print("Cant request page")
# else:
#     print(response.text)