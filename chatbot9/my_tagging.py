from chatterbot import languages
import MeCab

class MecabTagger(object):
    def __init__(self, language=None):
        """
        languageパラメータはChatterBotの初期化時に
        tagger_language='フォーマット'
        として渡します。
        """
        self.language = language
        # デフォルトではspacyの「en」モデルが使用されるので「分かち書き」に変更
        if self.language == languages.ENG:
            self.language = '-Owakati'

        self.tagger = MeCab.Tagger(self.language)

    def get_text_index_string(self, text):
        """
        bigramペアを作成するクラスメソッドです。
        この機能を使用使用するには、ChatterBot初期化時に
        tagger=MecabTagger
        のように渡します。
        bigramの要素は、「カナ文字：品詞」の形に作成されます。
        """
        bigram_pairs = []

        document = self.tagger.parseToNode(text).next

        if document:
            tokens = []
            while document.next:
                feature = document.feature.split(',')
                if feature[0] in ['補助記号', '記号']: # リスト内の要素は除外
                    pass
                else:
                    tokens.append(feature[0]) # 名詞を追加
                    tokens.append(feature[-1]) # カナ文字を追加
                document = document.next

            for index in range(2, len(tokens), 2): # bigramペア「カナ：品詞」を作成
                bigram_pairs.append('{}:{}'.format(
                    tokens[index - 1],
                    tokens[index]
                ))

        if not bigram_pairs:
            document = self.tagger.parseToNode(text).next
            while document.next:
                feature = document.feature.split(',')
                if feature[0] in ['補助記号', '記号']:
                    pass
                else:
                    bigram_pairs.append(
                            feature[-1]
                    )
                document = document.next

        return ' '.join(bigram_pairs)