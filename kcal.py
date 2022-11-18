# パラメータの取得
import sys

# 画像処理
from PIL import Image

# 画像のテキストを抽出
import pyocr

# pyocrモジュールのbuilders関数()を使用
import pyocr.builders

# 日付の情報を持っているオブジェクト
import datetime

# 画像を取る
tools = pyocr.get_available_tools()


# def say_print():
#     txt = datetime in year,
#         datetime in month,
#         datetime in day


#     print(txt)

# もしも文字数が0だったら(ツールが何もなければ(ツールは配列になってる))表示して抜け出る
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)
# 推奨している順で読み込むので、配列の最初に推奨順の1つ目がはいる
tool = tools[0]
# 一番推奨しているツール(今回はtesseract)の名前をターミナルに表示する
print("Will use tool '%s'" % (tool.get_name()))
# 例: Will use tool 'Tesseract (sh)'


# メイン関数を定義
def main():

    sum = 0
    # 要素を1つずつ取り出すのを繰り返す
    for i in range(1, 6):
        # 処理
        # ①すべてのファイル
        file_path = "0" + str(i) + ".png"
        # ②画像ファイルをテキストとして読み込む
        txt = tool.image_to_string(
            Image.open(f"images/{file_path}"),  # OCRする画像
            lang="jpn",  # 学習済み言語データ
            builder=pyocr.builders.DigitBuilder(tesseract_layout=6),  # 期待される出力のタイプを指定
        )
        # ③sumを初期化してテキストから読み取った数値を繰り返し足していく
        sum += int(txt)
    # テキストファイルを開いて書いて終わるとテキストを閉じる(as=名前をつける)
    with open("text.txt", mode="w") as f:
        # f操作を終えた数値のsumテキスト全体をリストとして読み取り
        f.writelines(str(sum))


def print_kal_data():
    now = datetime.date.today()
    today = now.strftime("%Y/%m/%d/")
    with open("text.txt", "r") as r:
        sum = r.read()
    print(str(today) + "の摂取カロリーは" + str(sum) + "kcalです")


if __name__ == "__main__":
    main()
    print_kal_data()
