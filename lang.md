- Ruby
  - https://docs.ruby-lang.org/ja/2.3.0/doc/index.html
- Rust
  - http://rust-lang-ja.org/rust-by-example/
  - [REPL](https://repl.it/languages/rust)
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

ActiveSupport 使うと wrap が使える

http://api.rubyonrails.org/classes/Array.html

```ruby
Array.wrap(nil)       # => []
Array.wrap([1, 2, 3]) # => [1, 2, 3]
Array.wrap(0)         # => [0]
```

#### Rust

配列はTという単一の型(訳注: ジェネリック型でも可)のオブジェクトの集合です。それらのオブジェクトはメモリ上の連続した領域に保存されます。配列は[]を用いて生成されます。サイズはコンパイル時には決定されていて、[T; size]という形で指定できます。

Ruby みたくリストみたいに使うわけではなさそうか。

```rust
// 固定長の配列（型シグネチャは冗長なので、なくても可）
let xs: [i32; 5] = [1, 2, 3, 4, 5];
let xs2 = [1, 2, 3, 4, 5];

// すべての要素を0にする場合
let ys: [i32; 500] = [0; 500];

// 部分的に取得するには
xs2[1..4][2] #=> 4 (index 1 から 4 なので、2,3,4,5 が取得され、さらにその index 2 なので 4 となる。
```

##### スライス

スライスは配列に似ていますが、コンパイル時にサイズが決定されていません。2つの部分からなり、1つは別のデータへのポインタ、もう1つはスライスの長さです。配列の一部を借用するのに使用され&[T]という型シグネチャを持ちます。

```rust
fn test(slice: &[i32]) {
  println!("length:{} 2:{}", slice.len(), slice[2]);
}
fn main() {
  let ys: [i32; 500] = [0; 500];
  test(&ys[1 .. 4]);
}  
```

配列だとサイズが決定するので上記のように `test` メソッドに配列を渡すことはできない。

#### PHP

TODO

#### Swift

TODO

### 
