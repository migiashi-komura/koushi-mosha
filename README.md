# 使用したパッケージ

- opencv-python

# メモ
Windows10のwslで実行すると、guiの環境が設定されていないためエラーが出る。そのためWSLgの機能が付いたバージョンにwslをアップデートしておく必要がある。

## 1. Powershellを管理者権限で開く。
ctrl + shift押しながらPowershell開く。そして、

```powershell
wsl --update
```

と入力。

```powershell
wsl --version
```

と入力してWSLgの項目が表示されればおｋ。