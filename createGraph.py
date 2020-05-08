import timeit
from random import choice
from webcrawler import crawledList


def createGraph(func, trials=10):
    nVal = []
    tVal = []
    for i in range(0, len(crawledList), 1):
        for j in range(trials):
            runtime = 0
            url = [choice(crawledList) for n in range(i)]
            start = timeit.default_timer()
            func(url)
            end = timeit.default_timer()
            runtime += (end - start) * 1000
        runtime = runtime/trials
        nVal.append(i)
        tVal.append(runtime)
        
    return nVal, tVal
