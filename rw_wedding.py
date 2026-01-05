import streamlit as st

# 1. 設定網頁標題
st.set_page_config(page_title="弘智 & 凡宸 婚禮邀請", page_icon="💍")

# 2. 初始化頁面狀態
if 'entered' not in st.session_state:
    st.session_state['entered'] = False

# ==========================================
#  頁面 A：封面進場頁 (置中版)
# ==========================================
if not st.session_state['entered']:
    # 使用 CSS 讓按鈕變寬一點，看起來比較大氣
    st.markdown(
        """
        <style>
        .stButton>button {
            width: 100%;
            border-radius: 20px;
            font-size: 18px;
        }
        </style>
        """, 
        unsafe_allow_html=True
    )
    
    # --- 1. 置中的文字 ---
    # 使用 HTML 語法 <h1> 和 <p> 搭配 text-align: center
    st.markdown("<h1 style='text-align: center;'>💌 誠摯邀請</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>弘智 & 凡宸 的婚禮派對</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: gray;'>Jan 31, 2026</p>", unsafe_allow_html=True)
    
    st.write("") # 留一點空白行
    st.write("") 

    # --- 2. 置中的按鈕 (使用欄位技巧) ---
    # 建立三個欄位：[左邊空白, 中間放按鈕, 右邊空白]
    col1, col2, col3 = st.columns([1, 2, 1]) 

    with col2:
        # 按鈕放在中間的欄位 (col2)
        if st.button("👉 點此開啟喜帖", type="primary"):
            st.session_state['entered'] = True
            st.rerun()

# ==========================================
#  頁面 B：婚禮主頁面
# ==========================================
else:
    # 1. 音樂自動播放 (因為剛才有按按鈕，這裡 100% 會播)
    st.audio("How_Long_Will_I_Love_You.mp3", format="audio/mp3", start_time=0, autoplay=True)

    # 2. 標題置中
    st.markdown("<h1 style='text-align: center;'>❤️ 弘智 & 凡宸</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>我們結婚了！歡迎大家來參加我們的婚宴。</p>", unsafe_allow_html=True)

    # 3. 婚紗照
    col1, col2 = st.columns(2)
    with col1:
        st.image("photo1.jpg", use_container_width=True) 
    with col2:
        st.image("photo2.jpg", use_container_width=True)

    # 4. 婚禮資訊
    st.markdown("---")
    st.markdown("<h3 style='text-align: center;'>📅 宴客資訊</h3>", unsafe_allow_html=True)
    
    # 使用 info 框框顯示資訊，比較整齊
    st.info("""
    **日期**：2026 年 1 月 31 日 (星期六)\n
    **時間**：12:00 宴客入席 / 12:30 午宴開席\n
    **地點**：香格里拉冬山河渡假飯店\n
    **地址**：宜蘭縣五結鄉公園二路 15 號
    """)

    # 5. 座位查詢
    st.markdown("<h3 style='text-align: center;'>🔍 查詢我的座位</h3>", unsafe_allow_html=True)
    
    seat_data = {
        "王大明": "男方大學同學桌 - A1",
        "林小美": "女方親戚桌 - B2",
        "任弘智": "新郎本人",
        "王凡宸": "新娘本人"
    }

    user_input = st.text_input("請輸入您的姓名或綽號 (例如：大谷翔平)")

    if user_input:
        result = seat_data.get(user_input.strip())
        if result:
            st.balloons()
            st.success(f"🎊 嗨 {user_input}！您的座位在：【{result}】")
        else:
            st.warning("查無資料，請確認名字是否輸入正確。")

    # 6. 地圖與底部
    st.markdown("---")
    # 按鈕置中技巧
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        st.link_button("📍 打開 Google 地圖導航", "https://www.google.com/maps/search/?api=1&query=宜蘭縣五結鄉公園二路15號")
    
    st.write("")
    if st.button("🔄 重新觀看開場"):
        st.session_state['entered'] = False
        st.rerun()
