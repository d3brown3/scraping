from bs4 import BeautifulSoup
from selenium import webdriver
import time
import random
import re
import csv
import numpy
import pickle

## provide email for login and password
## word to search
## public profile link to make sesssion more normal
## number of pages to click through
def linkedin_searcher(email_address, password_string, search_term, profile_link, pages):

    driver = webdriver.Chrome()

    login_link="https://www.linkedin.com/uas/login"
    driver.get(login_link)

    time.sleep(random.uniform(10,20))

    email = driver.find_element_by_xpath('//*[@id="session_key-login"]')
    email.send_keys(email_address)

    password = driver.find_element_by_xpath('//*[@id="session_password-login"]')
    password.send_keys(password_string)

    sign_in = driver.find_element_by_xpath('//*[@id="btn-primary"]')

    time.sleep(random.uniform(2,10))

    sign_in.click()

    time.sleep(random.uniform(60,120))

    driver.get(profile_link)

    time.sleep(random.uniform(60,120))

    #links
    links = []
    companies = []

    for page in range(1,pages+1):

        search_link = 'https://www.linkedin.com/search/results/companies/?keywords=' + search_term + '&page='
        search_link = search_link + str(page)
        driver.get(search_link)
        html=driver.page_source

        soup = BeautifulSoup(html)


        for link in soup.find_all('a'):
            links.append(link.get('href'))

        r = re.compile("^/company")
        links = filter(r.match, links)

        linkedin = "https://www.linkedin.com"

        links = [linkedin + l for l in links]

        companies = companies + links

        time.sleep(random.uniform(20,60))

    ##need to fix aggregating the lists [1,2,3]+[1,2,3]

    driver.quit()

    #with open('~/scraping/linkedin/' + search_term + '_firm_discovery.txt', 'wb') as f:
    #    pickle.dump(companies, f)
