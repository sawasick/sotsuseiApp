# sotsuseiApp

[webgazer.js](https://github.com/sawasick/sotsusei)を用いた視線トラッキングのcsvデータを元にヒートマップ画像を作成するプログラム
## Usage
ターミナルで`pipenv shell`を実行した状態で
``` zsh
$ python main.py test.csv
```

---
### selenium
iMacのchromeのバージョン→ 96.0.4664.110  
↓chromedriverのダウンロード先  
https://chromedriver.chromium.org/downloads

参考サイト
- https://self-development.info/selenium%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%A6python%E3%81%A7%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88%E3%82%92%E5%8F%96%E5%BE%97%E3%81%99%E3%82%8B/
- https://self-development.info/%E5%88%9D%E5%BF%83%E8%80%85%E3%81%A7%E3%82%82%E7%B0%A1%E5%8D%98%E3%81%AB%E3%81%A7%E3%81%8D%E3%82%8Bselenium%E3%81%AE%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E3%80%90python%E3%80%91/
- https://self-development.info/selenium-4%e3%81%a7%e3%80%8cdeprecationwarning%e3%80%8d%e3%81%8c%e5%87%ba%e3%82%8b%e5%a0%b4%e5%90%88%e3%81%ae%e5%af%be%e7%ad%96/
- https://self-development.info/selenium-4%e3%81%a7headless%ef%bc%88%e3%83%98%e3%83%83%e3%83%89%e3%83%ac%e3%82%b9%ef%bc%89%e3%81%ab%e5%af%be%e5%bf%9c%e3%81%99%e3%82%8b/

---
### 画像圧縮（Pillow）
参考サイト
- https://create-it-myself.com/know-how/compress-png-and-jpeg-images-in-python/

---
### 描画（Pillow）
参考サイト
- https://note.nkmk.me/python-pillow-imagedraw/

---
### 画像合成（Pillow）
参考サイト
- https://qiita.com/iso12800jp/items/a74852ebfd3041065aeb
- https://yu-nix.com/blog/2020/9/27/python-pillow-image-blend/