## Ruby 2.3 install

http://kwski.net/linux/1223/

```
$ sudo apt-add-repository ppa:brightbox/ruby-ng
$ sudo apt-get update
$ sudo apt-get install ruby2.3
```

## Install Redis

```
$ sudo apt-get install redis-server
```

### Register to upstart

https://gist.github.com/bdotdub/714533

systemd ではなく upstart を使うにいたった背景。今のところはデフォルトは upstart のようなので。
[Upstart Jobをsystemd Unitに変換する - gihyo.jp](http://gihyo.jp/admin/serial/01/ubuntu-recipe/0358)
[Ubuntuにおけるinitと起動方法 - kotaroito's notes](http://kotaroito.hatenablog.com/entry/2015/06/20/100240)

## Install Node.js

https://nodejs.org/en/download/package-manager/#debian-and-ubuntu-based-linux-distributions

## Xvfb for Electron

[Setup Electron on Ubuntu](http://fraserxu.me/2016/01/29/setup-electron-on-ubuntu/)

上記サイトの手順で一通り Electron が動作する Xvfb の環境ができあがります。Electron ベースの nightmare も動作。

### firefox や Chrome を使う xvfb を利用する例

今回は Electron に焦点をあてましたが参考までに。

- [The Jenkins + selenium + headless browser nightmare](http://t0k4rt.github.io/2015/04/15/jenkins-selenium-firefox/)
- [Xvfb を利用したヘッドレスブラウザテスト - Qiita](http://qiita.com/kt3k@github/items/cea3c6de3c2337004a84)
- [Headless Browser Testing With Xvfb - toby ho](http://tobyho.com/2015/01/09/headless-browser-testing-xvfb/)
 
## Install hubot

[Hubot のインストール - Qiita](http://qiita.com/bouzuya/items/11c0c6da2b3ad54b827f)

yo で入れると、何故か失敗する。以下のサイトのようにデフォルトで generate すると回避できた。

["yo hubot" fails on ubuntu 14.04.](https://github.com/github/hubot/issues/1178)

```
yo hubot --defaults 
```

[Hubot を Amazon EC2 にセットアップし、Slack と連携する！ - Qiita](http://qiita.com/hkusu/items/3e3695450f8a4f9389b3)

Slack アダプタの設定は上記サイトを参考に。といっても `npm install hubot-slack --save` して 3 つの環境変数の設定をして hubot を起動するだけ。

### hubot のデーモン化

- [hubotと戯れてみる #番外編 hubotをデーモン化する - bit Wave](http://bitwave.showcase-tv.com/hubot%E3%81%A8%E6%88%AF%E3%82%8C%E3%81%A6%E3%81%BF%E3%82%8B-%E7%95%AA%E5%A4%96%E7%B7%A8-hubot%E3%82%92%E3%83%87%E3%83%BC%E3%83%A2%E3%83%B3%E5%8C%96%E3%81%99%E3%82%8B/)
- [hubotをforeverでデーモン化するときにハマった - Qiita](http://qiita.com/kacky69/items/ee806b8c17bbd70ca55e)
 
上記を参考にすれば問題無いです。

一応 Upstart を使う方法もありますが、`forever` でいいでしょう。
[Hubot Upstart Script - gist](https://gist.github.com/DavidWittman/1983925)
