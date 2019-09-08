
# HTML, CSS and Web Scraping -  Recap

## Introduction

In this section, you learned a lot about web pages and how to exploit their structure for your own web scraping purposes. Take this opportunity to briefly review some of the key takeaways from the section.

## Objectives

You will be able to:
    
    * Identify key takeaways from web design
    * Recall precautions and best practices of web scraping

## HTML


To start this section, you investigated the basic structure of an HTML page and saw both the nested structure as well as some of the basic tags that you later leveraged for web scraping. This included `a` tags for links and `div` tags which act as general containers for other HTML code blocks.

## CSS

After taking an initial look at HTML, you then saw the role CSS plays in styling a web page. You learned that HTML deals with content while CSS deals with style. There is certainly more you could learn regarding CSS but an important take away is that CSS selectors can also be used while web scraping. For example, you can select a tag with `id` or `class` selector.

## Beautiful Soup

After an initial exploration into web development, you then returned to Python and used the requests and Beautiful Soup packages in order to extract data from the web. This was also a great chance for you to practice your data wrangling skills as you often will have to navigate nested data structures and clean messy data, removing spaces, using regular expressions and converting data types. 

## Precautions

Remember to practice caution when scraping websites. Surfing the web at superhuman speeds will get you banned from many domains and may violate the terms & conditions of many websites that require you to login. As such, there are a few considerations you should take along your way.

* Are there a terms and conditions for using the website?
* Test your scraping bot on in small samples to debug before scaling to hundreds, thousands or millions of requests.
* Start thinking about your IP address: getting blacklisted from a website is no fun. Consider using a VPN.
* Slow your bot down! Add delays along the way with the time package. Specifically, time.sleep(seconds) adds wait time in a program.

## Other Scraping Tools

While Beautiful Soup is a powerful go-to tool for scraping the web, remember that there are other tools such as Selenium and Scrapy that have their own advantages and disadvantages. While Beautiful Soup is apt to be your primary scraping tool, for now, it is worth noting that there are other options should you feel like you need additional resources such as interacting with dynamic javascript based websites.

## Summary

This was an exciting section delving into the world of web scraping! There's always a plethora of information to be mined from the web so go out there and get scraping!
