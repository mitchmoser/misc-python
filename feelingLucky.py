#!/usr/bin/env python3
import sys
import mechanicalsoup

# connect to duckduckgo
browser = mechanicalsoup.StatefulBrowser()
browser.open("https://google.com/")

# fill in search form
browser.select_form('form[action="/search"]')
browser["q"] = sys.argv[1]
browser.submit_selected(btnName="btnI")

# display results
print(browser.get_url())
