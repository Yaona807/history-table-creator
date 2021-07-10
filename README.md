# history-table-creator

## 概要

AtCoderのコンテスト参加履歴を取得し、これまでのコンテストの参加をまとめたtableを作成し、マークダウンでファイルの書き込みを行う。

## 使い方

1. AtCoderのユーザーネームと書き込みたい任意のファイル(.md推奨)を指定

    ```python
    # AtCoderのユーザーネーム
    user_name = 'in708'
    
    # tableの出力先 
    file_name = 'README.md'
    ```

2. tableを書き込みたい場所を指定する。
    * tableの書き始めの場所を`<!-- table_top -->`で指定
    * tableの書き終わりの場所を`<!-- table_bottom -->`で指定
`<!-- table_top -->`と`<!-- table_bottom -->`の中に書かれてある内容は上書きされるので注意

3. プログラムを実行\
tableが任意のファイルに出力される

## 出力例

<!-- table_top -->
|    | EndTime                   | ContestName                                                             |   Place |   Performance |   NewRating |   Difference |
|---:|:--------------------------|:------------------------------------------------------------------------|--------:|--------------:|------------:|-------------:|
|  0 | 2021-07-04T22:40:00+09:00 | AtCoder Beginner Contest 208                                            |    3313 |           777 |         468 |           43 |
|  1 | 2021-06-26T22:40:00+09:00 | AtCoder Beginner Contest 207                                            |    2316 |           997 |         425 |           86 |
|  2 | 2021-06-19T22:40:00+09:00 | AtCoder Beginner Contest 206（Sponsored by Panasonic）                  |    4832 |           507 |         339 |           18 |
|  3 | 2021-06-13T22:40:00+09:00 | AtCoder Beginner Contest 205                                            |    6390 |           124 |         321 |          -17 |
|  4 | 2021-06-12T23:00:00+09:00 | 東京海上日動 プログラミングコンテスト2021（AtCoder Regular Contest 122) |    1747 |           100 |         338 |          -22 |
|  5 | 2021-06-06T22:40:00+09:00 | AtCoder Beginner Contest 204                                            |    4419 |           580 |         360 |           26 |
|  6 | 2021-05-30T22:40:00+09:00 | AtCoder Beginner Contest 203（Sponsored by Panasonic）                  |    3338 |           762 |         334 |           52 |
|  7 | 2021-05-29T23:00:00+09:00 | NOMURA プログラミングコンテスト 2021(AtCoder Regular Contest 121)       |    2446 |            10 |         282 |          -21 |
|  8 | 2021-05-23T22:00:00+09:00 | AtCoder Regular Contest 120                                             |    1756 |          -171 |         303 |          -39 |
|  9 | 2021-05-22T22:40:00+09:00 | エイシングプログラミングコンテスト2021（AtCoder Beginner Contest 202）  |    4115 |           631 |         342 |           35 |
| 10 | 2021-05-15T22:40:00+09:00 | マイナビプログラミングコンテスト2021（AtCoder Beginner Contest 201）    |    3898 |           687 |         307 |           45 |
| 11 | 2021-05-08T22:40:00+09:00 | 京セラプログラミングコンテスト2021（AtCoder Beginner Contest 200）      |    4755 |           522 |         262 |           28 |
| 12 | 2021-05-01T22:40:00+09:00 | ZONeエナジー プログラミングコンテスト  “HELLO SPACE”                    |    3982 |           542 |         234 |           32 |
| 13 | 2021-04-24T22:40:00+09:00 | AtCoder Beginner Contest 199（Sponsored by Panasonic）                  |    4979 |           489 |         202 |           29 |
| 14 | 2021-04-18T23:00:00+09:00 | AtCoder Regular Contest 117                                             |    2965 |           250 |         173 |           11 |
| 15 | 2021-04-11T22:40:00+09:00 | AtCoder Beginner Contest 198                                            |    6090 |           143 |         162 |            6 |
| 16 | 2021-03-28T23:00:00+09:00 | AtCoder Regular Contest 116                                             |    2810 |           277 |         156 |           16 |
| 17 | 2021-03-27T22:40:00+09:00 | AtCoder Beginner Contest 197（Sponsored by Panasonic）                  |    4188 |           540 |         140 |           38 |
| 18 | 2021-03-21T22:00:00+09:00 | AtCoder Regular Contest 115                                             |    2122 |           -71 |         102 |            2 |
| 19 | 2021-03-20T22:40:00+09:00 | AtCoder Beginner Contest 196                                            |    4840 |           497 |         100 |           36 |
| 20 | 2021-03-14T23:00:00+09:00 | AtCoder Regular Contest 114                                             |    1980 |           222 |          64 |           21 |
| 21 | 2021-03-06T22:40:00+09:00 | AtCoder Beginner Contest 194                                            |    6266 |            26 |          43 |           14 |
| 22 | 2021-02-27T22:40:00+09:00 | キャディプログラミングコンテスト2021(AtCoder Beginner Contest 193)      |    6426 |           -46 |          29 |           13 |
| 23 | 2021-02-21T23:00:00+09:00 | AtCoder Regular Contest 113                                             |    3338 |          -275 |          16 |            9 |
| 24 | 2021-02-20T22:40:00+09:00 | SOMPO HD プログラミングコンテスト2021(AtCoder Beginner Contest 192)     |    7118 |             2 |           7 |            7 |
<!-- table_bottom -->
