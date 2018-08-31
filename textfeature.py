#coding:utf-8
# 数学ライブラリNumPy
from numpy import *
# 正規表現表現を使った文字列処理ライブラリre
import re
# 英単語の語幹を取り出すporter2というプログラムのstem関数を提供するstemmingライブラリ
# もし、stemming モジュールがインストールされてない場合は、porter2.pyをpythonを起動するディレクトリに置いて
# 以下のコマンドに置き換える。
from porter2 import stem
#from stemming.porter2 import stem
# 関数形式の標準演算子ライブラリoperator. ソートにおいてタプル内のキーの位置を指定するitemgetterを使用
from operator import *

# 指定された英文記事のファイルfile_nameから，タイトルのリスト，単語のリスト，各記事に何回その単語が出現したかを表す行列を返す
# 行列の各行が１つの記事に対応し，各列か１つの単語に対応する．(i,j)成分は記事iに単語jが何回出現したかが格納される．
def get_matrix(file_name):
    # 辞書オブジェクトallwordsを空で初期化
    allwords={}
    # リストオブジェクトarticlewordsとtitkesを空で初期化
    articlewords=[]
    titles=[]
    art_no=0
    # 記事のファイルをオープン
    f=open(file_name)
    # 最初の行をlineに読み込む
    line=f.readline()
    # ファイル内の各行を１行ずつ最後の行まで処理する
    while line:
        # 記事の単語辞書を空で追加(後でart_noでアクセスできるように初期化)
        articlewords.append({})
        # "|"で分けてリストにし，最初の要素をタイトルリストに追加
        titles.append(re.split('\|',line)[0])
        # １文字以上の任意の非英数文字列で分割してリストにし，リスト要素のうち４文字以上の文字列のリストをセット
        words=[s.lower() for s in re.split('\W+',line) if len(s)>3]
        # wordsリスト内の各文字列を処理
        for word in words:
            # 語幹を取り出す
            word_stem=stem(word)
            # word_stemがキーとして辞書allwordsに登録されていなければ要素'word_stem:0'をallwordsに追加
            ###### ここにコーディング　######
            allwords.setdefault(word_stem,0)
            # 辞書allwordsに登録されているキーword_stemの値を１増やす
            allwords[word_stem] = allwords[word_stem] + 1
            ###### ここにコーディング　######
            # word_stemがキーとして処理中の記事の単語辞書articlewords[art_no]に登録されていなければ'word_stem:0'をarticlewords[art_no]に追加
            articlewords[art_no].setdefault(word_stem,0)
            # 処理中の記事の単語辞書articlewords[art_no]に登録されているキーword_stemの値を１増やす
            articlewords[art_no][word_stem]+=1;
        # 次の行をlineに読み込む
        line=f.readline()
        art_no+=1
    f.close
    # 出現単語の内，２回以上出現したもののみwordvecに入れる
    wordlist=[]
    for w,c in allwords.items():
        if c>1:
            wordlist.append(w)
    # タイトルのリスト，単語のリスト，各記事に単語は何回出現したかの行列を返す．
    # 記事art_noに出現する単語はarticlewords[art_no]に格納されているが，その内，wordvecに格納されているもののみ使って行列を作る
    return titles,wordlist,matrix([[(word in f and f[word] or 0) for word in wordlist] for f in articlewords])

# i番目の記事のタイトルと単語リストを出力する．
def article_info(titles,wordlist,A,i):
    print titles[i]
    for j in range(shape(A)[1]):
        if A[i,j]>0: print " ",wordlist[j],":",A[i,j],
    print
    return

# NMFにかけた結果を分析してresult_fileに出力する
def analyze_nmf_result(U,V,titles,wordvec,result_file='result.txt'):
    out_file=open(result_file,'w')
    dim,column_dim=shape(V)
    row_dim=len(titles)

    # Vの各行iを処理する
    for i in range(dim):
        # Vのi行目の成分値V[i,j]の大きい方から６個をそれに対応する単語wordvec[j]と共に出力する
        ###### ここにコーディング　######
        words=[]
        for j in range(column_dim):
              words.append((wordvec[j],V[i,j]))
        for word in sorted(words,key = itemgetter(1),reverse=True)[0:6]:
              out_file.write(str(word)+'\n')
        # Uの$i$列目の成分値U[j,i]の大きい方から3個をそれに対応する記事のタイトルtitles[j]と共に出力する
        articles=[]
        for j in range(row_dim):
            articles.append((titles[j],U[j,i]))
        for art in sorted(articles,key=itemgetter(1),reverse=True)[0:3]:
            out_file.write(str(art)+'\n')

        # 1行あける
        out_file.write('\n')

    out_file.close()
    return

