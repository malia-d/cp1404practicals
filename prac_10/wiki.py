"""
Ask the user for a page title and print the page title, page summary, and page url. Repeat until the user
enters a blank input.

Wiki. Created by Malia D'Mello, May 2021.
"""

import wikipedia

page_title = input("Please enter a page title: ")
while page_title != "":
    # Customise how the page is determined by setting auto_suggest as false.
    page_title = wikipedia.page(page_title, auto_suggest=False)
    print("{}\n{}\n{}\n".format(page_title.title, page_title.summary, page_title.url))
    # Handle disambiguation page using an exception.
    try:
        monty = wikipedia.summary("Monty")
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)
    page_title = input("Please enter a page title: ")
