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

このデータを非負値行列としてあらわす、非負値行列の積で分解
![](https://github.com/luguorenjian/english_news_analysis_byNMF/blob/master/nmf.png)

これで解釈がしやすい! 
+ 各ユーザの購買ベクトル(行ベクトル)は、２つの購買パターンu1=(1,1,2,1,3)とu2=(1,2,1,3,1)の線形和　
+ ユーザ１,2,3,4の購買ベクトルはそれぞれu1,u2方向の成分が(1,0),(1,1),(1,0),(0,1)のベクトル

