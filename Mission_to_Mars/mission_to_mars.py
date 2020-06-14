from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser
import pandas as pd


def scrape_mars():

    url = "https://mars.nasa.gov/"
    response = requests.get(url)
    soup = bs(response.text, "html.parser")


#Find the feature articles title and description

    title = soup.find("h1", class_="media_feature_title").find("a").text

    news_p = soup.find("div", class_="description").find("a").text




#Set up chromedriver

    executable_path = {"executable_path": "chromedriver.exe"}
    browser = Browser('chrome', **executable_path, headless=False)




#Use splinter to navigate to correct page

    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)
    browser.click_link_by_partial_text("FULL IMAGE")
    browser.click_link_by_partial_text("more info")


#Get image url

    response = requests.get(browser.url)
    soup = bs(response.text, "html.parser")

    featured_image = soup.find("figure", class_="lede").find("a")["href"]

    featured_image_url = ("https://www.jpl.nasa.gov" + featured_image)


#Set up beautiful soup to get weather report

    url = "https://twitter.com/marswxreport?lang=en"
    response = requests.get(url)
    soup = bs(response.text, "html.parser")


#Get the latest tweet

    tweet = soup.find("div", class_="css-901oao r-1adg3ll r-1b2b6em r-q4m81j").find("span", class_="css-901oao css-16my406").text


#Get the table

    url = "https://space-facts.com/mars/"
    mars_tables = pd.read_html(url)
    mars_facts_table = mars_tables[0]


#Save the HTML file

    mars_html = mars_facts_table.to_html()
    mars_html.replace("\n", "")
    mars_facts_table.to_html("mars_table.html")


#Navigate to page to get hemisphere image

    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)
    browser.click_link_by_partial_text("Cerberus Hemisphere Enhanced")
    browser.click_link_by_partial_text("Open")


#Get hemisphere photo and title

    response = requests.get(browser.url)
    soup = bs(response.text, "html.parser")
    first_image_title = soup.find("h2", class_="title").text
    first_image_url = soup.find("li").find("a")["href"]


#Navigate to page to get hemisphere image

    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)
    browser.click_link_by_partial_text("Schiaparelli Hemisphere Enhanced")
    browser.click_link_by_partial_text("Open")



#Get hemisphere photo and title

    response = requests.get(browser.url)
    soup = bs(response.text, "html.parser")
    second_image_title = soup.find("h2", class_="title").text
    second_image_url = soup.find("li").find("a")["href"]



#Navigate to page to get hemisphere image

    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)
    browser.click_link_by_partial_text("Syrtis Major Hemisphere Enhanced")
    browser.click_link_by_partial_text("Open")


#Get hemisphere photo and title

    response = requests.get(browser.url)
    soup = bs(response.text, "html.parser")
    third_image_title = soup.find("h2", class_="title").text
    third_image_url = soup.find("li").find("a")["href"]



#Navigate to page to get hemisphere image

    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)
    browser.click_link_by_partial_text("Valles Marineris Hemisphere Enhanced")
    browser.click_link_by_partial_text("Open")



#Get hemisphere photo and title

    response = requests.get(browser.url)
    soup = bs(response.text, "html.parser")
    fourth_image_title = soup.find("h2", class_="title").text
    fourth_image_url = soup.find("li").find("a")["href"]


    browser.quit()
    
#Create a dictionary with all scraped data

    mars_dict = {
        "Title": title,
        "Description": news_p,
        "Featured_image": featured_image_url,
        "Tweet": tweet,
        "Cerberus_title": first_image_title,
        "Cerberus_url": first_image_url,
        "Schiaparelli_title": second_image_title,
        "Schiaparelli_url": second_image_url,
        "Syrtis_title": third_image_title,
        "Syrtis_url": third_image_url,
        "Valles_Marineris_title": fourth_image_title,
        "Valles_Marineris_url": fourth_image_url
    }

    return mars_dict

