# Ruby

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
- [twitter/secureheaders](https://github.com/twitter/secureheaders)
  - Content Security Policy 等のブラウザの機能で脆弱性を軽減するためのヘッダをブラウザに合わせてだしてくれる
  - Github の例 https://github.com/blog/1477-content-security-policy
  - 3 系になって rack middleware に書きなおされた模様
- [tkbrigham/nextable](https://github.com/tkbrigham/nextable)
  - id 以外の field でも null ではない next record を取ることができる
  - 検索条件を適用した上で付きで next record を取得する `filter` という機能もある
- [Angelmmiguel/pretty_routes](https://github.com/Angelmmiguel/pretty_routes)
  - ルーティングをキレイに見れる view を提供してくれる。以前は [sextant](https://github.com/schneems/sextant) というのがあった。Rails4 からはデフォでも十分キレイに見せてくれる。
  - `ActionDispatch::Routing::RoutesInspector` を使って `Rails.application.routes.routes` で取得できるルーティング情報から必要な情報を抽出し整形している。
  - 一般的にはフォーマッタを書いて、[CSV](http://qiita.com/ayasuda/items/a2b0c818e8b5efeb44cf) とか [Markdown](http://tkymtk.hatenablog.com/entry/2013/12/22/100706) とかにしてる模様。
  - `ActionDispatch::Routing::RoutesInspector` の使い方として [collect_routes](http://apidock.com/rails/ActionDispatch/Routing/RoutesInspector/collect_routes) を直接呼んでいるのが面白い。
- [nikkypx/color_route](https://github.com/nikkypx/color_route)
  - 同じく `ActionDispatch::Routing::RoutesInspector` と `Rails.application.routes.routes` を用いている
  - 配色は colorize を利用しているようだ
- [zeisler/active_enumerable](https://github.com/zeisler/active_enumerable)
  - おー、面白い。`Base` で `Enumerable` をいきなり `to_a` しちゃってるように見えるが、それはいいのだろうか。
  - `english_dsl` は、英語なれてしないので名前付けの参考になります。
- [statusify/statusify](https://github.com/statusify/statusify)
  - サービスのインシデント等の発生時に別アプリとしてユーザーに通知できる。インシデントの登録等も基本は UI からする想定。
  - サービスのユーザーはこのページに来ると、メール通知を受け取るように email で activation できる。（その時に確認メールが来る）
  - インシデント発生時にはもメールが送らてくる。
  - 各通知に加えて、インシデントのキャッシュを作る処理も Sidekiq で非同期に実行される。
  - schema.rb に `delayed_jobs` というテーブルがあるが、これは。。。ゴミかな。
- [girishso/pluck_to_hash](https://github.com/girishso/pluck_to_hash) 
  - pluck の結果を多重配列ではなくて、ちゃんと hash として返してくれる。実装も割りと愚直だけど便利。 
- [hyperoslo/gamification](https://github.com/hyperoslo/gamification)
- [FetLife/rollout](https://github.com/FetLife/rollout)
- [sinsoku/tachikoma_ai](https://github.com/sinsoku/tachikoma_ai)
  - これは。deppbot がいらなくなってしまう。
  - `Tachikoma::Application#pull_request` を拡張すればメッセージの内容いじれると知った

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

## Architecture

- [Trailblazer](http://trailblazer.to/)
- [xo8bit/faat](https://github.com/xo8bit/faat)
  - service と form を提供
  - 実装は form は virtus, service は特に何もしない（method_missing とかはする）で最低限
  - 小さな generator の実装の参考に

## Archive

- [matt-morris/has_archive](https://github.com/matt-morris/has_archive)
  - archive 対象毎に別に archive 用テーブルを作り、archive 時には、そちらに移動させる
  - restore 時には archive テーブルからデータを読み出し削除し、元のテーブルに書き戻す
- [johnotander/archivable](https://github.com/johnotander/archivable)
  - テーブルに `archived` カラムを付ける単純なもの。controller の helper を追加したりしているが、あまり特徴が無い。

## Testing

### Redis

- [brigade/mock_redis](https://github.com/brigade/mock_redis)
- [guilleiguaran/fakeredis](https://github.com/guilleiguaran/fakeredis)
  - 実装を比較していないが、両方とも evalsha は無い。transaction 系はある。

## Fun

- [johnnyt/cowsay](https://github.com/johnnyt/cowsay)
  - 渡した文字列を吹きだしの中に入れて ASCII art のキャラクターと一緒にコンソールに出してくれる。面白いなぁ。
