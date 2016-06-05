OAuth2 に準拠しているなら [omniauth-oauth2](https://github.com/intridea/omniauth-oauth2) を利用するといい。

facebook や github の strategy も同様のよう。

- https://github.com/mkdynamic/omniauth-facebook
- https://github.com/intridea/omniauth-github

## 基本

README にある通り。

```ruby
require 'omniauth-oauth2'

module OmniAuth
  module Strategies
    class SomeSite < OmniAuth::Strategies::OAuth2
      # NOTE strategy の名前になるので指定する。
      option :name, 'some_site'

      # NOTE user_id など unique な id。
      uid{ raw_info['id'] }

      info do
        {
          name: raw_info['name'],
          email: raw_info['email']
        }
      end

      # NOTE skip_info の判定は有効にしておいて良さそう
      extra do
        skip_info? ? {} : {raw_info: raw_info}
      end

      def raw_info
        @raw_info ||= access_token.get('/me').parsed
      end
    end
  end
end
```

## access_token について

omniauth-oauth2 で出てくる `access_token` は `oauth2` ライブラリのクラスのこと。

access_token クラス
https://github.com/intridea/oauth2/blob/master/lib/oauth2/access_token.rb

access_token 内部で使われる client と access_token の生成箇所 
https://github.com/intridea/oauth2/blob/master/lib/oauth2/client.rb#L128-L142

### access_token.get はどうなっているか

https://github.com/intridea/oauth2/blob/master/lib/oauth2/access_token.rb#L107-L117
https://github.com/intridea/oauth2/blob/master/lib/oauth2/client.rb#L88-L120

client クラスの `#request` は全てのリクエストで使われるので、まあ get での接続している実態はこういう感じと思えばいいかと。

ポイントになるのは header。以下の access_token の `#initialize` で取得したトークンをどういう形式で渡すかを設定できるのが分かる。

https://github.com/intridea/oauth2/blob/master/lib/oauth2/access_token.rb#L51-L53

デフォルトは header に `"Authorization: Bearer #{access_token}"` のような形で渡される。実際のコードは[こちら](https://github.com/intridea/oauth2/blob/master/lib/oauth2/access_token.rb#L148-L150)

もし、渡し方が異るのならこの辺はカスタマイズする必要がある。

`access_token.get` には option を渡せる。詳しくは上述した client クラスの方をみてもらうと良いがその中に `parse` オプションがある。
これは、返却された値をパースする方式を指定するのだが、デフォルトは `automatic` となっており、Content-Type によって自動で選択されるようだ。

もしも、期待通りパースされない時は Content-Type を指定したり、parse をオプションを直接指定すると良いかもしれない。

## expires と refresh_token について

今回対応した Timely API は refresh_token は返してくるが、expires を返さないという謎仕様だった。つまり、いつ expire が来るか分からない、または expire はこない。。

omniauth-oauth2 は以下のように expires 系が存在しないと refresh_token を credential 情報として認めない。

https://github.com/intridea/omniauth-oauth2/blob/master/lib/omniauth/strategies/oauth2.rb#L39-L45

もちろん、実装する Strategy 側でこの Credential を上書きすればいいのだが、考えてみれば確かに使いみちの無い refresh_token を受け取ったところで保存する気にもならない。

## Strategy の initialize について

Strategy のテストコードを書くのに、この Strategy はどういう風にインスタンス化されるのか追ってみると以下らへんにたどり着く

https://github.com/intridea/omniauth/blob/1cc1cf4b2821a7d2a4a376a5ca93c61b6bd8b5f1/lib/omniauth/strategy.rb#L129-L146
https://github.com/intridea/omniauth/blob/1cc1cf4b2821a7d2a4a376a5ca93c61b6bd8b5f1/lib/omniauth/builder.rb

Rack::Builder 継承のクラスがどのように振る舞うのかきちんと理解できていないが、Strategy は initialize 時の第一引数は Rack application いうことのようだ。
