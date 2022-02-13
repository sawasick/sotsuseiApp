import os
from tkinter import *
import tkinter.filedialog as fd

inputDirPath = '' # csvファイルのパス
outputDirPath = '' # 出力先のディレクトリパス
accuracy = '' # PlotCsvのaccuracy
bool_compress = False # CompressImageを実行するかどうかのフラグ
quality_compress = '' # CompressImageの圧縮クオリティ

def SelectInput(inputEntry):
    global inputDirPath
    inputDirPath = fd.askopenfilename(
    title="webgazerのcsvファイルを指定してください",
    filetypes=[('data files','*.csv')]
    )
    inputEntry.set(inputDirPath)

def SelectOutput(outputEntry):
    global outputDirPath
    outDir = os.path.abspath(os.path.dirname(__file__))
    outputDirPath = fd.askdirectory(initialdir = outDir)
    outputEntry.set(outputDirPath)

def SwitchBtnStateCompress(scaleBar_compress):
    if scaleBar_compress['state'] == NORMAL:
        scaleBar_compress["state"] = DISABLED
    else:
        scaleBar_compress["state"] = NORMAL

def SetupGui(root):
    ### メインウィンドウを作成
    # root = Tk()
    root.title('ヒートマップ作成ツール ver.1.0') # タイトルを設定
    root.geometry('800x500') # 幅800,高さ500のウィンドウサイズ


    ### csvファイル選択
    # エントリーを作成
    inputEntry = StringVar()
    inputDirEntry = Entry(
        width=50,
        textvariable=inputEntry,
        state="readonly"
    )
    inputDirEntry.insert(0, 'ファイルが選択されていません')
    inputDirEntry.place(
        x = 200, # ラベルの配置先座標x
        y = 50, # ラベルの配置先座標y
    )

    # 選択ボタンを作成
    input_button = Button(
        text="csvファイル選択", # ボタンのテキスト
        width=12, height=1, # 文字数でボタンのサイズを指定
        command=lambda:SelectInput(inputEntry)   # ボタンをクリックした時の動作
    )
    input_button.place(
        x = 50, # ラベルの配置先座標x
        y = 50, # ラベルの配置先座標y
    )

    ### 出力先
    # エントリーを作成
    outputEntry = StringVar()
    outputDirEntry = Entry(
        width=50,
        textvariable=outputEntry,
        state="readonly"
    )
    outputDirEntry.insert(0, '出力先が選択されていません')
    outputDirEntry.place(
        x = 200, # ラベルの配置先座標x
        y = 100, # ラベルの配置先座標y
    )
    # 選択ボタンを作成
    output_button = Button(
        text="出力先",        # ボタンのテキスト
        width=12, height=1, # 文字数でボタンのサイズを指定
        command=lambda:SelectOutput(outputEntry)   # ボタンをクリックした時の動作
    )
    output_button.place(
        x = 50, # ラベルの配置先座標x
        y = 100, # ラベルの配置先座標y
    )

    ### PlotCsvのaccuracy(注視点の大きさ)
    # ラベルを作成
    accuracy_label = Label(text="注視点の大きさ(1~50)")
    accuracy_label.place(
        x = 50,
        y = 150
    )
    # スピンボックスを作成
    # global accuracy_Spinbox
    global accuracy
    accuracy = IntVar(root, value=15) # 初期値
    # accuracy.set(15)
    accuracy_Spinbox = Spinbox(
        root,
        from_=1,
        to=50,
        increment=1,
        width=10,
        state="readonly",
        textvariable=accuracy
    )
    accuracy_Spinbox.place(
        x = 50, # ラベルの配置先座標x
        y = 180, # ラベルの配置先座標y
    )

    ### CompressImageを実行するかどうか
    # チェックボタンのON/OFF
    global bool_compress
    bool_compress = BooleanVar()
    bool_compress.set(False)
    # スケールバーを作成(圧縮のレベル)
    global quality_compress
    quality_compress = IntVar(root, value=30) # 初期値
    scaleBar_compress = Scale(
        root,
        orient='horizontal',
        length=100,
        from_=10,
        to=90,
        resolution=10,
        showvalue=1,
        variable=quality_compress,
        state=DISABLED
    )
    # scaleBar_compress.set(30)
    scaleBar_compress.place(
        x = 250,
        y = 280
    )
    # ラベルを作成
    compress_label = Label(text="出力画像を圧縮する")
    compress_label.place(
        x = 250,
        y = 150
    )
    # チェックボタンを作成
    checkBtn_compress = Checkbutton(
        root,
        variable=bool_compress,
        command=lambda:SwitchBtnStateCompress(scaleBar_compress)
    )
    checkBtn_compress.place(
        x = 250, # ラベルの配置先座標x
        y = 180, # ラベルの配置先座標y
    )
    # スケールバーのラベルを作成
    compressLevel_label = Label(text="圧縮後の画質")
    compressLevel_label.place(
        x = 250,
        y = 230
    )

    # ### 実行ボタン
    # start_button = Button(
    #     text="実行", # ボタンのテキスト
    #     width=4, height=2, # 文字数でボタンのサイズを指定
    #     # command=lambda:main2.test(inputEntryGet)  # 入力値が全て正しいか確認
    # )
    # start_button.place(
    #     x = 450, # ラベルの配置先座標x
    #     y = 400, # ラベルの配置先座標y
    # )

    # メインループを開始
    # root.mainloop()

