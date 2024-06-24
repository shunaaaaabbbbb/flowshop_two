import streamlit as st
import pandas as pd

def input_jobs():
    num =  st.slider("ジョブ数を入力（最大20個）", min_value=2, max_value=20, key = "node")    
    return num

def input_time(num):
    p1 = []
    p2 = []
    
    # ジョブごとの処理時間を入力するためのデータフレームを作成
    data = {
        "ジョブ": [f"ジョブ {i+1}" for i in range(num)],
        "機械1での処理時間": [0] * num,
        "機械2での処理時間": [0] * num,
    }

    # データフレームを表示して編集可能にする
    df = pd.DataFrame(data)
    return df
    