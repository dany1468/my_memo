# Ruby

- [matt-morris/has_archive](https://github.com/matt-morris/has_archive)
  - archive 対象毎に別に archive 用テーブルを作り、archive 時には、そちらに移動させる
  - restore 時には archive テーブルからデータを読み出し削除し、元のテーブルに書き戻す
- [arkency/rails_event_store](https://github.com/arkency/rails_event_store/tree/master/lib/rails_event_store)
  - [arkency/ruby_event_store](https://github.com/arkency/ruby_event_store)
- [rails/actionpack-action_caching](https://github.com/rails/actionpack-action_caching)
- [typicode/json-server](https://github.com/typicode/json-server)
- [r7kamura/rack-json_schema](https://github.com/r7kamura/rack-json_schema)
- [chadrem/tribe](https://github.com/chadrem/tribe)
  - [chadrem/workers](https://github.com/chadrem/workers)
- [instructure/switchman](https://github.com/instructure/switchman)
- [makandra/query_diet](https://github.com/makandra/query_diet)
  - 画面表示のための 1 リクエストで何回 SQL が投げられているかを画面に表示してくれる。
  - widget ぽいのを画面に表示する参考になる。
- [zendesk/active_record_inherit_assoc](https://github.com/zendesk/active_record_inherit_assoc) 
  - `belongs_to`, `has_many,has_one` 関連のそれぞれで inherit_from or inherit のキーワードが指定できる。親となるオブジェクトを渡して子を生成すると、値を親からそのままコピーしてくれる。親と子の関連として、継承指定したカラムでの絞込も可能にしてくれる。
  - まだ使いみちがピンときてないが、なんか面白そう
  - 実装は ActiveRecord に問答無用でパッチあてる感じ
- [ridiculous/usable](https://github.com/ridiculous/usable)
  - include した module のうち、`usable` と `only` キーワードで指定したものだけを include できる
  - include する module のさらに inner module を同様に include できる。（その場合は親 module のメソッドは全て include されるし、名前が被ると親が優先される）
  - `only` の実装方法は `remove_method` を使っている。
  - 設計として微妙というのはあるが、確かに複数 class に include したいメソッドのうち、ここではこれだけというのはやりたいことあるなぁ。

## Logging

- [rocketjob/rails_semantic_logger](https://github.com/rocketjob/rails_semantic_logger)
  - [rocketjob/semantic_logger](https://github.com/rocketjob/semantic_logger)
- [fluent/fluent-logger-ruby](https://github.com/fluent/fluent-logger-ruby) 
  - fluentd への書き出しにも使え、ログを構造化もできる
  - fluent_logger.rb で `Monitor#synchronize` が使われているので、Signal.trap 内では[利用できない](http://docs.ruby-lang.org/ja/search/query:Mutex%23synchronize/version:2.0.0/query:monitor/)

## AB Testing

- [splitrb/split](https://github.com/splitrb/split)
- [amatsuda/motorhead](https://github.com/amatsuda/motorhead)
- [lucaong/ablab](https://github.com/lucaong/ablab)
  - AB テスト用のモジュールはベタに実装するが、トラッキング機能と確認用の View が用意されてる
  - トラッキング情報のストア先ははメモリか Redis か選べる
