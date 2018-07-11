#!/usr/bin/env python
# coding: utf-8

"""
@oringin author: OrangeMeoww
@modified by : maidres
version 0.1
"""
import argparse
import sys
import os
import requests
import re
from bs4 import BeautifulSoup

#url = "https://www.javbus.com/"
#url = "https://www.javbus.info/"
url = "https://www.javbus.us/"

# proxy default config
proxy = {
    'http': 'socks5://127.0.0.1:1080',
    'https': 'socks5://127.0.0.1:1080',
}


def download_image_over_socks5(img_src):

    #ir = requests.get(img_src, proxies=proxy)
    ir = requests.get(img_src)
    if ir.status_code == 200:
        open(img_src.split(".")[-2].split("/")[-1] +
             os.path.splitext(img_src)[1], 'wb').write(ir.content)
    print '[-] ' + img_src.split(".")[-2].split("/")[-1] + " done!"


def download_image(avcode):

    s = requests.Session()

    #r = s.get(url + avcode, proxies=proxy)
    r = s.get(url + avcode)
    gidd = re.findall(r'[\d]{10,11}', r.text)
    gid = str(gidd[0])
    # gid 10-11
    # print gid

    ucc = re.findall(r'uc = [\d]', r.text)
    uc = str(ucc[0].split()[2])

    soup = BeautifulSoup(r.content.decode('utf-8', 'ignore'), 'html.parser')

    # get name
    name_node = soup.find('h3')

    name = name_node.text
    print '[*] ' + name

    cwd = os.getcwd()
    wd = os.path.join(cwd, name)
    if not os.path.exists(wd):
        try:
            os.mkdir(wd)
        except OSError, e:
            os.mkdir(wd[:100])
    os.chdir(wd)

    print "[*] Downloading cover image"
    img_node = soup.find('a', attrs={"class": "bigImage"})

    download_image_over_socks5(img_node.get('href'))

    # sample picture
    print '[*] Downloading sample image'
    sample_node = soup.findAll('a', class_="sample-box")
    for sample in sample_node:
        sample_src = sample.get('href')
        download_image_over_socks5(sample_src)

    return gid, uc


def get_av_magnet(avcode):

    Referer = {
        "Referer": "123"
    }

    s = requests.Session()
    gid, uc = download_image(avcode)

    params = {
        'gid': gid,
        'uc': uc,
        'lang': 'zh'
    }

#    r2 = s.get("http://www.javbus.com/ajax/uncledatoolsbyajax.php",
#               params=params, proxies=proxy, headers=Referer)
    r2 = s.get("http://www.javbus.com/ajax/uncledatoolsbyajax.php",
               params=params, headers=Referer)
    soup = BeautifulSoup(r2.content.decode('utf-8', 'ignore'), 'html.parser')

    trs = soup.findAll('tr', attrs={"height": "35px"})
    print '[*] get magnet link'
    for tr in trs:
        trsoup = BeautifulSoup(str(tr).decode('utf-8', 'ignore'), 'html.parser')
        td2 = trsoup.findAll('td', attrs={"style": "text-align:center;white-space:nowrap"})
        a = td2[0].find('a')
        magnet = a.get("href")  # unicode object
        size = a.text.strip()
        print '[*] ' + magnet, size

    os.chdir("../..")

def format_id(avcode):
    # insert '-'
    if avcode.find("-") == -1:
        i = 0
        l = list(avcode)
        for a in l:
            if a.isdigit():
                l.insert(i, '-')
                break
            i = i + 1
        if not l[0] == 'n':  # tokyohot
            avcode = ''.join(l)
    return avcode

def main():

    parser = argparse.ArgumentParser(
        description='Find magnetlink and download cover image via javID')
    parser.add_argument('-i', '--id', help='avcode you want to download', dest='id', default=None)
    parser.add_argument('-p', '--proxy', help='set your own HTTP/socks5',
                        dest='proxy', default=None)
    parser.add_argument('-d', '--disable-image', help='disable download image, only to search magnet',
                        dest='disable_image', default=None)

    args = parser.parse_args()

    avcode = args.id
    proxies = args.proxy
    disable_image = args.disable_image

    if avcode == None:
        parser.print_help()
        sys.exit(-1)

    if disable_image == None:
        disable_image = True

    # set proxy address
    if not proxies == None:
        proxy['http'] = proxies
        proxy['https'] = proxies
        print '[*] proxyurl set to ' + proxies

    # change directory to library

    cwd = os.getcwd()
    print "[*] Current working directory", cwd
    wd = os.path.join(cwd, 'library')
    if not os.path.exists(wd):
        os.mkdir(wd)

    os.chdir(wd)
    avcode = format_id(avcode)
    get_av_magnet(avcode)


if __name__ == '__main__':
    main()
