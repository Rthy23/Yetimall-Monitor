import streamlit as st
import sys

# 1. 基礎 UI，確保伺服器有東西可以跑
st.title("除錯模式：YetiMall Monitor")
st.write("如果看到這行字，代表伺服器與 Port 8501 已成功連接！")

# 2. 逐步檢查模組
try:
    st.write("正在測試模組載入...")
    import cloud_db
    st.write("✅ cloud_db 載入成功")

    import processor
    st.write("✅ processor 載入成功")

    # 測試是否可以呼叫其中的一個函數 (請根據你的實際函數名修改)
    # st.write(cloud_db.get_db_status())

except Exception as e:
    st.error(f"❌ 程式啟動失敗，錯誤訊息如下：")
    st.code(str(e))
    # 印出完整的 Traceback 幫助定位
    import traceback
    st.text(traceback.format_exc())

st.info("如果看到上面有紅色的錯誤，請把內容複製給我，我就能幫你修復！")