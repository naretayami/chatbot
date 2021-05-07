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