import random as rd
import re


def n_gram(sentence: str | list | tuple, 
           n: int = 2, mode: str = "word") -> list:
    """ シーケンスからn-gramを作る関数.
    入力は英単語とコンマとピリオドから成る英文を想定している.
    """

    if isinstance(sentence, str):
        sentence = sentence.replace(",", "").replace(".", "")
        sentence:list = sentence.split(" ")

    total_elements = len(sentence) // n

    if mode == "word":
        rslt = [" ".join(sentence[i:i+n]) for i in range(0, len(sentence), total_elements)]
    elif mode == "letter":
        rslt = "".join(sentence)
        rslt = ["".join(rslt[i:i+n]) for i in range(0, len(rslt), n)]

    return rslt


def generate_str_by_template(x: int, y: str, z: int) -> str:
    """ 「x時のyはz」という文字列を返す関数.
    """
    return str(x) + "時の" + y + "は" + str(z)


def cipher(message: str):
    """
    与えられた文字列を一定の規則に従い変換する.
    文字列中の英小文字のみを (219-文字コード) の文字に置き換える. 
    """
    return "".join(map(lambda x: chr(219-ord(x)) if x.islower() else x, message))


def str_shuff(sentence):
    """
    与えられた文字列の文字をランダムに並べ替える.
    """
    length = len(sentence)
    return "".join(rd.sample(sentence, length))

def extract_category_name(string: str):
    """カテゴリを含む行からカテゴリ名だけを抽出
    """
    category_name = re.sub('.+:', '', string) # カテゴリ名より前の文字列を削除
    category_name = re.sub('(\|.)?\]+(\\n)?','',category_name)
    return category_name

def print_secname_level(string: str):
    """セクション名とそのレベルを表示する
    """
    secname = string.strip('=')
    total_eqs = len(string.replace(secname,"")) # strに含まれる'='の総数
    level = total_eqs // 2 -1
    print("セクション名: ", secname, "\nレベル: ", level)

def remove_internal_link(string: str):
    """内部リンクを取り除く
    """
    internal_links = re.findall('\[\[[^\]]+\]\]',string)
    list_article_name = [re.sub('(\|[^\|^\[]+)+]]', '', article_name).lstrip("[").rstrip("]") for article_name in internal_links]

    for article in list_article_name:
        string = re.sub('\[\[[^\]]+\]\]', article, string)
    return string