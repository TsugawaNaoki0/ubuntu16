"""
import urllib.request, urllib.error
from bs4 import BeautifulSoup
import csv

# アクセスするURL
url = "https://mainichi.jp/"
# URLを開く
html = urllib.request.urlopen(url)
# BeautifulSoupで開く
soup = BeautifulSoup(html, "html.parser")

# HTMLからニュース一覧に使用しているaタグを絞りこんでいく
tag_mainbox = soup.select_one(".main-box")
tag_listA = tag_mainbox.select_one(".list-typeA")
news_tag = tag_listA.findAll("a")
# 配列の作成。表の見出し部分の情報を入力しておく。
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
"""
import urllib.request, urllib.error
from bs4 import BeautifulSoup
import csv

url = "https://mainichi.jp/"
# URLを指定する

html = urllib.request.urlopen(url)
# URLを開く

soup = BeautifulSoup(html, "html.parser")
# BeautifulSoup で開く

# HTMLからニュース一覧に使用しているaタグを絞りこんでいく
print(soup)
tag_mainbox = soup.select_one(".main-box")
tag_listA = tag_mainbox.select_one(".list-typeA")
news_tag = tag_listA.findAll("a")
### この辺は入れ子っぽい


# 配列の作成。表の見出し部分の情報を入力しておく。
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
