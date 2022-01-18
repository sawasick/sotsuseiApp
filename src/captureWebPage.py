from selenium import webdriver
from selenium.webdriver.chrome.options import Options

CHROMEDRIVER = "./chromedriver"
URL = "https://hikkoshizamurai.jp/"

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

# ページサイズ取得
w = driver.execute_script("return document.body.scrollWidth;")
h = driver.execute_script("return document.body.scrollHeight;")
print(w,h)

# ウィンドウサイズ＝画像サイズ
driver.set_window_size(w, h)

# スクリーンショットを取得
driver.save_screenshot('result.png')

driver.quit()