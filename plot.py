import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.cm as cm
import streamlit as st

def gantt_chart(m,result,p):
    # 初期化
    jobs = {f"Job{j+1}": {} for j in range(m)}
    end_time = [0, 0]  # 機械1, 機械2の終了時間を追跡

    # ジョブの順序に従って処理時間を計算
    for job in result:
        job_index = job - 1
        machine1_start = end_time[0]
        machine1_end = machine1_start + p[0][job_index]
        jobs[f"Job{job}"]["Machine1"] = (machine1_start, machine1_end)
        end_time[0] = machine1_end

        machine2_start = max(machine1_end, end_time[1])  # 機械2の開始時間を直前のジョブの終了時間として設定
        machine2_end = machine2_start + p[1][job_index]
        jobs[f"Job{job}"]["Machine2"] = (machine2_start, machine2_end)
        end_time[1] = machine2_end

    # ジョブごとの色を定義
    colors = cm.get_cmap("tab20",m)  # カラーマップからジョブごとの色を取得
    job_colors = {f"Job{j+1}": colors(j) for j in range(m)}

    # 最大終了時間を計算
    max_end_time = max(end for tasks in jobs.values() for start, end in tasks.values())
    
    fig, ax = plt.subplots(1, figsize=(20, 5),dpi=2)  # 横幅を広く設定

    # マシンごとの開始時間と終了時間のバーを描く
    machine_y = {"Machine1": 2, "Machine2": 1}  # 機械1を上、機械2を下に設定

    for job, tasks in jobs.items():
        for machine, (start, end) in tasks.items():
            ax.add_patch(patches.Rectangle((start, machine_y[machine] - 0.4), end - start, 0.8, edgecolor="black", facecolor=job_colors[job]))
            ax.add_patch(patches.Rectangle((start, machine_y[machine] - 0.4), 0.01, 0.8, edgecolor="black", fill=False))  # 開始時間の枠線を追加
            ax.add_patch(patches.Rectangle((end, machine_y[machine] - 0.4), 0.01, 0.8, edgecolor="black", fill=False))  # 終了時間の枠線を追加

    # 凡例の作成
    legend_patches = [patches.Patch(color=color, label=job) for job, color in job_colors.items()]
    ax.legend(handles=legend_patches, loc="lower left")  # 左上に設定

    # 軸の設定
    ax.set_yticks([1, 2])
    ax.set_yticklabels(["Machine2", "Machine1"])  # 上から下に機械1、機械2の順に表示
    # 動的に目盛りの間隔を決定
    max_xticks = 30  # 最大の目盛りの数
    interval = max(1, int(max_end_time / max_xticks))
    ax.set_xticks(range(0, int(max_end_time) + interval, interval))
    ax.set_xlim(0, max_end_time + 0.5)
    ax.set_xlabel("Time")
    ax.set_ylabel("Machine")
    ax.set_title("Flow Shop Schedule")

    plt.ylim(0.5, 2.5)  # y軸の範囲を調整
    plt.grid(True)
    st.pyplot(fig)
    st.header(f"メイクスパンの値は{max_end_time}です。")