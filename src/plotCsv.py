'''
csvデータをプロットしていく(重みをつける)
重みの付け方は画像参照→plot.png
'''

def PlotCsv(d, w, h):
    print('PlotCsv実行中')

    data = d
    width_capture = w
    height_capture = h
    accuracy = 15 # 注視点の座標の周り何pxを範囲とするか(2以上)→plot.pngの緑の数値
    plotData = [[0] * (height_capture + 1) for i in range(width_capture + 1)] # キャプチャ画像のピクセルデータ
    data_len = len(data)-5 #csvのデータ数
    #↑ +1は0,0とかも必要だから

    # 重みをつけていく
    for i in range(data_len):
            # 注視点中心
            for j in range(accuracy): # ヨコ
                for k in range(accuracy): # タテ
                    if (int(data[i + 5][0]) - (accuracy // 2) + j) >= 0 and (int(data[i + 5][1]) - (accuracy // 2) + k) >= 0 and (int(data[i + 5][0]) - (accuracy // 2) + j) <= width_capture and (int(data[i + 5][1]) - (accuracy // 2) + k) <= height_capture:
                        plotData[int(data[i + 5][0]) - (accuracy // 2) + j][int(data[i + 5][1]) - (accuracy // 2) + k] += 3
                        # print(str(int(data[i + 5][0]) - (accuracy // 2) + j)+','+str(int(data[i + 5][1]) - (accuracy // 2) + k))
                    else:
                        # print('する〜'+str(int(data[i + 5][0]) - (accuracy // 2) + j)+','+str(int(data[i + 5][1]) - (accuracy // 2) + k))
                        continue
            # 注視点の上
            for j in range(accuracy): # ヨコ
                for k in range(accuracy): # タテ
                    if (int(data[i + 5][0]) - (accuracy // 2) + j) >= 0 and (int(data[i + 5][1]) - (accuracy // 2) + k - accuracy) >= 0 and (int(data[i + 5][0]) - (accuracy // 2) + j) <= width_capture and (int(data[i + 5][1]) - (accuracy // 2) + k - accuracy) <= height_capture:
                        plotData[int(data[i + 5][0]) - (accuracy // 2) + j][int(data[i + 5][1]) - (accuracy // 2) + k - accuracy] += 2
                        # print(str(int(data[i + 5][0]) - (accuracy // 2) + j)+','+str(int(data[i + 5][1]) - (accuracy // 2) + k - accuracy))
                    else:
                        # print('する〜'+str(int(data[i + 5][0]) - (accuracy // 2) + j)+','+str(int(data[i + 5][1]) - (accuracy // 2) + k - accuracy))
                        continue
            # 注視点の下
            for j in range(accuracy): # ヨコ
                for k in range(accuracy): # タテ
                    if (int(data[i + 5][0]) - (accuracy // 2) + j) >= 0 and (int(data[i + 5][1]) - (accuracy // 2) + k + accuracy) >= 0 and (int(data[i + 5][0]) - (accuracy // 2) + j) <= width_capture and (int(data[i + 5][1]) - (accuracy // 2) + k + accuracy) <= height_capture:
                        plotData[int(data[i + 5][0]) - (accuracy // 2) + j][int(data[i + 5][1]) - (accuracy // 2) + k + accuracy] += 2
                        # print(str(int(data[i + 5][0]) - (accuracy // 2) + j)+','+str(int(data[i + 5][1]) - (accuracy // 2) + k + accuracy))
                    else:
                        # print('する〜'+str(int(data[i + 5][0]) - (accuracy // 2) + j)+','+str(int(data[i + 5][1]) - (accuracy // 2) + k + accuracy))
                        continue
            # 注視点の左
            for j in range(accuracy): # ヨコ
                for k in range(accuracy): # タテ
                    if (int(data[i + 5][0]) - (accuracy // 2) + j - accuracy) >= 0 and (int(data[i + 5][1]) - (accuracy // 2) + k) >= 0 and (int(data[i + 5][0]) - (accuracy // 2) + j - accuracy) <= width_capture and (int(data[i + 5][1]) - (accuracy // 2) + k) <= height_capture:
                        plotData[int(data[i + 5][0]) - (accuracy // 2) + j - accuracy][int(data[i + 5][1]) - (accuracy // 2) + k] += 2
                        # print(str(int(data[i + 5][0]) - (accuracy // 2) + j - accuracy)+','+str(int(data[i + 5][1]) - (accuracy // 2) + k))
                    else:
                        # print('する〜'+str(int(data[i + 5][0]) - (accuracy // 2) + j - accuracy)+','+str(int(data[i + 5][1]) - (accuracy // 2) + k))
                        continue
            # 注視点の右
            for j in range(accuracy): # ヨコ
                for k in range(accuracy): # タテ
                    if (int(data[i + 5][0]) - (accuracy // 2) + j + accuracy) >= 0 and (int(data[i + 5][1]) - (accuracy // 2) + k) >= 0 and (int(data[i + 5][0]) - (accuracy // 2) + j + accuracy) <= width_capture and (int(data[i + 5][1]) - (accuracy // 2) + k) <= height_capture:
                        plotData[int(data[i + 5][0]) - (accuracy // 2) + j + accuracy][int(data[i + 5][1]) - (accuracy // 2) + k] += 2
                        # print(str(int(data[i + 5][0]) - (accuracy // 2) + j + accuracy)+','+str(int(data[i + 5][1]) - (accuracy // 2) + k))
                    else:
                        # print('する〜'+str(int(data[i + 5][0]) - (accuracy // 2) + j + accuracy)+','+str(int(data[i + 5][1]) - (accuracy // 2) + k))
                        continue
            # 注視点の左上
            for j in range(accuracy): # ヨコ
                for k in range(accuracy): # タテ
                    if (int(data[i + 5][0]) - (accuracy // 2) + j - accuracy) >= 0 and (int(data[i + 5][1]) - (accuracy // 2) + k - accuracy) >= 0 and (int(data[i + 5][0]) - (accuracy // 2) + j - accuracy) <= width_capture and (int(data[i + 5][1]) - (accuracy // 2) + k - accuracy) <= height_capture:
                        plotData[int(data[i + 5][0]) - (accuracy // 2) + j - accuracy][int(data[i + 5][1]) - (accuracy // 2) + k - accuracy] += 1
                        # print(str(int(data[i + 5][0]) - (accuracy // 2) + j - accuracy)+','+str(int(data[i + 5][1]) - (accuracy // 2) + k - accuracy))
                    else:
                        # print('する〜'+str(int(data[i + 5][0]) - (accuracy // 2) + j - accuracy)+','+str(int(data[i + 5][1]) - (accuracy // 2) + k - accuracy))
                        continue
            # 注視点の右上
            for j in range(accuracy): # ヨコ
                for k in range(accuracy): # タテ
                    if (int(data[i + 5][0]) - (accuracy // 2) + j + accuracy) >= 0 and (int(data[i + 5][1]) - (accuracy // 2) + k - accuracy) >= 0 and (int(data[i + 5][0]) - (accuracy // 2) + j + accuracy) <= width_capture and (int(data[i + 5][1]) - (accuracy // 2) + k - accuracy) <= height_capture:
                        plotData[int(data[i + 5][0]) - (accuracy // 2) + j + accuracy][int(data[i + 5][1]) - (accuracy // 2) + k - accuracy] += 1
                        # print(str(int(data[i + 5][0]) - (accuracy // 2) + j + accuracy)+','+str(int(data[i + 5][1]) - (accuracy // 2) + k - accuracy))
                    else:
                        # print('する〜'+str(int(data[i + 5][0]) - (accuracy // 2) + j + accuracy)+','+str(int(data[i + 5][1]) - (accuracy // 2) + k - accuracy))
                        continue
            # 注視点の左下
            for j in range(accuracy): # ヨコ
                for k in range(accuracy): # タテ
                    if (int(data[i + 5][0]) - (accuracy // 2) + j - accuracy) >= 0 and (int(data[i + 5][1]) - (accuracy // 2) + k + accuracy) >= 0 and (int(data[i + 5][0]) - (accuracy // 2) + j - accuracy) <= width_capture and (int(data[i + 5][1]) - (accuracy // 2) + k + accuracy) <= height_capture:
                        plotData[int(data[i + 5][0]) - (accuracy // 2) + j - accuracy][int(data[i + 5][1]) - (accuracy // 2) + k + accuracy] += 1
                        # print(str(int(data[i + 5][0]) - (accuracy // 2) + j - accuracy)+','+str(int(data[i + 5][1]) - (accuracy // 2) + k + accuracy))
                    else:
                        # print('する〜'+str(int(data[i + 5][0]) - (accuracy // 2) + j - accuracy)+','+str(int(data[i + 5][1]) - (accuracy // 2) + k + accuracy))
                        continue
            # 注視点の右下
            for j in range(accuracy): # ヨコ
                for k in range(accuracy): # タテ
                    if (int(data[i + 5][0]) - (accuracy // 2) + j + accuracy) >= 0 and (int(data[i + 5][1]) - (accuracy // 2) + k + accuracy) >= 0 and (int(data[i + 5][0]) - (accuracy // 2) + j + accuracy) <= width_capture and (int(data[i + 5][1]) - (accuracy // 2) + k + accuracy) <= height_capture:
                        plotData[int(data[i + 5][0]) - (accuracy // 2) + j + accuracy][int(data[i + 5][1]) - (accuracy // 2) + k + accuracy] += 1
                        # print(str(int(data[i + 5][0]) - (accuracy // 2) + j + accuracy)+','+str(int(data[i + 5][1]) - (accuracy // 2) + k + accuracy))
                    else:
                        # print('する〜'+str(int(data[i + 5][0]) - (accuracy // 2) + j + accuracy)+','+str(int(data[i + 5][1]) - (accuracy // 2) + k + accuracy))
                        continue
    #######################################
    '''
    plotDataをコンソールに出力
    '''
    # tr = []
    # for i in range(len(plotData[0])):
    #     tr_row = []
    #     for vector in plotData:
    #         tr_row.append(vector[i])
    #     tr.append(tr_row)
    # for i in tr:
        # print(i)
    #######################################

    print('plotCsv実行完了')

    return plotData
