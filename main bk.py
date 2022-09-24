from re import I
from turtle import right
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit超入門')

#st.write('DataFrame')

#表
df = pd.DataFrame({
    '1列目': [1, 2, 3, 4],
    '2列目': [10, 20, 30, 40]
})

#st.write(df)

#st.dataframe(df.style.highlight_max(axis=0), width=200, height=200)
#st.dataframe(df.style.highlight_max(axis=0))

#st.table(df.style.highlight_max(axis=0))  #静的テーブル

#コメント
#"""
# 章
## 節
### 項

#```Python
#import streamlit as st
#import numpy as np
#import pandas as pd
#```
#"""

#グラフ
df = pd.DataFrame(
    np.random.rand(20, 3),
    columns = ['a', 'b', 'c']
)

#st.area_chart(df)

#マップ
df = pd.DataFrame(
    np.random.rand(10, 2)/[50, 50] + [34.55, 135.49],
    columns = ['lat', 'lon']   #緯度、経度
)

#st.map(df)

#チェックボックス
#st.write('Display Image')

#st.write('Interactive widgets')

#if st.checkbox('Show Image'):
#    img = Image.open('img24.JPG')
#    st.image(img, caption='Sample1', use_column_width=True)

#セレクトボックス
#option = st.selectbox(
#    'あなたが好きな数字は？',
#    list(range(1, 11))
#)
#'あなたがすきな数字は', option, 'です。'

#テキスト入力
#text = st.text_input('あなたの趣味は?')
#'あなたの趣味は', text, 'です。'

#スライドバー
#condition = st.slider('あなたの今の調子は？', 0, 100, 50)
#コンディション：', condition

#サイドバー
#st.sidebar.write('Interactive widgets')
#text = st.sidebar.text_input('あなたの趣味は?')
#condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)

#'あなたの趣味は', text, 'です。'
#コンディション：', condition

#2カラムレイアウト
#left_column, right_column = st.beta_columns(2)   #st.beta_columnsは削除されたため
left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムです')

#expanderの追加
#expander1 = st.expander('問い合わせ1')
#expander1.write('問い合わせ1の回答')
#expander2 = st.expander('問い合わせ2')
#expander2.write('問い合わせ2の回答')
#expander3 = st.expander('問い合わせ3')
#expander3.write('問い合わせ3の回答')

#プログレスバー

st.write('プログレスバーの表示')
'Start!'

latest_iteration = st.empty()g
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!'