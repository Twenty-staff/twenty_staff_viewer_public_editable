import streamlit as st
import pandas as pd
import os
import urllib.parse
from datetime import datetime

# ページ設定
st.set_page_config(page_title="TWENTY STAFF VIEWER", layout="centered")

# CSV読み込み
df = pd.read_csv("staff_data.csv")

# 勤続年数の自動計算
def calculate_years(start_date_str):
    try:
        start = datetime.strptime(start_date_str, "%Y年%m月%d日")
        today = datetime.today()
        return round((today - start).days / 365, 1)
    except:
        return ""

df["勤続年数"] = df["入社年月"].apply(calculate_years)

# スタッフ選択
staff_names = df["氏名"].tolist()
selected_name = st.selectbox("スタッフを選択", staff_names)
staff = df[df["氏名"] == selected_name].iloc[0]

# カードCSS
st.markdown("""
    <style>
    .staff-card {
        border: 1px solid #ddd;
        border-radius: 15px;
        padding: 25px;
        background-color: white;
        box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
        margin: 30px auto;
        max-width: 700px;
    }
    .staff-title {
        font-size: 28px;
        font-weight: bold;
        margin-bottom: 5px;
    }
    .staff-sub {
        font-size: 16px;
        color: #666;
        margin-bottom: 20px;
    }
    .staff-item {
        font-size: 16px;
        margin: 8px 0;
    }
    .rank-badge {
        background-color: #ff3c38;
        color: white;
        padding: 4px 12px;
        border-radius: 10px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# カード内容表示
st.markdown(f"""
<div class="staff-card">
    <div class="staff-title">{staff["氏名"]}</div>
    <div class="staff-sub">{staff["英語表記"]}</div>

    <div class="staff-item">📅 入社年月：<b>{staff["入社年月"]}</b>（<b>{staff["勤続年数"]}年</b>）</div>
    <div class="staff-item">💼 雇用区分：<b>{staff["雇用区分"]}</b></div>
    <div class="staff-item">🏢 部署：<b>{staff["部署"]}</b></div>
    <div class="staff-item">🧑‍💼 役職／担当：<b>{staff["役職/担当"]}</b></div>
    <div class="staff-item">💎 成長支援制度ランク：<span class="rank-badge">{staff["ランク"]}</span></div>
    <div class="staff-item">📈 出勤状況：<b>{staff["出勤状況"]}</b></div>
    <div class="staff-item">🎯 目標：<b>{staff["目標"]}</b></div>
    <div class="staff-item">🍼 育休／産休：<b>{staff["育休／産休"]}</b></div>
    <div class="staff-item">👪 扶養内勤務：<b>{staff["扶養内勤務"]}</b></div>
    <div class="staff-item">📌 配慮事項：<b>{staff["配慮事項"]}</b></div>
""", unsafe_allow_html=True)

# GEPPO PDFへのリンク
geppo_pdf_path = staff["GEPPOパス"]
if isinstance(geppo_pdf_path, str) and geppo_pdf_path.strip() != "":
    full_path = f"pdf/{geppo_pdf_path}"
    if os.path.exists(full_path):
        encoded_path = urllib.parse.quote(full_path)
        st.markdown(f"""
        <div style="text-align: center; margin-top: 20px;">
            📄 GEPPO記録 → <a href="{encoded_path}" target="_blank">[PDFを開く]</a>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("🔍 GEPPO PDFが見つかりません。ファイルパスをご確認ください。")
else:
    st.markdown("📄 GEPPOコメント：未登録")

st.markdown("</div>", unsafe_allow_html=True)
