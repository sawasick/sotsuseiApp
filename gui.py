# ダイアログを表示するために必要なモジュール
import tkinter.filedialog as fd

# ファイル選択ダイアログを表示する
path = fd.askopenfilename(
    title="処理対象のファイルを指定してください",
    filetypes=[('data files','*.csv')])
print(path)

