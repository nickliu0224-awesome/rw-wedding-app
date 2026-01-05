import streamlit as st

# 1. 設定網頁標題
st.set_page_config(page_title="弘智 & 凡宸 婚禮邀請", page_icon="💍")

# 2. 初始化頁面狀態
if 'entered' not in st.session_state:
    st.session_state['entered'] = False

# ==========================================
#  頁面 A：封面進場頁 (修正版)
# ==========================================
if not st.session_state['entered']:
    # 自訂 CSS 讓按鈕圓潤一點
    st.markdown(
        """
        <style>
        .stButton>button {
            border-radius: 20px;
            font-size: 18px;
            font-weight: bold;
        }
        </style>
        """, 
        unsafe_allow_html=True
    )
    
    # --- 1. 標題文字 ---
    st.markdown("<h1 style='text-align: center; margin-bottom: 0px;'>誠摯邀請</h1>", unsafe_allow_html=True)
    
    # --- 2. 信封圖示 (放在標題下方，設為超大字體) ---
    st.markdown("<div style='text-align: center; font-size: 80px; margin-top: 0px;'>💌</div>", unsafe_allow_html=True)
    
    # --- 3. 新人名字與日期 ---
    st.markdown("<h3 style='text-align: center;'>弘智 & 凡宸 的婚禮派對</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: gray;'>Jan 31, 2026</p>", unsafe_allow_html=True)
    
    st.write("") # 增加一點間距
    st.write("") 

    # --- 4. 按鈕置中 ---
    # 使用 [1, 2, 1] 的比例，並加上 use_container_width=True
    col1, col2, col3 = st.columns([1, 2, 1]) 

    with col2:
        # use_container_width=True 會讓按鈕填滿中間這個欄位，確保絕對置中
        if st.button("👉 點此開啟喜帖", type="primary", use_container_width=True):
            st.session_state['entered'] = True
            st.rerun()

# ==========================================
#  頁面 B：婚禮主頁面
# ==========================================
else:
    # 1. 音樂自動播放
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
    
    # 底部按鈕也幫你置中整理一下
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        st.link_button("📍 Google 地圖導航", "https://www.google.com/maps/search/?api=1&query=宜蘭縣五結鄉公園二路15號", use_container_width=True)
    
    st.write("")
    if st.button("🔄 重新觀看開場"):
        st.session_state['entered'] = False
        st.rerun()
