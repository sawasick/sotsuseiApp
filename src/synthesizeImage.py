from PIL import Image

def SynthesizeImage():
    print('SynthesizeImage実行中')

    # 下側の画像(キャプチャ画像)
    img_bottom = Image.open('./dist/capture.png')
    # 上側の画像(ヒートマップのプロット画像)
    img_top = Image.open('./dist/heartmap.png')

    # キャプチャ画像をRGBAモードに変更
    img_bottom.convert("RGBA")
    # ヒートマップ画像と同じサイズにリサイズ→retina対策
    img_bottom = img_bottom.resize(img_top.size)

    # print("img_bottom_info: size("+str(img_bottom.size)+"), mode:"+str(img_bottom.mode))
    # print("img_top_info: size("+str(img_top.size)+"), mode:"+str(img_top.mode))

    # 背景と同サイズの透明な画像を生成
    img_clear = Image.new("RGBA", img_bottom.size, (255, 255, 255, 0))
    # 透過画像の上にペースト(ここのアルファ値の引数で上側の画像の透明度が変わる)
    img_top_blend = Image.blend(img_top, img_clear, 0.3)

    # 上と下の画像を重ねる
    img = Image.alpha_composite(img_bottom, img_top_blend)
    img.save('./dist/result.png', quality=95)

    print('SynthesizeImage実行完了')

    return