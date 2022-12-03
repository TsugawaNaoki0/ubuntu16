from tkinter import messagebox
import bs4
import requests
import re
import urllib.request, urllib.error
import os
import argparse
import sys
import json
import os
import time
import datetime


class file_name_dates_class():
    def file_name_dates(self):
        now = datetime.datetime.now()
        now_id = now
        now_id = str(now_id)

        id = ""
        for i in range(20, 26):
            id += str(now_id[i])
        file_name = now.strftime('%Y' + "年" + '%m' + "月" + '%d' + "日" + '%H' + "時" + '%M' + "分" + '%S' + "秒")
        no_mili = file_name
        file_name += id
        # print(file_name)
        return file_name, no_mili


# How To
# (1) ソースコードを保存して命名する (e.g. scrape.py)
# (2) プログラムを起動する python scrape.py
# (3) オプション
# -s: Google Imagesにかける検索キーワード、複数可 (デフォルト "banana")
# -n: ダウンロードする画像の数量 (デフォルト 10枚)
# -o: 画像の保存先 (デフォルト　<DEFAULT_SAVE_DIRECTORY>で指定する)
class get_soup_class ():
    def get_soup(self, url,header):
        return bs4.BeautifulSoup(urllib.request.urlopen(urllib.request.Request(url,headers=header)),'html.parser')

    def main(self, args):
        parser = argparse.ArgumentParser(description='Options for scraping Google images')
        parser.add_argument('-s', '--search', default='abc', type=str, help='search term')
        parser.add_argument('-n', '--num_images', default=0, type=int, help='num of images to scrape')
        parser.add_argument('-o', '--directory', default='./figures', type=str, help='output directory')
        args = parser.parse_args()

        # 複数のキーワードを"+"で繋げる
        query = args.search.split()
        query = '+'.join(query)
        max_images = args.num_images

        # 画像をフォルダーでグループする
        save_directory = args.directory + '/' + query
        if not os.path.exists(save_directory):
            os.makedirs(save_directory)

        # スクレーピング
        url="https://www.google.co.jp/search?q="+query+"&source=lnms&tbm=isch"
        header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
        bbb = get_soup_class()
        soup = bbb.get_soup(url,header)
        ActualImages=[]

        for a in soup.find_all("div",{"class":"rg_meta"}):
            link , Type =json.loads(a.text)["ou"]  ,json.loads(a.text)["ity"]
            ActualImages.append((link,Type))
        for i , (img , Type) in enumerate( ActualImages[0:max_images]):
            try:
                Type = Type if len(Type) > 0 else 'jpg'
                # print("Downloading image {} ({}), type is {}".format(i, img, Type))
                print(i)
                raw_img = urllib.request.urlopen(img).read()
                f = open(os.path.join(save_directory , "img_"+str(i)+"."+Type), 'wb')
                f.write(raw_img)
                f.close()
            except Exception as e:
                print ("could not load : "+img)
                print (e)

if __name__ == '__main__':

    # ['get_pics.py', '-n', '3', '-s', 'no']
    # round = 3
    while True:
        print("Do you want to delete ./figure directory when this program finished ? (yes/no)")
        ans = input()
        if ans == "yes":
            del_check = 0
            break
        elif ans == "no":
            del_check = 1
            break
    print()
    print()
    print()
    print()
    # ;lkf:slakla;ksl;aksla;fksd
    word_list = []
    i = 0
    print("Input search word")
    while (True):
        word = input()
        if word=="qwerty":
            break
        else:
            word_list.append(word)
            i += 1
            print("@@@ @@@")

    print(word_list)
    # word_list = 'one','two','three','four','five','six','seven','eight', \
    #             'nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen'

    # """
    round = len(word_list)

    from sys import argv
    argv.append("-n")
    argv.append('10')
    argv.append("-s")
    argv.append([])
    for i in range(round):
        argv[4] = word_list[i]  # 検索ワードを順番に代入していく
        # argv[2] = '100'  # 取ってくる枚数
        try:
            aaa = get_soup_class()
            aaa.main(argv)
        except KeyboardInterrupt:
            pass
        print("@@@ @@@ @@@")
        print("@@@ @@@ @@@")
        print("@@@ @@@ @@@")
        print("@@@ @@@ @@@")
        print("@@@ @@@ @@@")
        print()
        print(argv)
        print(type(argv))
        print()
        print("@@@ @@@ @@@")
        print("@@@ @@@ @@@")
        print("@@@ @@@ @@@")
        print("@@@ @@@ @@@")
        print("@@@ @@@ @@@")
        print("@@@ @@@ @@@")
        print()
        print()
        print()

    aaa = file_name_dates_class()
    aaa_aaa = aaa.file_name_dates()
    os.system('git add *')
    os.system('git commit -m "{}"'.format(aaa_aaa[1]))
    os.system('git push')

    if del_check == 0:
        # """
        os.system('rm -rf figures')
        # """
    messagebox.showinfo('通知', '全作業が終了しました.')
    sys.exit()
    # """
