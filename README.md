## 最終更新
2021-07-19 13:57

# 準備

1. pythonをインストール。
2. コマンドラインで以下を入力。
```
> python -V  
```
Python 3.8.8のように，バージョンが表示されたら成功。

コマンドが見つかりません等のメッセージが出たら，環境変数を設定してPATHを通す。

3. Anaconda promptで以下を実行し，Anacondaをupdateする。
```
conda update --prefix [anacondaがインストールされているフォルダ] anaconda
```


# 実行
コマンドラインで，以下のファイルが入っているディレクトリに移動。
```
bistro.txt
staub.txt
menu.py
```
そのあと，以下を実行。
```
> python menu.py
```

# 使い方
![例](https://user-images.githubusercontent.com/35482155/126108072-faae0ffc-200e-4c32-b1e0-5abed0d18dc7.jpg)
![例](https://user-images.githubusercontent.com/35482155/126919292-a80c3724-225f-47b3-8d84-356bb2a55480.png)

上記の各ボタンを押すと，ランダムにメニューが変わる。
