
### 検索ツールサンプル
### これをベースに課題の内容を追記してください
import csv
import os

# 検索ソース
# ソースファイルからリストを作成
# ファイルが存在しない場合は、新規作成して空のリストを作成
source_path = 'source.csv'
if os.path.exists(source_path):
    with open(source_path, mode='r') as f:
        reader = csv.reader(f)
        source = [row[0] for row in reader]
else:
    with open(source_path, mode='w'):
        source = []


### 検索ツール
def search():
    word = input("鬼滅の登場人物の名前を入力してください >>> ")

    ### ここに検索ロジックを書く
    if word in source:
        print("{}が見つかりした".format(word))
    else:
        print("{}が見つかりませんでした".format(word))

        # 登場人物の追記処理
        with open(source_path, mode='a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([word])
            print("{}を追加しました".format(word))


if __name__ == "__main__":
    search()
