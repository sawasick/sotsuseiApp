'''
seleniumで取得したキャプチャ画像の容量が大きいので圧縮する
png→jpg(現状この方法だとjpg保存しかできない)
'''

from PIL import Image
from io import BytesIO
import os

# コンフィグ
COMPRESS_QUALITY = 30 # 圧縮のクオリティ

# JPEG形式とPNG形式の画像ファイルを用意
# jpeg_imgefile = 'jpeg_image.jpg'
png_imgfile = 'result.png'

#############################
#     JPEG形式の圧縮処理     #
#############################
# ファイル名を取得
# file_name = os.path.splitext(os.path.basename(jpeg_imgefile))[0]
# with open(jpeg_imgefile, 'rb') as inputfile:
#     # バイナリモードファイルをPILイメージで取得
#     im = Image.open(inputfile)
#     # JPEG形式の圧縮を実行
#     im_io = BytesIO()
#     im.save(im_io, 'JPEG', quality = COMPRESS_QUALITY)
# with open('comp_' + file_name + '.jpg', mode='wb') as outputfile:
#     # 出力ファイル(comp_png_image.png)に書き込み
#     outputfile.write(im_io.getvalue())

#############################
#     PNG形式の圧縮処理      #
#############################
# ファイル名を取得
file_name = os.path.splitext(os.path.basename(png_imgfile))[0]
with open(png_imgfile, 'rb') as inputfile:
    # バイナリモードファイルをPILイメージで取得
    img = Image.open(inputfile)
    # JPEG形式に変換して、圧縮を実行
    img = img.convert('RGB')
    img_io = BytesIO()
    img.save(img_io, 'JPEG', quality = COMPRESS_QUALITY)
with open('comp_' + file_name + '.jpg', mode='wb') as outputfile:
    # 出力ファイル(comp_png_image.png)に書き込み
    outputfile.write(img_io.getvalue())