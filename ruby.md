# Ruby

- [rails/actionpack-action_caching](https://github.com/rails/actionpack-action_caching)
- [typicode/json-server](https://github.com/typicode/json-server)
- [r7kamura/rack-json_schema](https://github.com/r7kamura/rack-json_schema)
- [chadrem/tribe](https://github.com/chadrem/tribe)
  - [chadrem/workers](https://github.com/chadrem/workers)
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
- [byroot/frozen_record](https://github.com/byroot/frozen_record)
  - YAML をデータベースとして AR のように検索や読み出しが可能
  - Scope の実装での criteria の作り方が面白い
- [clearwater-rb/clearwater](https://github.com/clearwater-rb/clearwater)
  - Opal で書くフロントエンドフレームワーク
- [jordanmaguire/seed_helper](https://github.com/jordanmaguire/seed_helper)
- [lukehorvat/env-dependencies](https://github.com/lukehorvat/env-dependencies)
  - 必要な ENV の設定状態を起動時にチェックする。
  - 簡単な起動時設定の実装参考に。
- [huacnlee/redis-search](https://github.com/huacnlee/redis-search)
- [farkasity/jekyll-diagrams](https://github.com/farkasity/jekyll-diagrams)
  - jekyll でダイアグラムを埋め込めるように。blockdiag とかも埋め込めるが、ローカルで実行してという感じ。
- [chaps-io/public_activity](https://github.com/chaps-io/public_activity) 
- [syro/satz](https://github.com/syro/satz)
  - JSON API つくるやつ
- [eprothro/perform-later](eprothro/perform-later)
  - Sidekiq のような非同期ジョブのライブラリをオブジェクトぽく使えるように
- [bbtfr/activerecord-redundancy](https://github.com/bbtfr/activerecord-redundancy)
  - 関連テーブルのカラムを非正規化するようなケースで使える。
- [MartinKoerner/deferred_associations](https://github.com/MartinKoerner/deferred_associations)
  - has_many/habtm の保存を遅延させる。どういう時使うんだろ。
- [danielpclark/faster_path](https://github.com/danielpclark/faster_path)
  - Rust で Pathname を爆速化。これはすごいな。
- [gemgento/rails_script](https://github.com/gemgento/rails_script)
  - controller や page に応じた CoffeeScript をかける。使えそうな予感。
- [sorentwo/readthis](https://github.com/sorentwo/readthis)
  - ActiveSupport の Cache 互換で Redis 利用のものに

## Rails

### Controller

- [asakusarb/action_args](https://github.com/asakusarb/action_args)

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
- [mikenichols/actionizer](https://github.com/mikenichols/actionizer)
- [andypike/rectify](https://github.com/andypike/rectify)
- [blaknite/blush](https://github.com/blaknite/blush)
  - ViewModel
- [NullVoxPopuli/skinny_controllers](https://github.com/NullVoxPopuli/skinny_controllers)
  - API 用らしい。trailblazer との対比をだしてるのが興味深い

## Archive

- [matt-morris/has_archive](https://github.com/matt-morris/has_archive)
  - archive 対象毎に別に archive 用テーブルを作り、archive 時には、そちらに移動させる
  - restore 時には archive テーブルからデータを読み出し削除し、元のテーブルに書き戻す
- [johnotander/archivable](https://github.com/johnotander/archivable)
  - テーブルに `archived` カラムを付ける単純なもの。controller の helper を追加したりしているが、あまり特徴が無い。
- [drexed/active_archive](https://github.com/drexed/active_archive)
  - `archived_at` カラムを付ける方式
- [firmafon/archiving](https://github.com/firmafon/archiving)

## RDB

### Mutli DB

- [eagletmt/switch_point](https://github.com/eagletmt/switch_point)
  - シャーディングまでいらない場合には、swith_point が R/W の切り替えと複数DB サポートだけをシンプルにやってくれていて良さそう。一方で switch_point は migration サポートが無いのでそこは別途考える必要あり。
- [taskrabbit/makara](https://github.com/taskrabbit/makara)
- [instructure/switchman](https://github.com/instructure/switchman)
- [hirocaster/activerecord-sharding](https://github.com/hirocaster/activerecord-sharding)
- [Smarre/multi_ar](https://github.com/Smarre/multi_ar)
- [kenn/slavery](https://github.com/kenn/slavery)
  - 複数DBではなく Master/Slave 切り替えのみ。コード量が少なくていい。
- [customink/secondbase](https://github.com/customink/secondbase)
  - Mast/Slave 切り替えではなく複数DB対応のみ。しかも 2 つ目しか対応しない。でもちょっとおもしろい。
- [customink/encom_dbs](https://github.com/customink/encom_dbs)
  - ライブラリではなくサンプルアプリ。establish_connection での切り替えのやり方を示してくれている。migration まであればよかったなぁ。

### suspended?

- [runeleaf/acts_as_readonlyable](https://github.com/runeleaf/acts_as_readonlyable)
- [schoefmann/multi_db](https://github.com/schoefmann/multi_db)
- [kovyrin/db-charmer](https://github.com/kovyrin/db-charmer)

### seeds

- [bpardee/data_seeder](https://github.com/bpardee/data_seeder)

## Testing

- [tomykaira/rspec-parameterized](https://github.com/tomykaira/rspec-parameterized)

### RSpec matcher

- [brigade/db-query-matchers](https://github.com/brigade/db-query-matchers)
  - クエリの発行回数は `ActiveSupport::Notifications.subscribed(@counter.to_proc, 'sql.active_record'` でカウントしている。`@counter.to_proc` が callback。

### Redis

- [brigade/mock_redis](https://github.com/brigade/mock_redis)
- [guilleiguaran/fakeredis](https://github.com/guilleiguaran/fakeredis)
  - 実装を比較していないが、両方とも evalsha は無い。transaction 系はある。
- [soveran/nest](https://github.com/soveran/nest) 

## Fun

- [johnnyt/cowsay](https://github.com/johnnyt/cowsay)
  - 渡した文字列を吹きだしの中に入れて ASCII art のキャラクターと一緒にコンソールに出してくれる。面白いなぁ。

## Security

- [rubysec/bundler-audit](https://github.com/rubysec/bundler-audit)
- [chrismo/bundler-advise](https://github.com/chrismo/bundler-advise)
  - [rubysec/ruby-advisory-db](https://github.com/rubysec/ruby-advisory-db)

## Measurement

- [evanphx/benchmark-ips](https://github.com/evanphx/benchmark-ips)

## Authentication

- [hassox/warden](https://github.com/hassox/warden)
- [halogenandtoast/monban](https://github.com/halogenandtoast/monban)
- [binarylogic/authlogic](https://github.com/binarylogic/authlogic)
- [apotonick/tyrant](https://github.com/apotonick/tyrant)
- [NoamB/sorcery](https://github.com/NoamB/sorcery)
  - メンテナ求む状態

## Authorization

- [blacklane/can-do](https://github.com/blacklane/can-do)
  - yaml で development/production のように RAILS_ENV によって feature の on/off を変更できる

## AWS

- [namusyaka/dinamo](https://github.com/namusyaka/dinamo)
  - DynamoDB の ORM
- [joker1007/redshift_simple_migrator](https://github.com/joker1007/redshift_simple_migrator)

## State Machine

- [amatsuda/stateful_enum](https://github.com/amatsuda/stateful_enum)
  - ActiveRecord enum のカラムを利用できる。見た目は AASM に似てる。
  - 設定をオブジェクトに格納する方法が勉強になる。さすが松田さん。
- [soveran/micromachine](https://github.com/soveran/micromachine)
- [sardaukar/strict_machine](https://github.com/sardaukar/strict_machine)
- [versus-systems/end_state](https://github.com/versus-systems/end_state)
- [mnelson/stator](https://github.com/mnelson/stator)
  - alias とか validates とか便利そう

## HTTP Client

- [rest-client/rest-client](https://github.com/rest-client/rest-client)
- [httprb/http](https://github.com/httprb/http)

### Faraday

- [envylabs/faraday-detailed_logger](https://github.com/envylabs/faraday-detailed_logger)

### REST Client

- [whichdigital/active-rest-client](https://github.com/whichdigital/active-rest-client)
- [flexirest/flexirest](https://github.com/flexirest/flexirest)
- [andyjeffries/flexirest](https://github.com/andyjeffries/flexirest)
- [A-Helberg/active_record-resource](https://github.com/A-Helberg/active_record-resource)
- [carwow/restful_resource](https://github.com/carwow/restful_resource)
- [liveh2o/active_remote](https://github.com/liveh2o/active_remote)
- [shvets/resource_accessor](https://github.com/shvets/resource_accessor)
  
## WebSocket

- [NullVoxPopuli/action_cable_client](https://github.com/NullVoxPopuli/action_cable_client)

## Template

- [soveran/mote](https://github.com/soveran/mote)

## TOML

- [emancu/toml-rb](https://github.com/emancu/toml-rb)

## Scraping

- [mdsol/grell](https://github.com/mdsol/grell)

## OAuth

- [intridea/omniauth](https://github.com/intridea/omniauth)
- [intridea/oauth2/](https://github.com/intridea/oauth2)
- [intridea/omniauth-oauth2](https://github.com/intridea/omniauth-oauth2)

## Event Tracking

- [arkency/rails_event_store](https://github.com/arkency/rails_event_store/tree/master/lib/rails_event_store)
  - [arkency/ruby_event_store](https://github.com/arkency/ruby_event_store)
- [ankane/ahoy](https://github.com/ankane/ahoy)

## Enum

- [redding/enumeration](https://github.com/redding/enumeration)
- [adzap/active_enum](https://github.com/adzap/active_enum)
- [beerlington/classy_enum](https://github.com/beerlington/classy_enum)

## Sidekiq

- [Moove-it/sidekiq-scheduler](https://github.com/Moove-it/sidekiq-scheduler)
- [square/sqeduler](https://github.com/square/sqeduler)
- [ccocchi/sidekiq-paquet](https://github.com/ccocchi/sidekiq-paquet)
- [TEA-ebook/sidekiq-reliable-fetch](https://github.com/TEA-ebook/sidekiq-reliable-fetch)

## SocketIO Client

- [lyondhill/socket.io-ruby-client](https://github.com/lyondhill/socket.io-ruby-client)
  - handshake もサポートしているので使いやすい
- [shokai/ruby-socket.io-client-simple](https://github.com/shokai/ruby-socket.io-client-simple)

## Define Attributes

- [solnic/virtus](https://github.com/solnic/virtus)
- [techscore/easy_model](https://github.com/techscore/easy_model)
- [kipcole9/attributable](https://github.com/kipcole9/attributable)
- [joker1007/attr_typecastable](https://github.com/joker1007/attr_typecastable)
- [dry-rb/dry-types](https://github.com/dry-rb/dry-types)
  - virtus の solnic さんがメインでやってるようで、virtus 使ってるならこっちが移行先なのかな。
