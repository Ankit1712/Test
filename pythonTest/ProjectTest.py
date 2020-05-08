from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
options = Options();
options.add_argument("--headless");
driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver',options=options)
driver.get("http://192.168.0.10:8080/hellosample/index.html")
assert "Hello Index" in driver.title
driver.close()
