# CheetPython

## pipがインストールされていない環境での導入方法
$ python -m ensurepip

## Debian, Ubuntuでのpipの導入方法
$ sudo apt instal -y python3-pip

## パッケージのインストール
$ pip install パッケージ名
$ pip install sampleproject

## バージョン指定
$ pip install sampleproject=1.2.0

## バージョンを範囲指定、うち最新をインストール
$ pip install "sampleproject>=1.2.0,<2.0.0"

## パッケージのアップグレード、ダウングレード
## 最新バージョンにアップグレード
$ pip install --upgreade sampleproject

## ダウングレード
$ pip install --upgrade sampleproject=1.2.0

## インストールされているパッケージとバージョンの確認
$ pip list

## 最新版ではないパッケージのみ表示
$ pip list --outdated

## パッケージのアンインストール
$ pip uninstall sampleproject



requirements.txtを作って複数の環境でバージョンを統一する

## requirements.txtの作成
$ pip freeze > requirements.txt

## requirements.txtの書き方の例 
- 先頭に「#」を入れた行はコメントになる
- foo==1.0.0 # 「==」だと指定されたバージョンがインストールされる 
- bar<2.0.0,>=1.2.0 # バージョンの範囲指定もできる 
- baz # バージョン番号を指定しなければ、インストール実行時点での最新版がインストールされる

## requirements.txtを参照してパッケージをインストール
$ pip install -r requirements.txt


-cオプションで特定パッケージのインストール可能バージョンに制限をかける
constraints.txtを使用する
requirements.txtとセットで使用しないとエラーが発生する

constraints.txtの内容(requirements.txtにはバージョンを書かない)
psycopg2-binary==2.9.1

$ pip install -r requirements.txt -c constraints.txt


---

## 仮想環境を作成する - venv

## 仮想環境の作成
# Python3.9用の仮想環境を作成する
$ python3.9 -m venv env

$ ls -l env envディレクトリの中身を確認する

## 仮想環境の有効化
|OS|シェル|コマンド|
|---|---|---|
|Unix系OS|bash/zsh|$ source <venv>/bin/activate|
|Unix系OS|fish|$ source <venv>/bin/activate.fish|
|Unix系OS|csh/tcsh|$ source <venv>/bin/activate.csh|
|Unix系OS|PowerShell Core|$ <venv>/bin/activate.ps1|
|Windows|コマンドプロンプト|C:\> <venv>\Scripts\activate.bat|
|Windows|PowerShell|PS C:\> <venv>\Scripts\Activate.ps1|

※仮想環境を有効化したら、最初に「pip install --upgrade pip」でpipを最新版にアップグレードするのがおすすめ

## 仮想環境の無効化
$ deactivate

## 仮想環境の削除
Unix系OSの場合
$ rm -rf env

Windows PowerShellの場合
Remove-Item Recurse -Force -Confirm:$false env



## Pythonのコーディング規約





















