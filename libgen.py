# from bs4 import BeautifulSoup
# from urllib import request
# from urllib.parse import urlencode
# import re


# def getSearchResults(term, page, column):
#     params = urlencode({'req': term, 'column': column, 'page': page})
#     url = 'http://libgen.io/search.php?&%s' % params

#     source = request.urlopen(url)
#     soup = BeautifulSoup(source, 'lxml')
#     if page == 1:
#         books_found = re.search(r'(\d+) books found', str(soup))
#         print(books_found.group().upper())
#         n_books = int(books_found.groups()[0])

#     page_books = soup.find_all('tr')
#     page_books = page_books[3:-1]  # Ignore 3 first and the last <tr> label.
#     books = page_books
#     if page == 1:
#         return(books, n_books)
#     else:
#         return(books)
