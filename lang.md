- Ruby https://docs.ruby-lang.org/ja/2.3.0/doc/index.html
- Rust http://rust-lang-ja.org/rust-by-example/
- PHP https://secure.php.net/manual/ja/index.php
- Swift https://developer.apple.com/library/content/documentation/Swift/Conceptual/Swift_Programming_Language/TheBasics.html#//apple_ref/doc/uid/TP40014097-CH5-ID309

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
