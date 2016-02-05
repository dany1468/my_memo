# Ruby

- [matt-morris/has_archive](https://github.com/matt-morris/has_archive)
  - archive 対象毎に別に archive 用テーブルを作り、archive 時には、そちらに移動させる
  - restore 時には archive テーブルからデータを読み出し削除し、元のテーブルに書き戻す
- [arkency/rails_event_store](https://github.com/arkency/rails_event_store/tree/master/lib/rails_event_store)
  - [arkency/ruby_event_store](https://github.com/arkency/ruby_event_store)
- [rails/actionpack-action_caching](https://github.com/rails/actionpack-action_caching)
- [rocketjob/rails_semantic_logger](https://github.com/rocketjob/rails_semantic_logger)
  - [rocketjob/semantic_logger](https://github.com/rocketjob/semantic_logger)
- [fluent/fluent-logger-ruby](https://github.com/fluent/fluent-logger-ruby) 
  - fluentd への書き出しにも使え、ログを構造化もできる
  - fluent_logger.rb で `Monitor#synchronize` が使われているので、Signal.trap 内では[利用できない](http://docs.ruby-lang.org/ja/search/query:Mutex%23synchronize/version:2.0.0/query:monitor/)
- [typicode/json-server](https://github.com/typicode/json-server)
- [r7kamura/rack-json_schema](https://github.com/r7kamura/rack-json_schema)
- [splitrb/split](https://github.com/splitrb/split)
- [chadrem/tribe](https://github.com/chadrem/tribe)
  - [chadrem/workers](https://github.com/chadrem/workers)
