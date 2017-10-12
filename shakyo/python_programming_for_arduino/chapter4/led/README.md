# LED – controlling LED brightness using PWM

## setup

### Python

Mac で python3 が入っていることが前提。以下では venv でのやり方だが、実行環境が作れれば何でもいい。

```
$ python3 -m venv test
$ source test/bin/activate
$ pip install -r requirements.txt
```

### Arduino 

[Uploading StandardFirmata To Arduino](https://github.com/MrYsLab/pymata-aio/wiki/Uploading-StandardFirmata-To-Arduino)

## execute

### pyFirmata

```
$ python led_pwm.py
```

### PyMata (pymata-aio)

```
$ python led_pwm_pymata.py
```

## 感想

PyMata はドキュメントもしっかりしてるしアクティブでかつ使いやすそう。
