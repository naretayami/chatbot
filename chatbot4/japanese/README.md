# chatterbot-corpusについて（備忘録）

## 日本語コーパス
日本語コーパスが収録されているライブラリである、chatterbot-corpusは開発者のGitHubにある最新のリポジトリからコーパスデータをインストールしました。
<br>

### 方法：  
`$ pip install git+git://github.com/gunthercox/chatterbot-corpus/@ae8ccd2912baa79cf0412c3c0822835dab64059c`


***
### 補足：  
`$ pip install chatterbot-corpus`  
では、日本語コーパスが収録されていません。そのため、もし既にこのコマンドでインストールしている場合は、一度  
`$ pip uninstall chatterbot-corpus`  
でアンインストールしてから再度インストールが必要です。

***
<br>

### 修正について
開発者のGitHubにあるコーパスデータを一部、修正しました。
主に修正したのは2点です。

1. 明らかに不自然な応答  
削除、または書き換えを行いました。  

2. 書き方のミス  
   正しい例  
`-- こんにちは`  
` - こんにちは`  
` - お元気ですか？`  

<br>

間違えている（と思われる）例  
`- こんにちは`  
`-- こんにちは`  
`-- お元気ですか？`  

