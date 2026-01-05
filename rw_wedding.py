import streamlit as st

# 1. 設定網頁標題
st.set_page_config(page_title="弘智 & 凡宸 婚禮邀請", page_icon="💍")

# 2. 初始化頁面狀態 (紀錄是否已經點擊過進場)
if 'entered' not in st.session_state:
    st.session_state['entered'] = False

# ==========================================
#  頁面 A：封面進場頁 (還沒點擊前顯示這個)
# ==========================================
if not st.session_state['entered']:
    # 這裡可以放一張全版大圖或是簡單的文字
    st.markdown(
        """
        <style>
        .stButton>button {
            width: 100%;
            height: 3em;
            font-size: 20px;
            background-color: #ff4b4b;
            color: white;
            border-radius: 10px;
        }
        </style>
        """, 
        unsafe_allow_html=True
    )
    
    st.title("💌 誠摯邀請")
    st.write("弘智 & 凡宸 的婚禮派對")
    st.write("Jan 31, 2026")
    
    st.divider()
    
    # 這是關鍵按鈕！使用者點擊後，我們切換狀態並重整
    if st.button("👉 點此開啟喜帖 (開啟音樂)", type="primary"):
        st.session_state['entered'] = True
        st.rerun()

# ==========================================
#  頁面 B：婚禮主頁面 (點擊後顯示這個)
# ==========================================
else:
    # 1. 音樂播放器 (設定為自動播放)
    # 由於使用者剛才點過了按鈕，這裡的 autoplay=True 就能成功生效！
    st.audio("How_Long_Will_I_Love_You.mp3", format="audio/mp3", start_time=0, autoplay=True)

    # 2. 新人資訊
    st.title("❤️ 弘智 & 凡宸 的婚禮派對")
    st.write("我們結婚了！歡迎大家來參加我們的婚宴。")

    # 3. 婚紗照 (請確認這裡的檔名跟 GitHub 上的一樣)
    col1, col2 = st.columns(2)
    with col1:
        st.image("photo1.jpg", use_container_width=True) 
    with col2:
        st.image("photo2.jpg", use_container_width=True)

    # 4. 婚禮資訊
    st.header("📅 宴客資訊")
    st.success("""
    - **日期**：2026 年 1 月 31 日 (星期六)
    - **時間**：12:00 宴客入席 / 12:30 午宴開席
    - **地點**：香格里拉冬山河渡假飯店
    - **地址**：宜蘭縣五結鄉公園二路 15 號
    """)

    # 5. 座位查詢
    st.header("🔍 查詢我的座位")
    
    seat_data = {
        "王大明": "男方大學同學桌 - A1",
        "林小美": "女方親戚桌 - B2",
        "任弘智": "新郎本人",
        "王凡宸": "新娘本人"
    }

    user_input = st.text_input("請輸入您的姓名或綽號 (例如：王大明)")

    if user_input:
        result = seat_data.get(user_input.strip())
        if result:
            st.balloons()
            st.success(f"🎊 嗨 {user_input}！您的座位在：【{result}】")
        else:
            st.warning("查無資料，請確認名字是否輸入正確。")

    # 6. 地圖與底部
    st.markdown("---")
    st.write("📍 [點我打開 Google 地圖導航](https://www.google.com/maps/search/?api=1&query=宜蘭縣五結鄉公園二路15號)")
    
    # 放一個重新播放的小按鈕在底部，以防萬一
    if st.button("🔄 重新觀看開場"):
        st.session_state['entered'] = False
        st.rerun()
