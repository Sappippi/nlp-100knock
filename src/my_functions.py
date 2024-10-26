import random as rd

def n_gram(sentence: str | list | tuple, 
           n: int = 2, mode: str = "word") -> list:
    """
    シーケンスからn-gramを作る関数.
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
    """
    引数x, y, zを受け取り「x時のyはz」という文字列を返す関数.
    """
    return str(x) + "時の" + y + "は" + str(z)

def cipher(message: str):
    """
    与えられた文字列を一定の規則に従い変換する.
    文字列中の英小文字のみを (219-文字コード) の文字に置き換える. 
    """

    rslt = [c for c in map(lambda x: chr(219-ord(x)) if x.islower() else x, message)]
    
    return "".join(rslt)

def str_shuff(sentence):
    """
    与えられた文字列の文字をランダムに並べ替える.
    """
    length = len(sentence)
    rslt = "".join(rd.sample(sentence, length))

    return rslt