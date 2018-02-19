#!/usr/bin/env python3
import sys
import mechanicalsoup

# connect to duckduckgo
browser = mechanicalsoup.StatefulBrowser()
browser.open("https://duckduckgo.com/")

# fill in search form
browser.select_form('#search_form_homepage')
browser["q"] = sys.argv[1]
browser.submit_selected()

# display results
for link in browser.get_current_page().select('a.result__a'):
    print("%50s -> %s" % (link.text[0:50], link.attrs['href']))
