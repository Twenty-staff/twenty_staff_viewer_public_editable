import streamlit as st
import pandas as pd
import os
from datetime import datetime
from PIL import Image

# CSVファイルの読み込み
df = pd.read_csv("staff_data.csv")

# スタッフ選択
selected_name = st.selectbox("スタッフを選んでください", df["名前"])

# 該当スタッフのデータを抽出
staff = df[df["名前"] == selected_name].iloc[0]

# ヘッダー（中央寄せ）
st.markdown("<h1 style='text-align: center;'>TWENTY STAFF VIEWER</h1>", unsafe_allow_html=True)

# カード風の情報表示
with st.container():
    st.markdown(f"## {staff['名前']} さんのカルテ")

    # 各項目を区切って表示
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown(f"**英語表記：** {staff['英語表記']}")
    st.markdown(f"**成長支援制度:ランク：** {staff['成長支援制度:ランク']}")

    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown(f"📅 **入社年月：** {staff['入社年月']}")
    try:
        start_date = pd.to_datetime(staff['入社年月'])
        now = pd.to_datetime(datetime.now())
        years = round((now - start_date).days / 365, 1)
        st.markdown(f"⏳ **勤続年数：** {years} 年")
    except:
        st.markdown("⏳ **勤続年数：** 計算不可")

    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown(f"🕒 **出勤状況：** {staff['出勤状況']}")
    st.markdown(f"🎯 **目標：** {staff['目標']}")

    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown(f"🗂️ **雇用区分：** {staff['雇用区分']}")
    st.markdown(f"🏢 **部署：** {staff['部署']}")
    st.markdown(f"💼 **役職/担当：** {staff['役職/担当']}")

    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown(f"👶 **育休 / 産休：** {staff['育休/産休']}")
    st.markdown(f"👨‍👩‍👧 **扶養内勤務：** {staff['扶養内勤務']}")
    st.markdown(f"💌 **配慮事項：** {staff['配慮事項']}")

    st.markdown("<hr>", unsafe_allow_html=True)

    # GEPPO コメントPDFリンク
    pdf_path = f"geppo_{staff['英語表記'].lower().replace(' ', '_')}.pdf"
    if os.path.exists(pdf_path):
        st.markdown(f"📄 **GEPPOコメント：** [PDFを開く]({pdf_path})", unsafe_allow_html=True)
    else:
        st.markdown("📄 **GEPPOコメント：** 未登録")

    st.markdown("<hr>", unsafe_allow_html=True)

    # ロゴ画像表示（中央寄せ）
    try:
        logo = Image.open("logo.jpeg")  # 拡張子注意！.png なら変更
        st.image(logo, width=150)
    except:
        st.warning("ロゴ画像が見つかりませんでした")
