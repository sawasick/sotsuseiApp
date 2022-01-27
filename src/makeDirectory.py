'''
画像を出力するディレクトリを作成する
ディレクトリ名はcsvのファイル名
'''
import os

def MakeDir(inputDir, outputDir):

    print('MakeDir実行中')

    inputDirName = os.path.splitext(os.path.basename(inputDir))[0] # 末尾の.csvを削除
    # 出力先ディレクトリにcsvファイル名のフォルダがない場合、作成する
    if not os.path.exists(outputDir+'/'+inputDirName):
        # print("ディレクトリを作成します")
        os.makedirs(outputDir+'/'+inputDirName)

    print('MakeDir実行完了')

    return outputDir+'/'+inputDirName