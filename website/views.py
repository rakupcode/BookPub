from turtle import heading
from flask import Blueprint, render_template, render_template_string, request
# from libgen_api import LibgenSearch
import requests
from bs4 import BeautifulSoup

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html", heading = "Welcome")

@views.route('/results')
def results():
    query = request.args.get('query', '')
    reading = []
    # download = []
    if query:
        response = requests.get(f'https://gutendex.com/books?search={query}')
        if response.status_code == 200:
            data = response.json()
            reading = data['results']
        # s = LibgenSearch()
        # download = s.search_title(query)
        heading = "Search Results for " + "\""+ query +"\""

    return render_template('results.html', query=query, results=results, reading = reading, heading=heading)

url='https://www.gutenberg.org/cache/epub/2148/pg2148-images.html'

@views.route('/book')
def readBook():
    # Step 1: Fetch the page content
    url = request.args.get('url', '')
    response = requests.get(url)
    html_content = response.content

    # Step 2: Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    heading=soup.h1.next_element


    contents = soup.find_all(class_ ="pginternal")

    text = soup.find_all(class_="chapter")


    # Step 4: Create the navigation and content structure
    base_start = ['{% extends "home.html" %}{% block title %}Results{% endblock %} {% block content %}  <div class="container-fluid mt-5 pt-2"> <div class="row flex-xl-nowrap">']
    base_end = ['</div> </div> {% endblock %}']
    content_html = ['<div class="position-fixed col-12 col-md-3 col-xl-2 bd-sidebar" id="sidebar"> <div class="sidebar-heading py-1"><h4>Contents</h4></div> <div class="list-group list-group-flush overflow-auto h-100">']
    text_html = ['<main class=" vh-100 float-right col-12 col-md-9 col-xl-8 py-md-3 pl-md-5 bd-content" role="main">']
    # text_html.append('<h1 class="mt-4">'+ heading + '</h1>')

    # chapter_counter = 1
    # subchapter_counter = 1
    # in_subchapter = False

    for content in contents:
        # content['class']="list-group-item list-group-item-action"
        content_html.append('<span>' + str(content) +'</span>')
    content_html.append('</div></div>')
    
    for chapter in text:
        text_html.append(str(chapter)+'<hr><br>')
    footer = '<footer class="d-flex py-3 my-4 border-top"><div class="col-md-4 d-flex align-items-center"><img src="/static/gutenberg.svg" width="30" height="30" class="d-inline-block align-top" alt=""><span class="mb-3 text-muted">© 2024 Rakup Reads. All rights reserved.</span></div></footer>'
    text_html.append('--- END OF BOOK ---')
    text_html.append(footer)
    text_html.append('</main>')
    

    # Step 5: Combine and Output the Result
    final_html = '\n'.join(base_start + content_html +text_html + base_end)
    return render_template_string(final_html, heading=heading)
