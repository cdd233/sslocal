<h1 align="center">Proxy</h1>

<p align="center">这是一个自动连接代理的脚本，说白了就是翻墙啦！</p>


> 以下 `Windows` 和 `Linux` 下的安装都建议搭配浏览器插件 [`SwitchyOmega`][SwitchyOmega] 一起使用！
>
> 仅支持浏览器代理（也许你懂得更多，希望可以分享一下！）


## Installation_01（Windows）

### `python` > `pip` > `requests`/`lxml`/`shadowsocks` > `openssl` > `proxy` > `switchyomega`（[参考链接][Install-Shadowsocks-Server-on-Windows]）

Step01. 下载并安装适用于 `Windows` 的 [`Python`][Python]

Step02. 在安装过程中，勾选安装 `pip` 以及勾选 `Add Python to environment variables` 添加 `python` 到环境变量

Step03. 安装 `requests`、`lxml` 和 `shadowsocks`，在 `cmd` 中运行：
```bash
$ pip3 install requests
$ pip3 install lxml
$ pip3 install shadowsocks
```

Step04. 安装 `shadowsocks` 所依赖的 [`OpenSSL`][OpenSSL]，如果你安装了 64 位 `Python`，则应安装 64 位 [`OpenSSL`][OpenSSL]

Step05. 下载 [`proxy.py`][proxy] 最新版本，双击即可运行

Step06. 下载 [`SwitchyOmega`][SwitchyOmega] ，适合自己浏览器（chrome/firfox）的插件，即可自由切换代理！

## Installation_02（Linux）

### `python` > `requests` > `shadowsocks` > `proxy` > `switchyomega`
参考 `Windows` 的安装吧，不测试了，我用的是 `archlinux` ，以下内容都是凭记忆写，只少不多

Step01. 安装 `python`、`lxml` 和 `ishadowsocks`
```bash
$ sudo pacman -S python
$ pip3 install requests
$ pip3 install lxml
$ pip3 install shadowsocks
```

Step02. 下载 [`proxy.py`][proxy] 最新版本，运行脚本
```bash
$ python proxy.py
```

Step03. 下载 [`SwitchyOmega`][SwitchyOmega] ，适合自己浏览器（chrome/firfox）的插件，即可自由切换代理！


## BUG
> 建议或优化[点这里][Issues] ，有 `建议` 或着 `BUG` 随便提啊，反正我也懒得回复。


## FAQ

```doc
Q：为什么会突然写这个脚本？
A：穷啊，只舍得用某些站点提供的免费酸酸乳；
   很多免费酸酸乳都得自己手动去站点获取，然后再一个一个输入，再启动，
   但是我懒啊，我觉得这个过程完全可以让 python 帮我去完成啊。
```

```doc
Q：这个脚本可以一直用吗?
A：显然这是不能的：
   1. 因为网站提供的这些信息本身就是敏感的，所以站点什么时候突然 404 我也不知道；
   2. 网站提供的酸酸乳可用周期以及更新周期都是不确定的；
   所以失效了的时候还得重新运行脚本，获取新的酸酸乳，这家不行找下家嘛！
```

```doc
Q：PC 环境里没 python 啊，可不可以弄个独立的可执行程序呢？
A： v1.x 版本就有 exe，但是夭折了！
   用 pyinstaller 打包发布，想着这样就可以给不用 python 的人用了，
   但是拷贝到一个新的环境中运行，发现很多东西都缺失了，跑不起来！
   shadowsocks 和 openssl 不晓得怎么一起给打包进去，
   花在这个小脚本身上的时间太多了，意义不大，所以立马终止了！
   我自个用着带着我网站 logo 的 exe 程序，看着还是挺舒服的，哈哈！
```

```doc
Q：如果我不想装那么多东西，只想用怎么办？
A：你可以到我源码文件里面，找到我抓取的站点的网址呀，你自个儿登上去随便换！酸酸乳客户端推荐用 shadowsocks
```

```doc
Q：你是弱鸡吗？
A：很遗憾地告诉你，是的。脚本初衷是自用，但是写出来了之后呢，感觉这个东西话可以持续更新的呀，
   那我用来熟悉一下软件的迭代更新是怎样的，还可以顺便练一下 git ，完美！
```

> 如果这个脚本能帮上你忙，那么，万分荣幸！如果对你造成了困扰，兄dei，这不是你自己找的吗...



[SwitchyOmega]:https://github.com/FelisCatus/SwitchyOmega
[Install-Shadowsocks-Server-on-Windows]:https://github.com/shadowsocks/shadowsocks/wiki/Install-Shadowsocks-Server-on-Windows
[Python]:https://www.python.org/downloads/windows/
[OpenSSL]:https://slproweb.com/products/Win32OpenSSL.html
[proxy]:https://github.com/demotogrn/sslocal/releases
[Issues]:https://github.com/demotogrn/sslocal/issues/new