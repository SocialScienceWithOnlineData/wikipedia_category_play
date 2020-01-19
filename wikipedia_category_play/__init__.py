"""
wikipedia_category_play provides helper functions for exploring wikipedia API category data.  Adapted from projects.mako.cc/harrypotter-wikipedia-cdsw
"""

import os
import requests
from collections import OrderedDict 

def getWikipediaTitlesByCategory( categories, downstream = True, intersect=True, wiki_scanner='https://petscan.wmflabs.org/' ):
  """
  we'll use another api called catscan2 to grab a list of pages in
  categories and subcategories. it works like all the other apis we've
  studied!
  
  The following requests call basically does the same thing as this string:
  "https://petscan.wmflabs.org/?language=en&project=wikipedia&depth=10&categories=American%20people%0D%0A1970%20births&ns%5B0%5D=1&search_max_results=500&interface_language=en&active_tab=&doit="
  
  Code cribbed from projects.mako.cc/harrypotter-wikipedia-cdsw
  """
  
  # function can take a single category or a list of them.  
  #  if it gets one, it turns it into a list
  if type(categories) == list:
    categories = "\n".join(categories)
  
  if downstream:
    depth = 10
  else: 
    depth = 0
  
  if intersect:
    combination = "subset"
  else:
    combination = "union"
  
  #url_catscan = "http://tools.wmflabs.org/catscan2/catscan2.php"
  #url_catscan = "https://petscan.wmflabs.org/"
  url_catsan = wiki_scanner

  parameters = {'language' : 'en',
                'project' : 'wikipedia',
                'depth' : depth,
                'categories' : categories,
                'combination' : combination,
                'format' : 'json',
                'doit' : 1}

  r = requests.get(url_catscan, params=parameters)
  articles_json = r.json() ### get the result into a handy format
  articles = articles_json["*"][0]['a']["*"]  #### work the result down more to the meat: the retrieved articles as a list
  article_titles = [ article["title"].replace("_", " ") for article in articles  ] 
  return( article_titles )

