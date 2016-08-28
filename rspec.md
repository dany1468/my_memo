### 引数付きの yield を伴うメソッドの sub

[RSpec: Stubbing a method that takes a block](https://makandracards.com/makandra/1321-rspec-stubbing-a-method-that-takes-a-block)

```ruby
allow(dummy).to receive(:method_with_yield).and_yield('yield argument')
```
