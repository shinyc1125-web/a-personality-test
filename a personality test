import streamlit as st
import time

# 페이지 설정
st.set_page_config(
    page_title="마크풍 성격 검사",
    page_icon="⛏️",
    layout="centered"
)

# 마인크래프트 & 파스텔 스타일 CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Noto Sans KR', sans-serif;
        background-color: #F0F4F8; /* 연한 파스텔 블루 */
    }
    
    .main {
        background-color: #FFFFFF;
        border-radius: 15px;
        padding: 2rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
    }
    
    /* 마인크래프트 스타일 버튼 */
    .stButton>button {
        width: 100%;
        background-color: #A8D5BA; /* 파스텔 그린 */
        color: #4A4A4A;
        border: 3px solid #7FB994;
        border-radius: 0px;
        padding: 10px;
        font-weight: bold;
        transition: 0.3s;
    }
    
    .stButton>button:hover {
        background-color: #7FB994;
        color: white;
        transform: translateY(-2px);
    }
    
    .question-box {
        background-color: #FFF9C4; /* 파스텔 옐로우 */
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #FFEB3B;
        margin-bottom: 20px;
    }
    
    h1 {
        color: #5D4037;
        text-align: center;
        border-bottom: 2px dashed #D7CCC8;
        padding-bottom: 10px;
    }
    </style>
    """, unsafe_allow_stdio=True)

# 질문 데이터 세트 (E/I, S/N, T/F, P/J 성향 측정용)
questions = [
    {"q": "새로운 서버에 접속했을 때 당신은?", "a": "사람들에게 먼저 인사한다", "b": "조용히 혼자 집 지을 자리를 찾는다", "type": "EI"},
    {"q": "동굴 탐험 중 갈림길이 나왔다!", "a": "일단 직진해서 부딪혀본다", "b": "횃불로 표시를 남기며 신중히 이동한다", "type": "SN"},
    {"q": "친구가 공들여 만든 집이 폭발했다면?", "a": "누가 그랬는지 범인을 찾거나 복구법을 논의한다", "b": "놀란 친구의 마음을 먼저 다독여준다", "type": "TF"},
    {"q": "조합법을 외울 때 당신의 스타일은?", "a": "하다 보면 외워지겠지 하고 바로 시작한다", "b": "책이나 위키를 정독하고 시작한다", "type": "PJ"},
    {"q": "마을 주민들과 거래할 때 당신은?", "a": "필요한 물건을 위해 적극적으로 흥정한다", "b": "주민들이 주는 대로 적당히 거래한다", "type": "EI"},
    {"q": "건축을 할 때 가장 중요한 것은?", "a": "기능적이고 효율적인 공간 배치", "b": "나만의 개성이 담긴 독특한 디자인", "type": "SN"},
    {"q": "서버 규칙을 어긴 유저를 발견했다면?", "a": "원칙대로 신고하거나 처벌을 요구한다", "b": "이유가 있었는지 물어보고 좋게 해결하려 한다", "type": "TF"},
    {"q": "상자 정리, 어떻게 하시나요?", "a": "대충 쑤셔넣고 나중에 찾는다", "b": "아이템별로 엄격하게 분류해서 정리한다", "type": "PJ"},
    {"q": "대규모 건축 프로젝트가 열렸다면?", "a": "사람들과 협동하며 역할을 나눈다", "b": "나만의 작은 부분을 맡아 묵묵히 만든다", "type": "EI"},
    {"q": "엔더 드래곤을 잡으러 갈 때?", "a": "충분한 장비를 갖추고 완벽한 계획을 세운다", "b": "일단 침대랑 칼만 들고 돌진한다", "type": "PJ"},
    {"q": "농사를 지을 때 당신의 모습은?", "a": "최대한 넓고 기계적으로 자동화한다", "b": "아기자기하고 예쁜 정원처럼 꾸민다", "type": "SN"},
    {"q": "누군가 내 상자에서 아이템을 가져갔다면?", "a": "논리적으로 따져서 돌려받는다", "b": "속상하지만 그럴만한 사정이 있었겠지 생각한다", "type": "TF"},
]

# 결과 데이터
results = {
    "EI": ["외향적인 리더", "내향적인 장인"],
    "SN": ["창의적인 건축가", "현실적인 탐험가"],
    "TF": ["이성적인 전략가", "따뜻한 중재자"],
    "PJ": ["계획적인 관리자", "자유로운 모험가"]
}

themes = {
    "따뜻한": {"color": "#FFD1DC", "image": "벚꽃 숲 (Cherry Blossom Grove)", "desc": "부드럽고 평화로운 느낌의 테마입니다."},
    "용감한": {"color": "#FFCCBC", "image": "네더의 폐허 (Nether Wastes)", "desc": "뜨거운 열정과 도전 정신이 느껴지는 테마입니다."},
    "차분한": {"color": "#C8E6C9", "image": "깊은 바다 (Deep Ocean)", "desc": "고요하고 깊은 사색에 잠길 수 있는 테마입니다."},
    "총명한": {"color": "#BBDEFB", "image": "하늘 섬 (The End Sky)", "desc": "신비롭고 지적인 분위기를 풍기는 테마입니다."}
}

# 세션 상태 초기화
if 'step' not in st.session_state:
    st.session_state.step = 0
if 'scores' not in st.session_state:
    st.session_state.scores = {"E":0, "I":0, "S":0, "N":0, "T":0, "F":0, "P":0, "J":0}

# 메인 UI
st.title("⛏️ 마크풍 성격 검사")

if st.session_state.step < len(questions):
    # 진행도 표시
    progress = (st.session_state.step + 1) / len(questions)
    st.progress(progress)
    
    q_data = questions[st.session_state.step]
    
    st.markdown(f"<div class='question-box'><h3>Q{st.session_state.step + 1}. {q_data['q']}</h3></div>", unsafe_allow_stdio=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button(q_data['a']):
            type_char = q_data['type'][0]
            st.session_state.scores[type_char] += 1
            st.session_state.step += 1
            st.rerun()
            
    with col2:
        if st.button(q_data['b']):
            type_char = q_data['type'][1]
            st.session_state.scores[type_char] += 1
            st.session_state.step += 1
            st.rerun()

else:
    # 결과 계산
    s = st.session_state.scores
    mbti = ""
    mbti += "E" if s["E"] >= s["I"] else "I"
    mbti += "S" if s["S"] >= s["N"] else "N"
    mbti += "T" if s["T"] >= s["F"] else "F"
    mbti += "J" if s["J"] >= s["P"] else "P"
    
    # 결과 텍스트 매칭
    trait = "착한" if "F" in mbti else "똑똑한"
    if "E" in mbti and "P" in mbti: trait = "활기찬"
    if "I" in mbti and "J" in mbti: trait = "성실한"
    
    st.balloons()
    st.success("검사가 완료되었습니다!")
    
    # 결과 박스
    st.markdown(f"""
        <div style='background-color: #E8F5E9; padding: 30px; border-radius: 20px; text-align: center; border: 4px double #4CAF50;'>
            <h2 style='color: #2E7D32;'>당신은 "{trait} {mbti} 유형" 입니다!</h2>
            <p style='font-size: 1.2rem;'>마치 마인크래프트의 <b>전문 건축가</b> 같은 면모를 가지고 계시네요.</p>
        </div>
    """, unsafe_allow_stdio=True)
    
    st.divider()
    
    # 테마 추천
    theme_key = "따뜻한" if "F" in mbti else "총명한"
    if "S" in mbti and "T" in mbti: theme_key = "용감한"
    if "N" in mbti and "P" in mbti: theme_key = "차분한"
    
    selected_theme = themes[theme_key]
    
    st.subheader("🎨 당신에게 어울리는 마크 이미지 테마")
    
    col_img, col_txt = st.columns([1, 1.5])
    
    with col_img:
        # 픽셀 느낌의 박스
        st.markdown(f"""
            <div style='width: 100%; height: 150px; background-color: {selected_theme['color']}; 
            border: 5px solid #5D4037; display: flex; align-items: center; justify-content: center;'>
                <span style='font-size: 3rem;'>🧊</span>
            </div>
        """, unsafe_allow_stdio=True)
        
    with col_txt:
        st.markdown(f"### {selected_theme['image']}")
        st.write(selected_theme['desc'])
        st.info(f"추천 컬러 코드: {selected_theme['color']}")

    if st.button("다시 테스트하기"):
        st.session_state.step = 0
        st.session_state.scores = {"E":0, "I":0, "S":0, "N":0, "T":0, "F":0, "P":0, "J":0}
        st.rerun()

st.markdown("<br><p style='text-align: center; color: #9E9E9E;'>Crafted with Pastel Bricks 🧱</p>", unsafe_allow_stdio=True)
