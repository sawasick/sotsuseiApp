'''
seleniumで取得したキャプチャ画像の容量が大きいので圧縮する
png→jpg(現状この方法だとjpg保存しかできない)
'''

from PIL import Image
from io import BytesIO
import os

def CompressImage(q, dir):
    print('CompressImage実行中')

    # コンフィグ
    COMPRESS_QUALITY = q
    file_name = os.path.splitext(os.path.basename(dir+'/result.png'))[0]
    with open(dir+'/result.png', 'rb') as inputfile:
        # バイナリモードファイルをPILイメージで取得
        img = Image.open(inputfile)
        # JPEG形式に変換して、圧縮を実行
        img = img.convert('RGB')
        img_io = BytesIO()
        img.save(img_io, 'JPEG', quality = COMPRESS_QUALITY)
    with open(dir+'/comp_' + file_name + '.jpg', mode='wb') as outputfile:
        # 出力ファイル(comp_png_image.png)に書き込み
        outputfile.write(img_io.getvalue())

    print('CompressImage実行完了')

    return