'''
csvデータをプロットしていく
'''

############################################################
# ここはimportCav.pyで処理する部分

# sysモジュールでコマンドライン引数のリスト取得
import sys
# csvモジュールを使ってCSVファイルから1行ずつ読み込む
import csv
data = [] # csvデータを格納する配列
'''
読み込むcsvは下記の形式
URL,
精度,
閲覧時のviewportの幅,閲覧時のviewportの高さ,
閲覧時間,
posX,posY,
...
このままだとカンマの後に空文字列が入るので行の末尾の要素を削除する処理をする→row.pop(-1)
'''
def OpenCsv(arg):
    filename =  arg
    with open(filename, encoding='utf8', newline='') as f:
        csvreader = csv.reader(f)
        for row in csvreader:
            if  row[0] == 'EOF':
                break
            else:
                row.pop(-1) # 上記のcsvの扱い方参照
                data.append(row)
            # print(row)
            # for d in row:
                # print(d)
        # print(data)
        # print(data[0]) # URL
        # print(data[1]) # 精度
        # print(data[2][0]) # 閲覧時のviewportの幅
        # print(data[2][1]) # 閲覧時のviewportの高さ
        # print(data[4以降][0]) # posX
        # print(data[4以降][1]) # posY
# filename = './test.csv'
args = sys.argv
# print(len(args))
if len(args) == 1:
    print('引数なし')
elif len(args) == 2:
    if args[1][-4:] == '.csv':
        OpenCsv(args[1])
    else:
        print('csvファイルじゃない')
else:
    print ('引数多すぎ')
############################################################
width_capture = 5# captureWebPage.pyから持ってくる
height_capture = 10# captureWebPage.pyから持ってくる

# プロット(重みをつける)
# 重みの付け方は画像参照→plot.png
# 座標が-値なら無視
plotData = [[0] * (height_capture + 1) for i in range(width_capture + 1)] # キャプチャ画像のピクセルデータ
#↑ +1は0,0とかも必要だから

accuracy = 3 # 注視点の座標の周り何pxを範囲とするか(2以上)→plot.pngの緑の数値

data_len = len(data)-5 #csvのデータ数

# 重みをつけていく
for i in range(data_len):
        # 注視点中心
        for j in range(accuracy): # ヨコ
            for k in range(accuracy): # タテ
                if (int(data[i + 5][0]) - (accuracy // 2) + j) >= 0 and (int(data[i + 5][1]) - (accuracy // 2) + k) >= 0 and (int(data[i + 5][0]) - (accuracy // 2) + j) <= width_capture and (int(data[i + 5][1]) - (accuracy // 2) + k) <= height_capture:
                    plotData[int(data[i + 5][0]) - (accuracy // 2) + j][int(data[i + 5][1]) - (accuracy // 2) + k] += 3
                    # print(str(int(data[i + 5][0]) - (accuracy // 2) + j)+','+str(int(data[i + 5][1]) - (accuracy // 2) + k))
                else:
                    # print('する〜'+str(int(data[i + 5][0]) - (accuracy // 2) + j)+','+str(int(data[i + 5][1]) - (accuracy // 2) + k))
                    continue
        # 注視点の上
        for j in range(accuracy): # ヨコ
            for k in range(accuracy): # タテ
                if (int(data[i + 5][0]) - (accuracy // 2) + j) >= 0 and (int(data[i + 5][1]) - (accuracy // 2) + k - accuracy) >= 0 and (int(data[i + 5][0]) - (accuracy // 2) + j) <= width_capture and (int(data[i + 5][1]) - (accuracy // 2) + k - accuracy) <= height_capture:
                    plotData[int(data[i + 5][0]) - (accuracy // 2) + j][int(data[i + 5][1]) - (accuracy // 2) + k - accuracy] += 2
                    # print(str(int(data[i + 5][0]) - (accuracy // 2) + j)+','+str(int(data[i + 5][1]) - (accuracy // 2) + k - accuracy))
                else:
                    # print('する〜'+str(int(data[i + 5][0]) - (accuracy // 2) + j)+','+str(int(data[i + 5][1]) - (accuracy // 2) + k - accuracy))
                    continue
        # 注視点の下
        for j in range(accuracy): # ヨコ
            for k in range(accuracy): # タテ
                if (int(data[i + 5][0]) - (accuracy // 2) + j) >= 0 and (int(data[i + 5][1]) - (accuracy // 2) + k + accuracy) >= 0 and (int(data[i + 5][0]) - (accuracy // 2) + j) <= width_capture and (int(data[i + 5][1]) - (accuracy // 2) + k + accuracy) <= height_capture:
                    plotData[int(data[i + 5][0]) - (accuracy // 2) + j][int(data[i + 5][1]) - (accuracy // 2) + k + accuracy] += 2
                    # print(str(int(data[i + 5][0]) - (accuracy // 2) + j)+','+str(int(data[i + 5][1]) - (accuracy // 2) + k + accuracy))
                else:
                    # print('する〜'+str(int(data[i + 5][0]) - (accuracy // 2) + j)+','+str(int(data[i + 5][1]) - (accuracy // 2) + k + accuracy))
                    continue
        # 注視点の左
        for j in range(accuracy): # ヨコ
            for k in range(accuracy): # タテ
                if (int(data[i + 5][0]) - (accuracy // 2) + j - accuracy) >= 0 and (int(data[i + 5][1]) - (accuracy // 2) + k) >= 0 and (int(data[i + 5][0]) - (accuracy // 2) + j - accuracy) <= width_capture and (int(data[i + 5][1]) - (accuracy // 2) + k) <= height_capture:
                    plotData[int(data[i + 5][0]) - (accuracy // 2) + j - accuracy][int(data[i + 5][1]) - (accuracy // 2) + k] += 2
                    # print(str(int(data[i + 5][0]) - (accuracy // 2) + j - accuracy)+','+str(int(data[i + 5][1]) - (accuracy // 2) + k))
                else:
                    # print('する〜'+str(int(data[i + 5][0]) - (accuracy // 2) + j - accuracy)+','+str(int(data[i + 5][1]) - (accuracy // 2) + k))
                    continue
        # 注視点の右
        for j in range(accuracy): # ヨコ
            for k in range(accuracy): # タテ
                if (int(data[i + 5][0]) - (accuracy // 2) + j + accuracy) >= 0 and (int(data[i + 5][1]) - (accuracy // 2) + k) >= 0 and (int(data[i + 5][0]) - (accuracy // 2) + j + accuracy) <= width_capture and (int(data[i + 5][1]) - (accuracy // 2) + k) <= height_capture:
                    plotData[int(data[i + 5][0]) - (accuracy // 2) + j + accuracy][int(data[i + 5][1]) - (accuracy // 2) + k] += 2
                    # print(str(int(data[i + 5][0]) - (accuracy // 2) + j + accuracy)+','+str(int(data[i + 5][1]) - (accuracy // 2) + k))
                else:
                    # print('する〜'+str(int(data[i + 5][0]) - (accuracy // 2) + j + accuracy)+','+str(int(data[i + 5][1]) - (accuracy // 2) + k))
                    continue
        # 注視点の左上
        for j in range(accuracy): # ヨコ
            for k in range(accuracy): # タテ
                if (int(data[i + 5][0]) - (accuracy // 2) + j - accuracy) >= 0 and (int(data[i + 5][1]) - (accuracy // 2) + k - accuracy) >= 0 and (int(data[i + 5][0]) - (accuracy // 2) + j - accuracy) <= width_capture and (int(data[i + 5][1]) - (accuracy // 2) + k - accuracy) <= height_capture:
                    plotData[int(data[i + 5][0]) - (accuracy // 2) + j - accuracy][int(data[i + 5][1]) - (accuracy // 2) + k - accuracy] += 1
                    # print(str(int(data[i + 5][0]) - (accuracy // 2) + j - accuracy)+','+str(int(data[i + 5][1]) - (accuracy // 2) + k - accuracy))
                else:
                    # print('する〜'+str(int(data[i + 5][0]) - (accuracy // 2) + j - accuracy)+','+str(int(data[i + 5][1]) - (accuracy // 2) + k - accuracy))
                    continue
        # 注視点の右上
        for j in range(accuracy): # ヨコ
            for k in range(accuracy): # タテ
                if (int(data[i + 5][0]) - (accuracy // 2) + j + accuracy) >= 0 and (int(data[i + 5][1]) - (accuracy // 2) + k - accuracy) >= 0 and (int(data[i + 5][0]) - (accuracy // 2) + j + accuracy) <= width_capture and (int(data[i + 5][1]) - (accuracy // 2) + k - accuracy) <= height_capture:
                    plotData[int(data[i + 5][0]) - (accuracy // 2) + j + accuracy][int(data[i + 5][1]) - (accuracy // 2) + k - accuracy] += 1
                    # print(str(int(data[i + 5][0]) - (accuracy // 2) + j + accuracy)+','+str(int(data[i + 5][1]) - (accuracy // 2) + k - accuracy))
                else:
                    # print('する〜'+str(int(data[i + 5][0]) - (accuracy // 2) + j + accuracy)+','+str(int(data[i + 5][1]) - (accuracy // 2) + k - accuracy))
                    continue
        # 注視点の左下
        for j in range(accuracy): # ヨコ
            for k in range(accuracy): # タテ
                if (int(data[i + 5][0]) - (accuracy // 2) + j - accuracy) >= 0 and (int(data[i + 5][1]) - (accuracy // 2) + k + accuracy) >= 0 and (int(data[i + 5][0]) - (accuracy // 2) + j - accuracy) <= width_capture and (int(data[i + 5][1]) - (accuracy // 2) + k + accuracy) <= height_capture:
                    plotData[int(data[i + 5][0]) - (accuracy // 2) + j - accuracy][int(data[i + 5][1]) - (accuracy // 2) + k + accuracy] += 1
                    # print(str(int(data[i + 5][0]) - (accuracy // 2) + j - accuracy)+','+str(int(data[i + 5][1]) - (accuracy // 2) + k + accuracy))
                else:
                    # print('する〜'+str(int(data[i + 5][0]) - (accuracy // 2) + j - accuracy)+','+str(int(data[i + 5][1]) - (accuracy // 2) + k + accuracy))
                    continue
        # 注視点の右下
        for j in range(accuracy): # ヨコ
            for k in range(accuracy): # タテ
                if (int(data[i + 5][0]) - (accuracy // 2) + j + accuracy) >= 0 and (int(data[i + 5][1]) - (accuracy // 2) + k + accuracy) >= 0 and (int(data[i + 5][0]) - (accuracy // 2) + j + accuracy) <= width_capture and (int(data[i + 5][1]) - (accuracy // 2) + k + accuracy) <= height_capture:
                    plotData[int(data[i + 5][0]) - (accuracy // 2) + j + accuracy][int(data[i + 5][1]) - (accuracy // 2) + k + accuracy] += 1
                    # print(str(int(data[i + 5][0]) - (accuracy // 2) + j + accuracy)+','+str(int(data[i + 5][1]) - (accuracy // 2) + k + accuracy))
                else:
                    # print('する〜'+str(int(data[i + 5][0]) - (accuracy // 2) + j + accuracy)+','+str(int(data[i + 5][1]) - (accuracy // 2) + k + accuracy))
                    continue
# print(plotData)
############################################################
'''
plotDataをコンソールに出力
'''
# tr = []
# for i in range(len(plotData[0])):
#     tr_row = []
#     for vector in plotData:
#         tr_row.append(vector[i])
#     tr.append(tr_row)
# for i in tr:
    # print(i)
############################################################

# 重みを元に色の濃度を決定する
max_weight = max(max(plotData))


############################################################
# ここはdrawHeartMap.pyで処理する部分
from PIL import Image, ImageDraw

def CalcFill(p):
    '''
    引数の値の重みを求める
    0%   → rgb(127, 255, 0)黄緑
    50%  → rgb(255, 255, 0)黄色
    100% → rgb(255, 0, 0)赤
    '''
    weight = p / max_weight
    if weight <= 0.5:
        r = 127 + round(127 * weight * 2)
        g = 255
    else:
        r = 255
        g = 255 - round(255 * (weight - 0.5) * 2)
    return r, g

img = Image.new('RGBA', (5, 10)) # captureWebPage.pyから幅と高さの値持ってくる
draw = ImageDraw.Draw(img)
for row in range(len(plotData)):
    for col in range(len(plotData[row])):
        if plotData[row][col] != 0:
            r, g = CalcFill(plotData[row][col])
            # ▼(x, y)の重み:N%, r:255, g:255 を出力
            # print('('+str(row)+','+str(col)+')の重み:'+str((plotData[row][col]) / max_weight * 100)+'%, r:'+str(r)+', g:'+str(g))
            draw.point((row, col), fill = (r, g, 0))
        else:
            # print('するー')
            continue
img.save('result.png', quality=95)