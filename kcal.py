import sys
from PIL import Image
import pyocr
import pyocr.builders
# 画像を取る
tools = pyocr.get_available_tools()

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


if __name__ == "__main__":
    main()
