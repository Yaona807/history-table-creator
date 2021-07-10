import json
import requests
import pandas as pd
from collections import defaultdict

# AtCoderのユーザーネーム
user_name = 'in708'

# tableの出力先 
file_name = 'README.md'

# AtCoderのhistoryを取得
url = 'https://atcoder.jp/users/' + user_name + '/history/json'
response = requests.get(url)
jsonData = response.json()


d = defaultdict(list)

# 表にするためにデータを加工
for i in range(len(jsonData)-1, -1, -1):
	for k, v in jsonData[i].items():
		d[k].append(v)

d_df = pd.DataFrame(d)

# IsRated == Falseの場合の処理
for index, row in d_df.iterrows():
    if row['IsRated']:
        d_df.loc[index:index,'Difference'] = d_df.loc[index:index,'NewRating'] - d_df.loc[index:index,'OldRating']
    else:
        d_df.loc[index:index,'Difference'] = '-'
        d_df.loc[index:index,'Performance'] = '-'
        d_df.loc[index:index,'NewRating'] = '-'

# 必要な列の取得
df = d_df.loc[:,['EndTime','ContestName','Place','Performance','NewRating','Difference']]

# tableの書き込み開始位置から終了位置
table_top_tag = '<!-- table_top -->'
table_bottom_tag = '<!-- table_bottom -->'

# ファイルの読み込み
with open(file_name,encoding='utf-8') as f:
	data_lines = f.readlines()

# 書き込み終えたかのフラグ
table_write_flag = 0

# 書き込み
with open(file_name,mode='w', encoding='utf-8') as f:
	for data in data_lines:
		# 書き込みを終えた　かつ　終了位置に到達していない
		if table_write_flag == 1 and table_bottom_tag != data.rstrip():
			continue

		# 終了位置へ到達
		if table_bottom_tag == data.rstrip():
			table_write_flag = 0
		# 書き込み
		f.write(data)

		# tableの書き込み
		if table_top_tag == data.rstrip():
			f.write(df.to_markdown() + '\n')
			table_write_flag = 1
