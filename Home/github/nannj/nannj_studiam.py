import numpy as np
import matplotlib.pyplot as plt
import sys
import time

class nannj_studiam_class():
    def nannj_studiam(self, url):
        import urllib.request, urllib.error
        from bs4 import BeautifulSoup
        import csv

        self.url = url

        html = urllib.request.urlopen(url)

        soup = BeautifulSoup(html, "html.parser")

        news_tag = soup.select("h2")
        news_tag = list(news_tag)

        for i in range(len(news_tag)):
            news_tag[i] = str(news_tag[i])

        # for i in range(7, len(news_tag)-5):
        #     data.append(news_tag[i])

        for i in range(len(news_tag)):
            index = news_tag[i].find("bookmark")
            # print(index)
            news_tag[i] = news_tag[i][index+27:]
            news_tag[i] = news_tag[i][:-9]


        return news_tag
        # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@








if __name__ == '__main__':
    import urllib.request, urllib.error

    url = "http://blog.livedoor.jp/nanjstu/"

    aaa = nannj_studiam_class()
    bbb = aaa.nannj_studiam(url)

    for i in range(len(bbb)):
        print(bbb[i])
