# # これはサンプルの Python スクリプトです。
#
# # Shift+F10 を押して実行するか、ご自身のコードに置き換えてください。
# # Shift を2回押す を押すと、クラス/ファイル/ツールウィンドウ/アクション/設定を検索します。
#
#
# def print_hi(name):
#     # スクリプトをデバッグするには以下のコード行でブレークポイントを使用してください。
#     print(f'Hi, {name}')  # Ctrl+F8を押すとブレークポイントを切り替えます。
#
#
# # ガター内の緑色のボタンを押すとスクリプトを実行します。
# if __name__ == '__main__':
#     print_hi('PyCharm')

# PyCharm のヘルプは https://www.jetbrains.com/help/pycharm/ を参照してください
import pandas as pd

# 第1章

# CSVファイルを読み取り
df = pd.read_csv('data/gapminder.tsv', sep='\t')
print(df.head())

# type関数
print(type(df))

# 行と列の個数をとる
print(df.shape)

# 列の名前を見る
print(df.columns)

# 各列のdtypeを見る
print(df.dtypes)

# データの詳しい情報を見る infoメソッド
print(df.info())

# countの列だけを取り出して独自の変数に保存する
country_df = df['country']

# 最初の5個の値を表示する
print(country_df.head())

# 最後の5個の値を表示する
print(country_df.tail())

# countryとcontinentとyearのデータを見る
subset = df[['country', 'continent', 'year']]
print(subset.head())
print(subset.tail())

# ------------------------------------------------------------
# インデックスラベル(行名)による絞り込み loc
# ------------------------------------------------------------

# 最初の行を抽出する
print(df.loc[0])

# 100番目の行を抽出する
print(df.loc[99])

# 最後の行を抽出する方法
# 行数を得る ⇒ 最終行のインデックス値を計算する
number_of_rows = df.shape[0]
last_row_index = number_of_rows - 1
print(df.loc[last_row_index])

# 複数行の抽出
print(df.loc[[0, 99, 999]])

# ------------------------------------------------------------
# インデックス番号による絞り込み iloc
# ------------------------------------------------------------

# 2番目の行を見る
print(df.iloc[1])

# 100番目の行を見る
print(df.iloc[99])

# -1を使って最後の行を抽出する
print(df.iloc[-1])

# 第1行と第100行と第1000行を選択する
print(df.iloc[[0, 99, 999]])
















# 第2章 pandasのデータ構造

# Seriesオブジェクトは、1次元のコンテナ
s = pd.Series(['banana', 42])
print(s)

# 手作業でSeriesにindexを代入する
s = pd.Series(['Wes McKinney', 'Creator of Pandas'], index=['Person', 'Who'])
print(s)

# DataFrameを作る
scientists = pd.DataFrame({
    'Name': ['Rosaline Franklin', 'William Gosset'],
    'Occupation': ['Chemist', 'Statistician'],
    'Born': ['1920-07025', '1876-06-13'],
    'Died': ['1958-04-16', '1937-10-16'],
    'Age': [37, 61]
})
print(scientists)







# 第3章 プロットによるグラフ描画
# matplotlibライブラリ
# seabornライブラリ
# pandasでのプロッティング

import seaborn as sns
anscombe = sns.load_dataset("anscombe")
print(anscombe)


