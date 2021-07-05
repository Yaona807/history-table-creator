import json
import requests
import pandas as pd
from collections import defaultdict

# AtCoderのユーザーネーム
user_name = 'in708'

# AtCoderのhistoryを取得
url = 'https://atcoder.jp/users/' + user_name + '/history/json'
response = requests.get(url)
jsonData = response.json()


d = defaultdict(list)

# 表にするためにデータを加工
for i in range(len(jsonData)-1, -1, -1):
	for k, v in jsonData[i].items():
		d[k].append(v)
df = pd.DataFrame(d)

# 不要な部分を削除
del df['InnerPerformance']
del df['ContestScreenName']
del df['ContestNameEn']
del df['IsRated']
del df['Place']

# HTMLファイルに書き込み
df.to_html('history.html')
