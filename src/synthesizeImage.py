from PIL import Image

# 下側の画像(キャプチャ画像)
img_bottom = Image.open('synthesize_test.png')
# 上側の画像(ヒートマップのプロット画像)
img_top = Image.open('draw2.png')

# 背景と同サイズの透明な画像を生成
img_clear = Image.new("RGBA", img_bottom.size, (255, 255, 255, 0))
# 透過画像の上にペースト(ここのアルファ値の引数で上側の画像の透明度が変わる)
img_top_blend = Image.blend(img_top, img_clear, 0.3)

# 上と下の画像を重ねる
img = Image.alpha_composite(img_bottom, img_top_blend)
img.save('synthesized.png', quality=95)