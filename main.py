import streamlit as st
import pandas as pd

# ロゴ画像の表示（左上に表示）
st.image("logo.jpeg", width=200)  # 幅は調整OK

# ページ設定＋ロゴ表示
st.set_page_config(page_title="TWENTY STAFF VIEWER", page_icon="🟦", layout="centered")
st.image("logo.jpeg", width=250)
st.markdown("### TWENTY STAFF VIEWER")

import streamlit as st
import pandas as pd

st.set_page_config(page_title="TWENTY STAFF VIEWER", layout="centered")
st.title("👕 TWENTY STAFF VIEWER")

# Sample staff data
data = pd.DataFrame([
    {
        "氏名": "七谷 拓実",
        "所属": "ウェアプリント部",
        "入社年月": "2016年6月1日",
        "ランク": "ダイヤモンド",
        "出勤状況": "無遅刻無欠勤",
        "目標": "5年で奇跡の組織を作り上げる"
    }
])

# スタッフ選択
selected = st.selectbox("🧑 スタッフを選んでください", data["氏名"])

# 詳細表示
if selected:
    staff = data[data["氏名"] == selected].iloc[0]
    st.markdown(f"### 📝 {selected} さんのカルテ")
    st.write(f"**所属**：{staff['所属']}")
    st.write(f"**入社年月**：{staff['入社年月']}")
    st.write(f"**ランク**：{staff['ランク']}")
    st.write(f"**出勤状況**：{staff['出勤状況']}")
    st.write(f"**目標**：{staff['目標']}")

    if st.button("✏️ 編集する"):
        st.warning("編集機能は現在このローカル版では無効です（クラウド版で拡張可能）")
