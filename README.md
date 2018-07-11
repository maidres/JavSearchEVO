# JavSearchEVO
# Modified from JavSearch

Find magnetlink and download cover image via javID

一个可以通过番号来下载封面和获取磁链的小工具。



## Installation

```bash
$ git clone https://github.com/qwqmeow/JavSearch
$ cd JavSearch
$ pip install -r requirments.txt
$ python search.py
```




## Usage

```bash
usage: search.py [-h] [-i ID] [-p PROXY]

Find magnetlink and download cover image via javID

optional arguments:
  -h, --help            show this help message and exit
  -i ID, --id ID        avcode you want to download
  -p PROXY, --proxy PROXY    set your own HTTP/socks5

```


### Examples

```bash
# 查找番号为star-735的影片
# 代理设置为socks5://127.0.0.1:8888
$ python search.py -i star735 -p socks5://127.0.0.1:8888
[*] proxyurl set tosocks5://127.0.0.1:8888
[*] Current working directory /root/JavSearch
[*] STAR-735 SODstar マジックミラー号誕生20周年記念作品 桐谷まつり AV Debut
[*] Downloading cover image
[-] 5stj_b done!
[*] Downloading sample image
[-] 1star00735jp-1 done!
[-] 1star00735jp-2 done!
[-] 1star00735jp-3 done!
[-] 1star00735jp-4 done!
[-] 1star00735jp-5 done!
[-] 1star00735jp-6 done!
[-] 1star00735jp-7 done!
[-] 1star00735jp-8 done!
[-] 1star00735jp-9 done!
[-] 1star00735jp-10 done!
[-] 1star00735jp-11 done!
[-] 1star00735jp-12 done!
[-] 1star00735jp-13 done!
[-] 1star00735jp-14 done!
[-] 1star00735jp-15 done!
[-] 1star00735jp-16 done!
[-] 1star00735jp-17 done!
[-] 1star00735jp-18 done!
[-] 1star00735jp-19 done!
[-] 1star00735jp-20 done!
[*] get magnet link
[*] magnet:?xt=urn:btih:C0335858DB2DF637114C11F556F5FF50A0FC949C&dn=star-735.mp4 2.09GB
[*] magnet:?xt=urn:btih:D67C963FCB2257DA14B20DBA90DF5C12C32031E3&dn=1211-javbo.net_star-735 4.2GB
```
文件结构
```bash
$ tree
├── library
│   └── STAR-735 SODstar マジックミラー号誕生20周年記念作品 桐谷まつり AV Debut
│       ├── 1star00735jp-10.jpg
│       ├── 1star00735jp-11.jpg
│       ├── 1star00735jp-12.jpg
│       ├── 1star00735jp-13.jpg
│       ├── 1star00735jp-14.jpg
│       ├── 1star00735jp-15.jpg
│       ├── 1star00735jp-16.jpg
│       ├── 1star00735jp-17.jpg
│       ├── 1star00735jp-18.jpg
│       ├── 1star00735jp-19.jpg
│       ├── 1star00735jp-1.jpg
│       ├── 1star00735jp-20.jpg
│       ├── 1star00735jp-2.jpg
│       ├── 1star00735jp-3.jpg
│       ├── 1star00735jp-4.jpg
│       ├── 1star00735jp-5.jpg
│       ├── 1star00735jp-6.jpg
│       ├── 1star00735jp-7.jpg
│       ├── 1star00735jp-8.jpg
│       ├── 1star00735jp-9.jpg
│       └── 5stj_b.jpg


```


## Notes
- 运行需要代理：目前滋滋 HTTP/SOCKS5 代理请自备
- 默认代理是socks5：127.0.0.1:1080
- 封面和例图会放在运行目录(不是脚本的存放目录)下的library目录中

## Todo
- magnet链接转换为种子，下载到对应目录中

## telegram bot
- bot @kerker233_bot
- /randomcar 随机发车
- /jav javID 查询番号的封面和磁链
