import matplotlib.pyplot as plt

class login_class():
    def login(self, url):
        import urllib.request, urllib.error
        from bs4 import BeautifulSoup
        import csv

        self.url = url
        # url = "https://login.com/stock/6501/2019/"
        # URLを指定する
        html = urllib.request.urlopen(url)
        # URLを開く
        soup = BeautifulSoup(html, "html.parser")
        aaa = soup.select(".login")

        # BeautifulSoup で開く
        # HTMLからニュース一覧に使用しているaタグを絞りこんでいく
        print(aaa)
        return

import matplotlib.pyplot as plt

if __name__ == '__main__':
    # yyy = finance_yahoo_class()
    # kabuka_data = yyy.finance_yahoo("https://stocks.finance.yahoo.co.jp/stocks/history/?code=6501.T")
    yyy = login_class()
    # kabuka_data = yyy.login("https://stocks.finance.yahoo.co.jp/stocks/history/?code=6501.T")
    url = "http://qq856533.php.xdomain.jp/"
    kabuka_data = yyy.login(url)

    plt.show()
