from PIL import Image, ImageDraw

def CalcFill(p, max_w):
    '''
    引数の値の重みを求める
    0%   → rgb(127, 255, 0)黄緑
    50%  → rgb(255, 255, 0)黄色
    100% → rgb(255, 0, 0)赤
    '''
    weight = p / max_w
    if weight <= 0.5:
        r = 127 + round(127 * weight * 2)
        g = 255
    else:
        r = 255
        g = 255 - round(255 * (weight - 0.5) * 2)
    return r, g

def DrawHeartMap(plotData, weight, width, height):
    print('DrawHeartMap実行中')

    img = Image.new('RGBA', (width, height))
    draw = ImageDraw.Draw(img)
    for row in range(len(plotData)):
        for col in range(len(plotData[row])):
            if plotData[row][col] != 0:
                r, g = CalcFill(plotData[row][col], weight)
                # ▼(x, y)の重み:N%, r:255, g:255 を出力
                # print('('+str(row)+','+str(col)+')の重み:'+str((plotData[row][col]) / max_weight * 100)+'%, r:'+str(r)+', g:'+str(g))
                draw.point((row, col), fill = (r, g, 0))
            else:
                # print('値が0なのでスルー')
                continue
    img.save('./dist/heartmap.png', quality=95)

    print('DrawHeartMap実行完了')

    return