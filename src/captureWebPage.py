'''
seleniumでwebページのキャプチャ画像を取得する
実行するPCにインストールされているchromeのバージョンに対応したchromedriverが必要
詳細はREADME記載
png→jpg(現状この方法だとjpg保存しかできない)
'''
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def CaptureImage(url, width):
    print('CaptureImage実行中')

    # CHROMEDRIVER = "./chromedriver_mac64_96_0_4664_110"
    CHROMEDRIVER = "./chromedriver_mac64_97_0_4692_71"
    URL =  url

    options = Options()
    # スクロールバーを非表示にする
    options.add_argument('--hide-scrollbars')
    # シークレットモードでChromeを起動する
    options.add_argument('--incognito')
    # ブラウザを表示しない
    options.add_argument('--headless')

    driver = webdriver.Chrome(CHROMEDRIVER, options=options)
    # 対象ページへアクセス
    driver.get(URL)

    # 暗黙的に指定時間待つ（秒）→ajaxなどの動的にページを表示するやつが表示し終わるのを待つため
    driver.implicitly_wait(10)

    driver.maximize_window()
    # ページサイズ取得
    # w = driver.execute_script("return document.body.scrollWidth;")
    w = width
    h = driver.execute_script("return document.body.scrollHeight;")
    # print(w,h)

    # ウィンドウサイズ＝画像サイズ
    driver.set_window_size(w, h)

    # スクリーンショットを取得
    driver.save_screenshot('./dist/capture.png')

    driver.quit()

    print('CaptureImage実行完了')

    return w, h


############################################################
# 単体で実行する時用
'''
CHROMEDRIVER = "./chromedriver"
URL =  'https://hikkoshizamurai.jp/'

options = Options()
# スクロールバーを非表示にする
options.add_argument('--hide-scrollbars')
# シークレットモードでChromeを起動する
options.add_argument('--incognito')
# ブラウザを表示しない
options.add_argument('--headless')

driver = webdriver.Chrome(CHROMEDRIVER, options=options)
# 対象ページへアクセス
driver.get(URL)

# 暗黙的に指定時間待つ（秒）→ajaxなどの動的にページを表示するやつが表示し終わるのを待つため
driver.implicitly_wait(10)

driver.maximize_window()
# ページサイズ取得
w = driver.execute_script("return document.body.scrollWidth;") + 60
# w = data[2][0] →csvデータの幅で取得
h = driver.execute_script("return document.body.scrollHeight;")
print(w,h)
print('wwww')

# ウィンドウサイズ＝画像サイズ
driver.set_window_size(w, h)

# スクリーンショットを取得
driver.save_screenshot('./dist/capture.png')

driver.quit()
'''