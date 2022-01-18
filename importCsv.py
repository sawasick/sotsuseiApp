# sysモジュールでコマンドライン引数のリスト取得
import sys

# csvモジュールを使ってCSVファイルから1行ずつ読み込む
import csv

data = [] # csvデータを格納する配列

def OpenCsv(arg):
    filename =  arg
    with open(filename, encoding='utf8', newline='') as f:
        csvreader = csv.reader(f)
        for row in csvreader:
            data.append(row)
            # for d in row:
                # print(d)
        print(data)

# filename = './test.csv'
args = sys.argv
print(len(args))
if len(args) == 1:
    print('引数なし')
elif len(args) == 2:
    if args[1][-4:] == '.csv':
        OpenCsv(args[1])
    else:
        print('csvファイルじゃない')
else:
    print ('引数多すぎ')