'''
Authors: Cuong Ly, Sergio Espinoza Ortiz, Josue
CMPE130 Project
Date: 5/8/20
'''
from urllib import request, parse
from bs4 import BeautifulSoup
import timeit
from random import choice
from collections import deque

queue = deque([])
crawledList = []
LINK_LIMIT = 3700

'''
Main algorithm of the application.
The parameter of this function is a URL.
'''

def BFSWebCrawler(url):
    crawledList.append(url)
    # print(len(queue))
    if len(crawledList) >= LINK_LIMIT:
        return
    # print("Crawling: ", url)  # Prints the url entered by user
    # returns back a request and takes care of 403 error
    req = request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = request.urlopen(req).read()  # Creates the html document
    soup = BeautifulSoup(html, "html.parser")  # Parses the html into an object
    for a_tag in soup.findAll('a'):  # Finds all a tags
        crawledFlag = False
        if a_tag.has_attr('href'):  # The following execute only if a_tag has an href
            href = a_tag['href']  # Extracts href
            full_url = parse.urljoin(url, href)
            for links in queue:
                if links == full_url:
                    crawledFlag = True
                    break
            if not crawledFlag:
                # print(len(queue))
                if len(crawledList) >= LINK_LIMIT:
                    return
                if crawledList.count(full_url) == 0:
                    # print("appended", full_url)
                    queue.append(full_url)
                # else:
                #     print("NOT ADDED", full_url)
    n = queue.popleft()
    # print("POPPED", n)
    BFSWebCrawler(n)

'''
createGraph is a function used to create a graph in jupyter notebook.
The parameters are the function (BFSWebCrawler) and the number of trials to run to get data.
'''

def createGraph(func, trials=10):
    #Initialize n = input and t = time arrays
    nVal = []
    tVal = []
    for i in range(0, len(crawledList), 1):
        for j in range(trials): #repeats for number of trials
            runtime = 0     #sets runtime = 0
            url = [choice(crawledList) for n in range(i)] #Generates an array of random URLs from crawledList of length i
            start = timeit.default_timer()  #start time
            func(url)
            end = timeit.default_timer()    #end time
            runtime += (end - start) * 1000 #find runtime and converts to milliseconds
        runtime = runtime/trials
        nVal.append(i)  #append i to nVal array
        tVal.append(runtime)    #append runtime to tVal array
        
    return nVal, tVal   

'''
Function to run the program. However, it's highly encouraged to run the program
in Jupyter Notebook for greater experience.
'''
if __name__ = "__main__":
    user_url = input("Enter URL to crawl: ")
    BFSWebCrawler(user_url)
    for urls in crawledList:
        print(urls)