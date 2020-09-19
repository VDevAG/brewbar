from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Scraper:

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        self.bot = webdriver.Chrome(chrome_options=options)

    def search(self, arg):
        bot = self.bot
        bot.get('https://formulae.brew.sh/')   
        time.sleep(1)
        searchfield = bot.find_element_by_xpath("/html/body/div/div[1]/div/span/input")
        searchfield.clear()
        searchfield.send_keys(arg)
        time.sleep(2)
        searchfield.send_keys(Keys.RETURN)
        time.sleep(2)
        formula = bot.find_element_by_xpath("/html/body/div/div[2]/table/tbody/tr[2]/td[1]/code")
        time.sleep(1)
        return formula.text

    def close_driver(self):
        self.bot.quit()

