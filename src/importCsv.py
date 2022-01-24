'''
コマンドラインから引数でcsvファイルを読み込み、配列に格納する
python src/importCsv.py test.csv
'''

# sysモジュールでコマンドライン引数のリスト取得
import sys

# csvモジュールを使ってCSVファイルから1行ずつ読み込む
import csv

'''
読み込むcsvは下記の形式
URL,
精度,
閲覧時間,
閲覧時のviewportの幅,閲覧時のviewportの高さ,
posX,posY,
...
EOF

このままだとカンマの後に空文字列が入るので行の末尾の要素を削除する処理をする→row.pop(-1)
'''
def OpenCsv(arg):
    print('OpenCsv実行中')

    data = [] # csvデータを格納する配列
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
        # print(data[0][0]) # URL
        # print(data[1][0]) # 精度
        # print(data[2][0]) # 閲覧時のviewportの幅
        # print(data[2][1]) # 閲覧時のviewportの高さ
        # print(data[4以降][0]) # posX
        # print(data[4以降][1]) # posY

    print('OpenCsv実行完了')

    return data


############################################################
# 単体で実行する時用
'''
data = [] # csvデータを格納する配列
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
'''