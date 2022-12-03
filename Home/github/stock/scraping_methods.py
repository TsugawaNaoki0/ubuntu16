import numpy as np
import matplotlib.pyplot as plt

class kabuoji3_class():
    def kabuoji3(self, url):
        import urllib.request, urllib.error
        from bs4 import BeautifulSoup
        import csv

        self.url = url
        # url = "https://kabuoji3.com/stock/6501/2019/"
        # URLを指定する
        html = urllib.request.urlopen(url)
        # URLを開く
        soup = BeautifulSoup(html, "html.parser")
        # BeautifulSoup で開く
        # HTMLからニュース一覧に使用しているaタグを絞りこんでいく
        aaa = soup.select(".data_contents")
        news_tag = soup.select("td") ###
        # print (news_tag)
        data_list_x = [[0 for i in range(7)] for k in range(int(len(news_tag)/7))]
        num = 0
        for i in range(0, int(len(news_tag) / 7)):
            for k in range(7):
                data_list_x[i][k] = news_tag[num]
                num += 1
        """
        for i in range(int(len(news_tag) / 7)):
            print(data_list_x[i])
        """
        csvlist = [["","ニュースリスト"]]
        num = 0
        for news_txt in news_tag:
            news_txt = news_txt.text
            csvlist.append([num, news_txt])
            num += 1
        # CSVファイルを開く。ファイルがなければ新規作成する。
        f = open("output.csv", "w")
        writecsv = csv.writer(f, lineterminator='\n')
        # 出力
        writecsv.writerows(csvlist)
        # CSVファイルを閉じる。
        f.close()
        for k in range(len(data_list_x)):
            z = data_list_x[k][0]
            # print()
            # print(z)
            z = str(z).replace("<td>", "").replace("</td>", "")
            # print(z)
            data_list_x[k][0] = str(z)
            # print(data_list_x[len(data_list_x)-1][i])
        for k in range(len(data_list_x)):
            for i in range(1, 7):
                z = data_list_x[k][i]
                # print()
                # print(z)
                z = str(z).replace("<td>", "").replace("</td>", "")
                # print(z)
                data_list_x[k][i] = float(z)
                # print(data_list_x[len(data_list_x)-1][i])
        dates = [0 for i in range(len(data_list_x))]
        qqq = [0 for i in range(len(data_list_x))]
        www = [0 for i in range(len(data_list_x))]
        eee = [0 for i in range(len(data_list_x))]
        rrr = [0 for i in range(len(data_list_x))]
        ttt = [0 for i in range(len(data_list_x))]
        yyy = [0 for i in range(len(data_list_x))]
        for i in range(len(data_list_x)):
            qqq[i] = data_list_x[i][1]
            www[i] = data_list_x[i][2]
            eee[i] = data_list_x[i][3]
            rrr[i] = data_list_x[i][4]
            ttt[i] = data_list_x[i][5]
            yyy[i] = data_list_x[i][6]
        plt.plot(range(1, len(data_list_x)+1), qqq, label="Opening Price")
        # plt.plot(range(1, len(data_list_x)+1), www, label="High Price")
        # plt.plot(range(1, len(data_list_x)+1), eee, label="Low Price")
        # plt.plot(range(1, len(data_list_x)+1), rrr, label="Closing Price")
        # plt.plot(range(1, len(data_list_x)+1), ttt, label="出来高")
        # plt.plot(range(1, len(data_list_x)+1), yyy, label="終値調整")
        return data_list_x

class finance_yahoo_class():
    def finance_yahoo(self, url_list, url_con):
        import urllib.request, urllib.error
        from bs4 import BeautifulSoup
        import csv

        dates = []
        hajime = []
        taka = []
        yasu = []
        owari = []
        dekidaka = []
        tyousei = []

        for t in range(len(url_list)):
            url = url_list[t]
            html = urllib.request.urlopen(url)
            soup = BeautifulSoup(html, "html.parser")
            news_tag = soup.select("td") ###
            for i in range(len(news_tag)):
                news_tag[i] = str(news_tag[i]).replace("<td>", "").replace("</td>", "")
                news_tag[i] = str(news_tag[i]).replace(",", "")

            data = []
            for i in range(3, len(news_tag)-1):
                data.append(news_tag[i])

            to_plot = data
            aaa = []
            i = 0
            while i < len(to_plot):
                if ('分割' in to_plot[i]):
                    i += 2
                else:
                    aaa.append(to_plot[i])
                    i += 1
                # """
            for i in range(len(aaa)):
                if i%7==0:
                    dates.append(aaa[i])
                elif i%7==1:
                    hajime.append(int(float(aaa[i])))
                elif i%7==2:
                    taka.append(int(float(aaa[i])))
                elif i%7==3:
                    yasu.append(int(float(aaa[i])))
                elif i%7==4:
                    owari.append(int(float(aaa[i])))
                elif i%7==5:
                    dekidaka.append(int(aaa[i]))
                elif i%7==6:
                    tyousei.append(int(float(aaa[i])))

            url_con += len(dekidaka)
            # for i in range(len(to_plot)):
            #     print(to_plot[i])
        # plt.plot(range(1, len(hajime)+1), hajime)
        # plt.plot(range(1, len(taka)+1), taka)
        # plt.plot(range(1, len(yasu)+1), yasu)
        # plt.plot(range(1, len(owari)+1), owari)
        plt.plot(range(url_con, len(dekidaka)+url_con), dekidaka)
        # plt.plot(range(1, len(tyousei)+1), tyousei)

        return dates, hajime, taka, yasu, owari, dekidaka, tyousei

import matplotlib.pyplot as plt

if __name__ == '__main__':
    print("[yahoo] / [kabuoji3] (\"L\"eft / \"R\"ight)")
    z = input()
    if (z == "l" or z == "L"):
        # url_url = "https://stocks.finance.yahoo.co.jp/stocks/history/?code=6501.T"
        url_list = []
        stock_code = 6501
        s_year = 1990
        s_month = 4
        s_date = 1

        f_year = 2019
        f_month = 3
        f_date = 31

        home_page_name = "https://info.finance.yahoo.co.jp/"
        for k in range(1, 10+1):
            url_maker = "history/?code={}.T&sy={}&sm={}&sd={}&ey={}&em={}&ed={}&tm=d&p={}".format(stock_code, s_year, s_month, s_date, f_year, f_month, f_date, k)
            full_url = home_page_name + url_maker
            url_list.append(full_url)
        # print(url_list)
        # for i in range(len(url_list)):
        #     print(url_list[i])
                                                                #  .format(<株コード>, <開始年>, <開始月>, <開始日>, <終了年>, <終了月>, <終了日>, <ページ番号>)
        url_con = 1
        yyy = finance_yahoo_class()
        kabuka_data = yyy.finance_yahoo(url_list, url_con)
        dates = kabuka_data[0]
        hajime = kabuka_data[1]
        taka = kabuka_data[2]
        yasu = kabuka_data[3]
        owari = kabuka_data[4]
        dekidaka = kabuka_data[5]
        tyousei = kabuka_data[6]
        # """
        plt.show()

    elif (z == "r" or z == "R"):
        url_url = "https://kabuoji3.com/stock/6501/2019/"
        yyy = kabuoji3_class()
        kabuka_data = yyy.kabuoji3(url_url)
    # """
        plt.show()
