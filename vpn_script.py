# coding : utf8

'''
sslocal auto connect script
---------------------------------------
+ 1. 连续请求 5 次目标网站不成功，将自动退出本程序
+ 2. 从返回的所有信息中，依次选取一条自动连接并检测是否可用
+ 3. 站点提供的信息更新周期不详，失效后重新运行本程序即可重新检测
-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
+ 博客链接：http://saltedfish.org
+ 源码链接：https://github.com/demoToGrn/sslocal
-------------------------------------------------
+ 目前可供选择的站点：
+ i：ishadowx      w：wuwweb(推荐)
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+'''
import random
import time
from lxml import etree
import os
import requests as rq
import multiprocessing


ISHADOWX_URL = 'http://ss.ishadowx.com/'
WUWWEB_URL = 'https://www.wuwweb.com/'
MAX_RETRY = 5
USER_AGENT = [
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2226.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1',
    'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0',
    'Mozilla/5.0 (X11; Linux i586; rv:31.0) Gecko/20100101 Firefox/31.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0',
    'Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0'
]


def get_headers():
    return {'User-Agent': random.choice(USER_AGENT)}


def get_html(url, cnt=1):
    if cnt <= MAX_RETRY:
        print('>>>>> Preparing to obtain vpn:  {} / {}'.format(cnt, MAX_RETRY))
    else:
        print('>>>>> The number of connections has reached a maximum, Exit now !')
        return exit()

    try:
        r = rq.get(url=url, headers=get_headers(), timeout=10)
        if r.status_code == 200:
            return r.text
        else:
            time.sleep(2)
            return get_html(url, cnt + 1)
    except Exception:
        time.sleep(2)
        return get_html(url, cnt + 1)


def parse_ishadowx():
    html = get_html(ISHADOWX_URL)
    tree = etree.HTML(html)
    ip = tree.xpath('//div/h4[1]/span[1]/text()')
    port = tree.xpath('//div/h4[2]/span[1]/text()')
    password = tree.xpath('//div/h4[3]/span[1]/text()')
    method = tree.xpath('//div/h4[4]/text()')
    proxy_list = []
    for i in range(len(ip)):
        proxy_list.append([ip[i], port[i].strip(), password[i].strip(), method[i][7:]])
    return proxy_list


def parse_wuwweb():
    html = get_html(WUWWEB_URL)
    tree = etree.HTML(html)
    ip = tree.xpath('//div[2]/div/table[1]/tbody/tr[2]/td[2]/text()')
    port = tree.xpath('//div[2]/div/table[1]/tbody/tr[3]/td[2]/text()')
    password = tree.xpath('//div[2]/div/table[1]/tbody/tr[4]/td[2]/text()')
    method = tree.xpath('//div[2]/div/table[1]/tbody/tr[5]/td[2]/text()')
    proxy_list = []
    for i in range(len(ip)):
        proxy_list.append([ip[i], port[i][-6:-2], password[i], method[i]])
    return proxy_list


## check whether current proxy is available
def test_proxy():
    print('>>>>> Begin to detect whether the current proxy is available...')
    if os.name == 'nt':
        command = 'TASKKILL /F /T /IM %s' % 'sslocal.exe'
    elif os.name == 'posix':
        command = 'killall sslocal'
    else:
        print('Unable to identify the current system, detection function closure !')
        return True
    time.sleep(2)
    try:
        r = rq.get(url='http://www.httpbin.org/ip', headers=get_headers(), proxies={'http': 'socks5://127.0.0.1:1080'}, timeout=10)
        if r.status_code == 200:
            print('>>>>> Current proxy is available, Have a pleasant time !')
            return True
        else:
            print('>>>>> Current proxy is unavailable, is try to reset proxy...')
            os.system(command)
            print('-' * 25)
            return False
    except Exception:
        print('>>>>> Current proxy is unavailable, is try to reset proxy...')
        os.system(command)
        print('-' * 25)
        return False


## Execute commands at the console
def system_script(proxy):
    command = 'sslocal -s {} -p {} -k {} -m {}'.format(proxy[0], proxy[1], proxy[2], proxy[3])
    print('>>>>> ' + command)
    os.system(command)


def run():
    choice = input('>>>>> Please choice one web to connect(i/w)：')
    if choice.lower() == 'i':
        proxy_list = parse_ishadowx()
    elif choice.lower() == 'w':
        proxy_list = parse_wuwweb()
    else:
        print('>>>>> Please enter the right option !')
        return run()
    p = multiprocessing.Process(target=system_script, args=(proxy_list.pop(0),))
    p.start()
    while not test_proxy():
        p.terminate()
        if proxy_list:
            p = multiprocessing.Process(target=system_script, args=(proxy_list.pop(0),))
            p.start()
        else:
            print(__doc__)
            print('>>>>> There is no data to connect, is trying to reboot...')
            return run()


if __name__ == '__main__':
    multiprocessing.freeze_support()
    print(__doc__)
    run()
