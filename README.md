# english_news_analysis_byNMF

## 目的
大量の英文記事から隠れたパタンを抽出し、似てる記事をクラスタリングする

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

## 実施内容
+ 英文ニュースRSSサイトから記事を取り出す
feedparserというpythonのライブラリを使って、記事をとる。具体的な手順はこちら：\n
<a href="https://www.jianshu.com/u/1f5ac0cf6a8b" target="_blank">getnewsrss</a>
