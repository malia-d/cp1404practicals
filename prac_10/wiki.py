import wikipedia

page_title = input("Please enter a page title: ")
while page_title != "":
    page_title = wikipedia.page(page_title, auto_suggest=False)
    print("{}\n{}\n{}\n".format(page_title.title, page_title.summary, page_title.url))
    try:
        monty = wikipedia.summary("Monty")
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)
    page_title = input("Please enter a page title: ")
