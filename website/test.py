# Import Module 
from bs4 import BeautifulSoup 
import requests 

url = 'https://www.gutenberg.org/cache/epub/110/pg110-images.html'
response = requests.get(url)
html_content = response.content

# Step 2: Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

print(soup.h1.next_element)

# contents = soup.find_all(class_ ="pginternal")

# text = soup.find_all(class_="chapter")


# # Step 4: Create the navigation and content structure
# base_start = ['{% extends "home.html" %}{% block title %}Results{% endblock %} {% block content %}']
# base_end = ['{% endblock %}']
# content_html = ['<div class="list-group list-group-flush border-bottom scrollarea">']
# text_html = ['<div class="col-sm-8 text-left">']

# # chapter_counter = 1
# # subchapter_counter = 1
# # in_subchapter = False

# for content in contents:
#     content_html.append(str(content))
    
# for chapter in text:
#     text_html.append(str(chapter))
# text_html.append('</div>')
# content_html.append('</div>')

# final_html = '\n'.join(base_start + content_html +text_html + base_end)

# # Step 5: Combine and Output the Result
# print(final_html, encoding="utf-8")