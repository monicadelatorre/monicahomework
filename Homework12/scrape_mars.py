#!/usr/bin/env python
# coding: utf-8

# Dependencies
from bs4 import BeautifulSoup as bs
import requests as req
import os
from splinter import Browser
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


# # NASA Mars News
# 
# 
# Scrape the NASA Mars News Site and collect the latest News Title and Paragraph Text. 
# Assign the text to variables that you can reference later.

def init_browser():
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    return Browser("chrome", **executable_path, headless=False)

def scrape_info():
    browser = init_browser()
    scraped_data = {}


    url = "http://mars.nasa.gov/news/"
    browser.visit(url)
    html=browser.html

    soup = bs(html, 'lxml')

    title = soup.find(class_='content_title', string=True).text

    paragraph_text = soup.find(class_='article_teaser_body', string=True).text

    print(title)
    print(paragraph_text)

    # Add the title and paragraph text to the dictionary
    scraped_data["title"] = title
    scraped_data["paragraph_text"] = paragraph_text

    # # JPL Mars Space Images - Featured Image
    # 
    # 
    # Visit the url for JPL Featured Space Image here. https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars
    # Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called featured_image_url.
    # Make sure to find the image url to the full size .jpg image.
    # Make sure to save a complete url string for this image.

    img_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    base_url = 'https://www.jpl.nasa.gov/'

    #go to the website and open browser window
    browser.visit(img_url)

    #click on the "Full Image" button and navigate to that page
    browser.click_link_by_partial_text('FULL IMAGE')
    # Give time to complete the task before closing the browser. 
    time.sleep(10)

    #click on the "more info" button and navigate to that page
    browser.click_link_by_partial_text('more info')

    #create a soup object for that page you are on
    soup = bs(browser.html, 'lxml')
    #soup

    #find the image information from the above html, class is "main_image"
    image =soup.find(class_="main_image")
    print(image)

    #put the base url and the image file name together to create "featured_image_URL"
    featured_image_URL= base_url + image['src']
    print(featured_image_URL)

    # Add the featured_image_URL to the dictionary
    scraped_data["featured_image_URL"] = featured_image_URL

    # # Mars Weather
    # 
    # 
    # Visit the Mars Weather twitter account here https://twitter.com/marswxreport?lang=en and scrape the latest Mars weather tweet from the page. Save the tweet text for the weather report as a variable called mars_weather.

    twitter_url = 'https://twitter.com/marswxreport?lang=en'

    #go to the website and open browser window
    browser.visit(twitter_url)

    #create a soup object for that page you are on
    twitter_soup = bs(browser.html, 'lxml')
    #twitter_soup

    #find the tweet information from the above html, class is "TweetTextSize TweetTextSize--normal js-tweet-text tweet-text"
    tweet =twitter_soup.find(class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text').text
    print(tweet)

    # Add the tweet text to the dictionary
    scraped_data["tweet"] = tweet


    # # Mars Facts
    # 
    # 
    # Visit the Mars Facts webpage here 'http://space-facts.com/mars/' and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
    # Use Pandas to convert the data to a HTML table string.

    facts_url='http://space-facts.com/mars/'

    #go to the website and open browser window
    browser.visit(facts_url)

    # https://pythonprogramminglanguage.com/web-scraping-with-pandas-and-beautifulsoup/

    res = req.get(facts_url)

    table_soup = bs(res.content,'lxml')

    table = table_soup.find_all('table')[0] 

    # Use Pandas to convert the data to a HTML table string.
    df = pd.read_html(str(table))
    df

    # Add the HTML table string to the dictionary
    scraped_data["df"] = df
  
    print(df[0].to_json(orient='records'))


    # # Mars Hemispheres
    # 
    # 
    # Visit the USGS Astrogeology site here https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars to obtain high resolution images for each of Mar's hemispheres.
    # You will need to click each of the links to the hemispheres in order to find the image url to the full resolution image.
    # Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys img_url and title.
    # Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.

    usgs_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'

    # https://pythonspot.com/selenium-get-images/
    # use selenium to get all image links

    options = Options()
    options.headless = True
    driver = webdriver.Chrome('/usr/local/bin/chromedriver', chrome_options=options)

    driver.get(usgs_url)

    hemisphere_image_urls = []
    images = driver.find_elements_by_tag_name('img')
    for image in images:
        image_title=image.get_attribute('alt')
        image_url=image.get_attribute('src')
        print(image_title)
        print(image_url)
        
        hemisphere_image_urls.append({'title':image_title, 'img_url':image_url})
    driver.close()

    hemisphere_image_urls[1]

    # Add the image infomation to the dictionary
    scraped_data["image1"] = hemisphere_image_urls[1]
    scraped_data["image2"] = hemisphere_image_urls[2]
    scraped_data["image3"] = hemisphere_image_urls[3]
    scraped_data["image4"] = hemisphere_image_urls[4]

    return scraped_data



