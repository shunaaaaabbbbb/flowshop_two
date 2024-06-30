import streamlit as st
import pandas as pd

def johnson_rule(m,p): #引数が「m:ジョブ数、p:処理時間」である関数を定義
    Group1 = [] # Group1の初期リスト
    Group2 = [] # Group2の初期リスト
    p1 = {} # Group1に属すジョブの、機械1での処理時間を記憶しておく辞書（ソートの時に使う）
    p2 = {} # Group2に属すジョブの、機械1での処理時間を記憶しておく辞書（ソートの時に使う）
    for j in range(m): # 全てのジョブに対して 
        if p[0][j] <= p[1][j]: # (機械1での処理時間) ≦ (機械2での処理時間)なら
            Group1.append(j+1) # Group1にジョブjを追加する(注 : pythonではリストのインデックスが0から始まる)
            p1[j+1] = p[0][j] # p1にジョブjの機械1での処理時間を記録しておく
        else: #それ以外 ((機械1での処理時間) ＞ (機械2での処理時間))なら
            Group2.append(j+1)# Group2にジョブjを追加する(注 : pythonではリストのインデックスが0から始まる)
            p2[j+1] = p[1][j] # p2にジョブjの機械2での処理時間を記録しておく
    Group1_sorted = sorted(Group1, key=lambda x:p1[x]) # 機械1での処理時間が小さい順にGroup1中のジョブをソートする
    Group2_sorted = sorted(Group2, key=lambda x:p2[x], reverse=True) # 機械1での処理時間が大きい順にGroup1中のジョブをソートする
    return Group1_sorted+Group2_sorted # 並べ替えた2つのリストを繋げて返す
