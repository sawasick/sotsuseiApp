'''
importCsv.py
コマンドラインから引数でcsvファイルを読み込み、配列に格納する
python main.py test.csv

makeDirectory.py
画像を出力するディレクトリを作成する

captureWebPage.py
URLからキャプチャ画像を取得

plotCsv.py
配列のデータを処理→重みを計算する

drawHeartMap.py
ヒートマップ画像を作成する

synthesizeImage.py
キャプチャ画像とヒートマップ画像を合成する

DrawInfo.py
合成した画像にURLやキャリブレーション精度などの情報を描画

compressImage.py
画像を圧縮する
'''

import sys

from src import importCsv
from src import makeDirectory
from src import captureWebPage
from src import plotCsv
from src import drawHeartMap
from src import synthesizeImage
from src import drawInfo
from src import compressImage

data = [] # csvデータを格納する配列

'''
importCsv.py
csvファイルを処理
'''
args = sys.argv
# print(len(args))
if len(args) == 1:
    print('引数なし')
elif len(args) == 2:
    if args[1][-4:] == '.csv':
        data = importCsv.OpenCsv(args[1])
    else:
        print('csvファイルじゃない')
else:
    print ('引数多すぎ')


'''
makeDirectory.py
画像を出力するディレクトリを作成する
DIR_NAMEはdist配下に作成したディレクトリの名前
'''
DIR_NAME = makeDirectory.MakeDir(args[1])


'''
captureWebPage.py
URLからキャプチャ画像を取得
キャプチャしてくる画像の幅はdata[4][0]
w, h は キャプチャしてきた画像のサイズ
'''
w, h = captureWebPage.CaptureImage(data[0][0], int(data[4][0]), DIR_NAME)


'''
plotCsv.py
data配列を元にプロットデータを作成→重みを計算する
plotDataはキャプチャ画像のピクセル毎の重みの情報
'''
plotData = plotCsv.PlotCsv(data, w, h)


'''
drawHeartMap.py
ヒートマップ画像を作成する
'''
max_weight = max(max(plotData)) # 重みの基準
drawHeartMap.DrawHeartMap(plotData, max_weight, w, h, DIR_NAME)


'''
synthesizeImage.py
キャプチャ画像とヒートマップ画像を合成する
'''
synthesizeImage.SynthesizeImage(DIR_NAME)


'''
DrawInfo.py
合成した画像にURLやキャリブレーション精度などの情報を描画
引数はURL, 日付, キャリブレーション精度, 閲覧時間, ディレクトリ名
'''
drawInfo.DrawInfo(data[0][0], data[1][0], data[2][0], data[3][0], DIR_NAME)


'''
compressImage.py
合成した画像を圧縮する
引数は圧縮のクオリティ.小さい値ほど圧縮を行う
'''
# compressImage.CompressImage(30, DIR_NAME)

'''
ログ出力
'''
print('▼ログ##########')
print('URL:'+str(data[0][0]))
print('キャプチャ画像のwidth:'+str(w)+', height:'+str(h))
print('▲ログ##########')