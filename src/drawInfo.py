'''
synthesizeImage.pyで合成した画像の上側に
URLやキャリブレーション精度などの情報を記載(描画)する
'''
from PIL import Image, ImageDraw, ImageFont

def CreateMargin():
    # 画像の上側に余白をつけるためベタ画像を生成

    MARGIN_TOP = 220 # 余白のサイズ

    # 合成した画像
    img_origin = Image.open('./dist/result.png')
    # 上側に余白をつけたベタ画像を生成
    img_new = Image.new("RGBA", (img_origin.width, img_origin.height + MARGIN_TOP), (240, 240, 240, 255))
    # ベタ画像の上に元の画像を重ねる
    img_new.paste(img_origin, (0, MARGIN_TOP))

    return img_new

def DrawInfo(url, accuracy, duration):
    print('DrawInfo実行中')

    # 閲覧時間(duration)の単位がミリ秒なので秒に変換
    duration = round((int(duration) / 1000), 1)

    img = CreateMargin()

    # 凡例の画像を重ねる
    img_legend = Image.open('./legend.png')
    img.paste(img_legend, (20, 240))

    draw = ImageDraw.Draw(img)
    textcolor = (40, 40, 40) # テキストの色
    textsize = 36 # 描画するテキストの大きさ
    font = ImageFont.truetype("Mplus1-Light.ttf", size=textsize) # テキストの描画の準備

    draw.text((20, 50), "URL: "+str(url), fill=textcolor, font=font)
    draw.text((20, 0), "キャリブレーション精度: "+str(accuracy)+"%", fill=textcolor, font=font)
    draw.text((20, 100), "閲覧時間: "+str(duration)+"秒", fill=textcolor, font=font)
    # draw.text((20, 150), "閲覧日: 2022年1月24日(月) 14:47", fill=textcolor, font=font)

    img.save('./dist/result2.png', quality=95)

    print('DrawInfo実行完了')

    return