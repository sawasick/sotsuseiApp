'''
画像を出力するディレクトリを作成する
ディレクトリ名はcsvのファイル名
'''
import os

def MakeDir(name):

    print('MakeDir実行中')

    DIR_NAME = './dist/'+name[:-4] # 末尾の'.csv'を削除

    # ディレクトリがない場合、作成する
    if not os.path.exists(DIR_NAME):
        # print("ディレクトリを作成します")
        os.makedirs(DIR_NAME)

    print('MakeDir実行完了')

    return DIR_NAME
