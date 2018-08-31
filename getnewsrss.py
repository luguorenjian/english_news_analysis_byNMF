#coding:utf-8
# 英文ニュースのRSSサイトのリスト
feedlist=['http://feeds.reuters.com/reuters/worldNews',
          'http://www.nytimes.com/services/xml/rss/nyt/International.xml',
          'http://feeds.bbci.co.uk/news/world/rss.xml',
          'http://feeds.abcnews.com/abcnews/internationalheadlines',
          'http://rss.cbc.ca/lineup/world.xml',
          'http://www.usnews.com/rss/news',
          'http://feeds.skynews.com/feeds/rss/world.xml',
          'http://www.npr.org/rss/rss.php?id=1004',
          'http://rss.upi.com/news/tn_int.rss']

# HTMLタグを取り除く
def stripHTML(h):
    p=''
    s=0
    for c in h:
        if c=='<': s=1
        elif c=='>':
            s=0
            p+=' '
        elif s==0: p+=c
    return p.rstrip()

# feedparserというライブラリのparse関数を用いてRSSから情報を取り出す．
from feedparser import *

for feed in feedlist:
    f=parse(feed)
    for e in f.entries:
        # RSSのtitleとdescriptionの項目を抜き出し"|"で区切って出力する．
        # ただし、descriptionはHTMLタグを含んでいる可能性があるため、それらを削る．
        print e.title.encode('utf8'),"|",stripHTML(e.description.encode('utf8'))
