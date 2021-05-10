# chatbotを開発するうえで困ったこと

## spacy
### 前提
spacyってなに？？？

### 状況
とりあえず、
pip install chatterbot
をしたときに勝手についてきた。バージョンは3.0.6
しかし、日本語の解析が上手くいかない＆英語のチュートリアルしかなく分かりづらい

### やったこと
pip install spacy=2.3.0
spacyをダウングレードして2系にした。
→spacy公式のチュートリアルで勉強しやすい

python -m spacy validate
どの言語の統計モデルがインストールされていて利用できるか確認できる


spacy.pyのファイルを作ってpython spacy.pyをやったら、spacyという名前のモジュールはありませんになってしまった。
→再起動＆pra.pyに変更したらなおった

意味
- >>> import spacy
- >>> spacy.explain("dobj")
 - 'direct object'
- >>> spacy.explain("NNP")
 - 'noun, proper singular'
- >>> spacy.explain("GPE")
 - 'Countries, cities, states'

### spacyのお勉強
- 言語、パイプライン、ライセンスが記載されているメタファイル(meta.json)がある
- 品詞タグ、依存関係ラベル、小結表現等の言語特徴量の抽出をするため機械学習の重みがある
- モデルの語彙データの文字列(strings.json)とそのハッシュ値がある
- 機械学習モデル作成に使ったラベル付きデータはない。予測には学習データが不必要。


#### 参考
spaCyを使った先進的な自然言語処理
https://course.spacy.io/ja