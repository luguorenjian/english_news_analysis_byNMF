# english_news_analysis_byNMF

## 目的
**抽象的：ビックデータ解析**<\n>
**具体的：大量の英文記事から隠れたパタン（トピック）を抽出し、似てる記事をクラスタリングする**

## 原理
世の中のデータは成分が非負値で表されるものが多い. 例えば：
+ 各ドキュメントが各単語をいくつ含んでいるかのデータ
+ 各ユーザが各商品をいくつ購入したかのデータ

例： 

|  |商品A|商品B|商品C|商品D|商品E|
|--|:--:|:---:|:--:|:--:|---:|
|ユーザ１|１|１|２|１|３|
|ユーザ２|２|３|３|４|４|
|ユーザ３|１|１|２|１|３|
|ユーザ４|１|２|１|３|１|

このデータを非負値行列 X としてあらわす、非負値行列の積 U * V で分解
<img src="https://github.com/luguorenjian/english_news_analysis_byNMF/blob/master/nmf.png" width=600 height=200 />

これで解釈がしやすい! 
+ 各ユーザの購買ベクトル(行ベクトル)は、２つの購買パターンu1=(1,1,2,1,3)とu2=(1,2,1,3,1)の線形和　
+ ユーザ１,2,3,4の購買ベクトルはそれぞれu1,u2方向の成分が(1,0),(1,1),(1,0),(0,1)のベクトル 

このように一つの非負値行列を二つの非負値行列の積で分解する方法をNMF(Nonnegative Matrix Factorization)と呼ぶ。実は、一般の非負値行列 X に対して、U と V を求めるのは数学的にNP問題であることが知られている。ここで中村先生(機械学習とパタン認識という授業を担当する先生)から助けをもらって、近似解を求める方法が開発されていることがわかった。具体的な方法はこちら： 

<img src="https://github.com/luguorenjian/english_news_analysis_byNMF/blob/master/nmf更新ルール.png" width=500 height=450 />
このアルゴリズムを実装したファイルはこちら：<a href="https://github.com/luguorenjian/english_news_analysis_byNMF/blob/master/nmf.py" target="_blank">nmf.py</a>

## 実施内容
1. **データの取得。英文ニュースRSSサイトから記事を取り出す。feedparserというpythonのライブラリを使って、記事をとる。具体的な手順はこちら：
<a href="https://github.com/luguorenjian/english_news_analysis_byNMF/blob/master/getnewsrss.py" target="_blank">getnewsrss.py</a> 取り出された記事はこちら：<a href="https://github.com/luguorenjian/english_news_analysis_byNMF/blob/master/news.txt" target="_blank">news.txt</a>**
2. **前処理。取られた記事を行列に入れる。入れる前に前処理が必要である。なぜなら、英語は日本語のような活用形がある。例えば、sleep,sleeps,sleepingは一緒の意味を持っている。もしこれらを違う意味を持つ単語として行列に入れれば、行列の大きさはすごく大きくなり、行列分解の効率が低い。なので、ここではporter2 stemming algorithmを使って、英単語の語幹だけを取り出す。またはひとつの記事に二回以上出ている単語だけを行列に入れること。これも行列の大きさをコントロール方法の一つ。最終的に得られた行列はこういう感じである、中の数字はそれぞれの単語の出現頻度である：**

|  |単語１|単語２|単語３|単語４|...|
|--|:--:|:---:|:--:|:--:|---:|
|記事１|０|４|２|２|...|
|記事２|２|０|３|４|...|
|記事３|０|０|２|０|...|
|...|...|...|...|...|...|
3. **行列分解。実装したnmf.pyを使って、行列分解する**
## 結果
結果を図表であらわす、抽出されたパタンをここではトピックと呼ぶ、単語は関連度順位で並ぶ：

|  | | | | |...|
|--|:--:|:---:|:--:|:--:|---:|
|トピック１|nation|unit|monday|general|...|
|トピック２|kill|after|china|taiwan|...|
|トピック３|from|spain|catalan|elect|...|
|トピック４|state|islam|syria|iraq|...|
|...|...|...|...|...|...|
|トピック10|...|...|...|...|...|

**結論①：10個のトピックが抽出され、それぞれのトピックの後ろについてる単語はどういう意味かというと、ある特定のトピックと関連している記事にはこういう単語がよく出てくるよという意味である。例えば、トピック２と関連する記事には、kill,after,china,taiwanの四つの単語が出やすい。**

それぞれのトピックと一番関連度の高い三つの記事を示す(タイトルだけ)：

_トピック１_
- 'At UN event, speakers call for end to Syria barrel bombs '
- 'Austrian minister: Deal with Assad _ but only short term '
- 'Key Leaders to Watch at the United Nations General Assembly '

_トピック２_
- 'Typhoon Dujuan reaches mainland China after killing 2 in Taiwan '
- 'Typhoon Dujuan kills two in Taiwan, arrives in eastern China '
- 'Typhoon makes landfall in eastern China; two dead in Taiwan '

_トピック３_
- 'Catalan Separatists Win Elections But Face Challenges In Breakaway From Spain '
- 'Catalan head indicted for calling referendum on split from Spain '
- 'Catalan separatist parties win parliament vote in Spain '

_トピック４_
- 'Coalition fighting Islamic State launch 17 airstrikes in Syria, Iraq '
- 'Iraq: Dozens killed in clashes with Islamic State, coalition airstrikes across Anbar province '
- 'Iraq says it will network Islamic State intelligence with Russia, Syria and Iran '

_..._

**結論②：トピック２に注目。三つの記事のタイトルを読めば、実は全部一つのことを報道しているに違いない。つまり、トピック２と関連してる記事はお互いに関連性が高いことがわかる、また上に示した通り、確かにkill,after,china,taiwanの四つの単語はこれらの三つの記事には出やすいことは直感的にわかる。これで、似ている記事をクラスタリングできた。実験は成功である。**

## 感想
1. 前処理が不十分。例えば、afterという単語は実はどの文章でも頻繁に出ている、トピックの抽出にはあまり役に立たない、もしこういうstopwordsを前処理のところですでに処理すれば、もっといい結果が得られるかもしれない。
2. パラメータの選択問題。行列分解を実施の際に、パタン（トピック）の数（この実験では10）を決めなければならない。このパラメーターは記事の数による、直感的に決めただけで、もし自動的にこのパラメーターを最適化できるアルゴリズムも実装すれば、もっといい結果が得られるかもしれない。
3. 応用について。実は、nmfというアルゴリズムは画像処理の分野でも応用できる。これについても今後の課題になれると思う。




