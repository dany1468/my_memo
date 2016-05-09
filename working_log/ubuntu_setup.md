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
