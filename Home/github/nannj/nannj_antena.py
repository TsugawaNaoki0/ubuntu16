import numpy as np
import matplotlib.pyplot as plt
import sys
import time

class nannj_antena_class():
    def nannj_antena(self, url):
        import urllib.request, urllib.error
        from bs4 import BeautifulSoup
        import csv

        self.url = url

        html = urllib.request.urlopen(url)

        soup = BeautifulSoup(html, "html.parser")

        news_tag = soup.select("a")
        data = []
        news_tag = list(news_tag)



        for i in range(len(news_tag)):
            news_tag[i] = str(news_tag[i])

        for i in range(15, len(news_tag)):
            data.append(news_tag[i])

        for i in range(len(data)):
            index = data[i].find("nofollow")
            data[i] = data[i][index+10:]
            data[i] = data[i][:-4]
        return data



if __name__ == '__main__':
    import urllib.request, urllib.error

    url = "http://livejupiter2.net/"

    aaa = nannj_antena_class()
    bbb = aaa.nannj_antena(url)

    for i in range(len(bbb)):
        print(bbb[i])
