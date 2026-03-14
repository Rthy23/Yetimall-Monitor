import streamlit as st

# 1. 頁面配置
st.set_page_config(page_title="YetiMall 監控中心", layout="wide")

# 2. 測試標題
st.title("YetiMall 監控中心")
st.write("系統已啟動，準備載入實時數據...")

# 3. 測試數據區塊
st.subheader("排行榜測試")
st.table({"排名": [1, 2, 3], "用戶ID": ["User_A", "User_B", "User_C"], "購買數量": [150, 120, 90]})

st.success("環境運作正常！")