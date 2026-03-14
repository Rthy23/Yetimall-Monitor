import streamlit as st
import sys
import os

st.title("極簡啟動測試 (路徑強化版)")

# 強制讓 Python 在目前目錄尋找檔案
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.append(current_dir)

st.write(f"當前工作目錄: {os.getcwd()}")
st.write(f"搜尋路徑清單: {sys.path[:3]}...") # 只顯示前三項

try:
    st.write("準備嘗試載入資料庫模組...")
    import cloud_db
    st.success("✅ cloud_db.py 引入成功！")

    # 測試是否能讀取到 cloud_db 內的屬性（確認不是空殼）
    st.write("模組內可用函數:", [f for f in dir(cloud_db) if not f.startswith('_')][:5])

except Exception as e:
    st.error(f"❌ 模組載入失敗: {e}")
    st.info("如果檔案明明在 GitHub 上卻讀不到，可能是 Streamlit 快取問題。")

st.success("🎉 如果看到這行，代表主程式已成功運行！")