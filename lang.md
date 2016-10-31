- Ruby
  - https://docs.ruby-lang.org/ja/2.3.0/doc/index.html
- Rust
  - http://rust-lang-ja.org/rust-by-example/
- PHP
  - https://secure.php.net/manual/ja/index.php
  - [REPL](http://phpepl.herokuapp.com/)
- Swift
  - https://developer.apple.com/library/content/documentation/Swift/Conceptual/Swift_Programming_Language/TheBasics.html#//apple_ref/doc/uid/TP40014097-CH5-ID309
  - [REPL](https://swiftlang.ng.bluemix.net/#/repl)

## Comment

### Ruby

```ruby
# this is a comment line
```
スクリプト言語の習慣にならい、文字列中や数値リテラル `?#' 以外の #から行末までをコメントと見なします。

### Rust

通常のコメント これはコンパイラによって完全に無視されます。
```rust
// 行末までコメントアウト
/* ブロックによって囲まれた部分をコメントアウト */
```

ドキュメンテーションコメント ライブラリのドキュメンテーションとしてhtmlにパースされます。
```rust
/// このコメントの下の内容に関するドキュメントとなります
//! このコメントを含むソースのドキュメントになります
```

### PHP

```php
<?php
echo 'テストです'; // C++型の単一行用のコメント
/* 複数行用のコメント
   もう一行分のコメント */
echo 'もうひとつのテストです';
echo '最後のテストです'; # シェル型の単一行用のコメント
?>
```

### Swift

```swift
// This is a comment.
/* This is also a comment
 but is written over multiple lines. */
```

## 行末のセミコロン

|Ruby|Rust|PHP|Swift|
|:--|:--|:--|:--|
|不要<br>1 行で書きたい時は付けることも|式して扱う場合にはつける。<br>付けることが多い|必要|Ruby と同じ|

## Array

### 初期化

#### Ruby

https://docs.ruby-lang.org/ja/latest/class/Array.html

```ruby
[1, 2, 3]
Array[1, 2, 3]
Array.new([1, 2, 3])
```

Size を指定して初期化

```ruby
ary = Array.new(3, "foo")
p ary                     #=> ["foo", "foo", "foo"]
ary[0].capitalize!
p ary                     #=> ["Foo", "Foo", "Foo"]  (各要素は同一のオブジェクトである)
```

```ruby
ary = Array.new(3) {|i| "foo" }
p ary                      #=> ["foo", "foo", "foo"]
ary[0].capitalize!
p ary                      #=> ["Foo", "foo", "foo"]  (各要素は違うオブジェクトである)
```

この初期化使ったことなかったな 😳

#### Rust

