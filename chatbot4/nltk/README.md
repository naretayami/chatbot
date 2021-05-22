# nltkコーパス について
chatterbotで開発を進めるのに必要

## nltkコーパス　ストップワードとは
自然言語処理する際に、一般的で役に立たない等の理由で処理対象外とする単語のこと。  
例　は　の　です　ます  
これらは、出現回数が多いのにもかかわらず役に立たない。計算量や性能に悪影響を及ぼすため、除去する必要がある。

<br>

参照：  
[自然言語処理における前処理の種類とその威力](https://qiita.com/Hironsan/items/2466fe0f344115aff177)


***

nltkに日本語用ストップワードが収録されていなかった  
→ストップワードを作成(以下参照)  
http://svn.sourceforge.jp/svnroot/slothlib/CSharp/Version1/SlothLib/NLP/Filter/StopWord/word/Japanese.txt  
c:/(省略)/nltk_data/corpora/stopwords  
に追加