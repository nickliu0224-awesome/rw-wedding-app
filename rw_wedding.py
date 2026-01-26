import streamlit as st

# 1. 設定網頁標題
st.set_page_config(page_title="弘智 & 凡宸 婚禮邀請", page_icon="💍")

# 2. 初始化頁面狀態
if 'entered' not in st.session_state:
    st.session_state['entered'] = False

# ==========================================
#  頁面 A：封面進場頁
# ==========================================
if not st.session_state['entered']:
    # 自訂 CSS
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
    
    # 標題與圖示
    st.markdown("<h1 style='text-align: center; margin-bottom: 0px;'>誠摯邀請</h1>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: center; font-size: 80px; margin-top: 0px;'>💌</div>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>弘智 & 凡宸 的婚禮派對</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: gray;'>Jan 31, 2026</p>", unsafe_allow_html=True)
    
    st.write("") 
    st.write("") 

    # 進場按鈕
    col1, col2, col3 = st.columns([1, 2, 1]) 
    with col2:
        if st.button("👉 點此開啟喜帖", type="primary", use_container_width=True):
            st.session_state['entered'] = True
            st.rerun()

# ==========================================
#  頁面 B：婚禮主頁面
# ==========================================
else:
    # --- 1. 新人資訊 ---
    st.markdown("<h1 style='text-align: center;'>❤️ 弘智 & 凡宸</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>我們結婚了！歡迎大家來參加我們的婚宴。</p>", unsafe_allow_html=True)

    # --- 2. 婚紗照 ---
    col1, col2 = st.columns(2)
    with col1:
        st.image("photo1.jpg", use_container_width=True) 
    with col2:
        st.image("photo2.jpg", use_container_width=True)

    # --- 3. 婚禮資訊 ---
    st.markdown("---")
    st.markdown("<h3 style='text-align: center;'>📅 宴客資訊</h3>", unsafe_allow_html=True)
    
    st.info("""
    **日期**：2026 年 1 月 31 日 (星期六)\n
    **時間**：12:00 宴客入席 / 12:30 午宴開席\n
    **地點**：香格里拉冬山河渡假飯店\n
    **地址**：宜蘭縣五結鄉公園二路 15 號
    """)

    # --- 4. 座位查詢 ---
    st.markdown("<h3 style='text-align: center;'>🔍 查詢我的座位</h3>", unsafe_allow_html=True)
    
    # 這裡已經填入你 CSV 檔案中的所有資料
    seat_data = {
        "何覲廷": "第6桌", "小羽": "第6桌", "陳賢鉦": "第6桌", "彭善玉": "第6桌", 
        "小玉": "第6桌", "Nick": "第6桌", "劉恩廷": "第6桌", "中和周湯豪": "第6桌", 
        "何佩珊": "第6桌", "莎莎": "第6桌", "育聖": "第6桌", "育聖叔叔": "第6桌", 
        "張哲豪": "第6桌", "蘇昱賢": "第7桌", "呂哲維": "第7桌", "林毅竹": "第7桌", 
        "陳鈞偉": "第7桌", "林文郁": "第7桌", "黃顏維霆": "第7桌", "賴奕文": "第7桌", 
        "林薘興": "第7桌", "林琮軒": "第8桌", "楊立任": "第8桌", "楊立群": "第8桌", 
        "張立憲": "第8桌", "康慧卿": "第8桌", "林彥妤": "第8桌", "林詠琳": "第8桌", 
        "王正文": "第9桌", "張廷碩": "第9桌", "黃竣瑋": "第9桌", "廖君珊": "第9桌", 
        "陳品妤": "第9桌", "周怡岑": "第9桌", "鍾家順": "第9桌", "黃于儂": "第10桌", 
        "Bo": "第10桌", "林敬翔": "第10桌", "Amber": "第10桌", "林俊宏": "第10桌", 
        "小龜": "第10桌", "蕭昱騰": "第10桌", "小騰": "第10桌", "王秋竣": "第10桌", 
        "秋哥": "第10桌", "鄭睿恩": "第11桌", "鍾家蕎": "第11桌", "陳柏毅": "第11桌", 
        "謝沂蓁": "第11桌", "崔西": "第11桌", "Tracy": "第11桌", "劉柏希": "第11桌", 
        "蕭凱仁": "第11桌", "李坤騰": "第11桌", "唐子鈞": "第12桌", "林杜萱": "第12桌", 
        "林士澤": "第12桌", "廖毓麟": "第12桌", "林嘉瑞": "第12桌", "余奕誠": "第12桌", 
        "海綿寶寶": "第12桌", "林佑穎": "第12桌", "小巨人": "第12桌", "陳昱凱": "第12桌", 
        "邱政民": "第13桌", "林可薇": "第13桌", "謝承祐": "第13桌", "蕭文心": "第13桌", 
        "孫雅鈺": "第13桌", "林煜珩": "第13桌", "陳韻如": "第13桌", "江崇銘": "第13桌", 
        "Summer": "第13桌", "李建華": "第14桌", "廖翊丞": "第14桌", "陳震陽": "第14桌", 
        "林榮松": "第14桌", "松哥": "第14桌", "徐湘菱": "第14桌", "陳彥銘": "第14桌", 
        "周威權": "第14桌", "大周": "第14桌", "游鈞雯": "第15桌", "林佩諭": "第15桌", 
        "Clock": "第15桌", "倪韻如": "第15桌", "徐妤苮": "第15桌", "徐以璇": "第15桌", 
        "陳葳": "第15桌", "朱晴": "第15桌", "伍倬慧": "第15桌", "兔子": "第15桌", 
        "林易庭廣": "第15桌", "Woof": "第15桌", "詹雅喻": "第15桌", "王希彤": "第15桌", 
        "陳妙慧": "第16桌", "何品萱": "第16桌", "黃鉅洋": "第16桌", "孫佩蓉": "第16桌", 
        "饅頭": "第16桌", "伊伊": "第16桌", "仔仔": "第16桌", "陳庭萱": "第17桌", "陳學志": "第17桌", "楊承恕": "第17桌", 
        "陳品怡": "第17桌", "周韋伶": "第17桌", "廖子淯": "第17桌", "王偉全": "第17桌", 
        "陳怡彤": "第18桌", "寶寶": "第18桌", "林雨薐": "第18桌", "王姿蓉": "第18桌", 
        "章玉瀅": "第18桌", "林玹滋": "第18桌", "林捷": "第18桌", "彭思融": "第18桌", 
        "仁宏": "第18桌", "宜汝": "第18桌", "余宗澤": "第19桌", "吳珮慈": "第19桌", 
        "豬仔": "第19桌", "吳瑀芯": "第19桌", "吳堉宏": "第19桌", "吳濬宇": "第19桌", 
        "啾啾": "第19桌", "嫂嫂": "第19桌", "陳馥萱": "第19桌", "林宜璇": "第2桌", 
        "游子萱": "第2桌", "賴宗男": "第2桌", "賴星宏": "第2桌", "何明儒": "第2桌", 
        "李均慧": "第16桌",
        # 額外保留新人資料
        "任弘智": "新郎本人",
        "王凡宸": "新娘本人"
    }

    user_input = st.text_input("請輸入您的姓名或綽號 (例如：大谷翔平)")

    if user_input:
        # 這裡會去除使用者輸入前後的空白，避免輸入錯誤
        result = seat_data.get(user_input.strip())
        if result:
            st.balloons()
            st.success(f"🎊 嗨 {user_input}！您的座位在：【{result}】")
        else:
            st.warning("查無資料，請確認名字是否輸入正確。")

    # --- 5. 地圖與底部區域 ---
    
    # 1. 頂部與查詢區的分隔線
    st.markdown("<hr style='margin: 30px 0px 0px 0px; border: 1px solid #f0f2f6;'>", unsafe_allow_html=True)
    
    # 2. 按鈕上方的空格
    st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)
    
    # 3. 地圖導航按鈕
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        st.link_button("📍 Google 地圖導航至飯店", "https://www.google.com/maps/search/?api=1&query=宜蘭縣五結鄉公園二路15號", use_container_width=True)
    
    # 4. 按鈕下方的空格
    st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)

    # --- 6. 音樂播放器 ---
    st.audio("How_Long_Will_I_Love_You.mp3", format="audio/mp3", start_time=0, autoplay=True)
