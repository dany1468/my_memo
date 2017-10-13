# Prototyping Lab 第一版

サンプルコードは processing か ActionScript 3 なので、ここでは Python で書き直す事にしている。

## 準備

```
$ python3 -m venv plab
$ source plab/bin/activate
$ pip install -r requirements.txt
```

## input1: 自然光の明るさを測りたい

pymata-aio を使う。
Analog ピンのデータを取得するのに、ある間隔でのアップデートにするか、同期するかでかき分けている。

- cds_led.py: Analog ピンの情報を global の value に入れておき、ループが来る毎（サンプルでは 2 sec) に LED の出力値を買えている
- cds_led_async.py: pymata-core に切り替え、Analog ピンの情報取得時に LED の出力を書き換えている

## 参考

[Digital And Analog Data Reporting Callback Usage Guidelines - MrYsLab/pymata-aio](https://github.com/MrYsLab/pymata-aio/wiki/Digital-And-Analog-Data-Reporting-Callback--Usage-Guidelines)
pymata-aio の Callback を取得する際の方法について、pymata-core か pymata3 を使うかで書き分ける部分について解説されている。

[pymata-aio/examples/control_C_handlers/for_core.py](https://github.com/MrYsLab/pymata-aio/blob/master/examples/control_C_handlers/for_core.py)
公式の example より pymata-core のサンプル。
シグナルハンドルの例にもなっているのだが、、loop.add_signal_handler を使わないと上手く行かなかった。

[pymata-aio/examples/core_sample.py](https://github.com/MrYsLab/pymata-aio/blob/master/examples/core_sample.py)
同じく公式の example より pymata-core のサンプル。
こちらはシンプル。

[MrYsLab/pymata_aio_core_example](https://gist.github.com/MrYsLab/df8ec22ea16de6c84d67)
pymata-core のサンプル。async/await の書き方ではないがそのまま使える。

[MrYsLab/callback_example.py](https://gist.github.com/MrYsLab/0b9f125f04f171065af0)
こちらは pymata3 を使った場合の callback のサンプル

[MrYsLab/rb4s/redbot_controller.py](https://github.com/MrYsLab/rb4s/blob/master/redbot_controller.py)
作者の別プロジェクトだが、pymata-core の使い方のサンプルとして参考になる。

[technologiescollege/s2aio-control-panel](https://github.com/technologiescollege/s2aio-control-panel/blob/master/s2aio/Lib/site-packages/pymata_aio/latching.py)
pymata-core を使った latch のサンプル
loop.run_forever を使うより、while True でやるのをよく見る気がする。

[Graceful shutdown of asyncio coroutines](https://stackoverflow.com/questions/37417595/graceful-shutdown-of-asyncio-coroutines)
asyncio を使った場合のシグナルでの停止について調べていた時にであった。
最終的には以下の aiohttp のコードを参考にした。
https://github.com/aio-libs/aiohttp/blob/master/aiohttp/web.py#L460
