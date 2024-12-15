## EXIF情報を追加した1:1の画像を作成

#### ディレクトリ構成
```
image/
├── src/
│   ├── single.py
│   ├── multi.py
│   ├── EXIF.py
│   ├── path.py
│   └── create_image.py
│
├── image/
│   ├── image.jpg
│   ├── image1.jpg
│   │── image2.jpg
│   │      ...
│   └── image-n.jpg
│
└── output/
```

#### 実行スクリプト一覧
- single.py
    相対パスを指定した一枚の画像に対して処理を実行

    ```
    python single.py
    ```

- multi.py
    相対パスを指定したディレクトリ内の全ての画像に対して処理を実行
    ```terminal
    python single.py
    ```


#### 関数スクリプト一覧
- EXIF.py
- path.py
- create_image.py


#### 出力EXIF情報
- [x] 日付
- [ ] 時間
- [x] カメラ機種名
- [x] 焦点距離
- [x] ISO感度
- [x] シャッタースピード
- [x] F値
