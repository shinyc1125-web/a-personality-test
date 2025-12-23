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
        background-color: #FDFCF0; /* 따뜻한 아이보리 파스텔 */
    }
    
    /* 메인 컨테이너 스타일 */
    .main .block-container {
        padding-top: 2rem;
        max-width: 600px;
    }
    
    /* 마인크래프트 스타일 버튼 (Pixelated Look) */
    .stButton>button {
        width: 100%;
        background-color: #B2DFDB; /* 파스텔 민트 */
        color: #455A64;
        border: 4px solid #80CBC4;
        border-bottom: 6px solid #4DB6AC;
        border-radius: 0px;
        padding: 15px;
        font-size: 1.1rem;
        font-weight: 700;
        margin-bottom: 10px;
        transition: all 0.1s;
    }
    
    .stButton>button:hover {
        background-color: #80CBC4;
        color: white;
        border-bottom: 4px solid #4DB6AC;
        transform: translateY(2px);
    }

    .stButton>button:active {
        border-bottom: 2px solid #00796B;
        transform: translateY(4px);
    }
    
    /* 질문 박스 스타일 */
    .question-box {
        background-color: #FFF9C4; /* 연한 노랑 */
        padding: 30px;
        border: 3px dashed #FBC02D;
        border-radius: 4px;
        margin-bottom: 30px;
        text-align: center;
        box-shadow: 4px 4px 0px rgba(0,0,0,0.1);
    }
    
    .title-text {
        color: #5D4037;
        font-size: 2.5rem;
        font-weight: 800;
        text-align: center;
        margin-bottom: 5px;
        text-shadow: 2px 2px 0px #D7CCC8;
    }

    .progress-text {
        text-align: right;
        color: #78909C;
        font-size: 0.9rem;
        margin-bottom: 5px;
    }
    </style>
    """, unsafe_allow_stdio=True)

# 질문 데이터 세트 (총 12개)
questions = [
    {"q": "낯선 서버에 처음 접속했을 때 당신은?", "a": "전체 채팅으로 반갑게 인사하며 친구를 만든다.", "b": "사람이 없는 곳을 찾아 조용히 기지를 짓기 시작한다.", "type": "EI"},
    {"q": "집을 지을 때 가장 중요하게 생각하는 것은?", "a": "실제로 사용하기 편하고 효율적인 창고 시스템", "b": "세상에 하나뿐인 독창적이고 아름다운 외관", "type": "SN"},
    {"q": "친구가 열심히 모은 다이아몬드를 용암에 빠뜨렸다면?", "a": "어쩌다 그랬는지 묻고 다시 얻을 수 있는 방법을 계산한다.", "b": "친구가 얼마나 상심했을지 공감하며 위로의 말을 건넨다.", "type": "TF"},
    {"q": "모험을 떠나기 전 당신의 인벤토리는?", "a": "음식, 도구, 횃불이 용도별로 완벽하게 정리되어 있다.", "b": "뭐가 들어있는지 모르겠지만 일단 대충 챙겨서 나간다.", "type": "PJ"},
    {"q": "마을 주민과 거래를 할 때 당신의 스타일은?", "a": "여러 명과 대화하며 가장 이득이 되는 거래를 찾는다.", "b": "필요한 물건만 딱 사고 조용히 마을을 떠난다.", "type": "EI"},
    {"q": "새로운 업데이트 소식을 들었을 때 반응은?", "a": "추가된 아이템의 수치와 활용법을 꼼꼼히 확인한다.", "b": "새로운 지형이 줄 신비로운 분위기와 상상을 즐긴다.", "type": "SN"},
    {"q": "서버원들끼리 의견 충돌이 일어났을 때 당신은?", "a": "어떤 쪽이 더 논리적으로 타당한지 따져본다.", "b": "모두가 기분 상하지 않게 잘 마무리되는 쪽을 택한다.", "type": "TF"},
    {"q": "대규모 건축물을 지을 때 계획은?", "a": "청사진을 완벽히 그리고 재료 수급 계획부터 세운다.", "b": "일단 기초부터 쌓으면서 영감이 떠오르는 대로 만든다.", "type": "PJ"},
    {"q": "축제가 열린 서버 광장에서 당신은?", "a": "이벤트에 적극 참여하며 분위기를 주도한다.", "b": "구석에서 사람들이 노는 모습을 흐뭇하게 구경한다.", "type": "EI"},
    {"q": "동굴 속에서 처음 보는 구조물을 발견했다면?", "a": "함정이 있는지 살펴보고 보물 상자부터 체크한다.", "b": "이 구조물에 어떤 전설이 담겨 있을지 상상해본다.", "type": "SN"},
    {"q": "전쟁 서버에서 적 팀을 마주했을 때?", "a": "승리 확률을 분석하여 전략적으로 대응한다.", "b": "팀원들의 사기를 북돋우며 단결을 강조한다.", "type": "TF"},
    {"q": "오늘의 할 일을 정할 때 당신은?", "a": "접속 전부터 오늘 만들 리스트를 머릿속에 완성한다.", "b": "그날그날 끌리는 활동(광질, 낚시 등)을 즉흥적으로 한다.", "type": "PJ"},
]

# 테마 데이터
themes = {
    "따뜻한": {"color": "#FFD1DC", "icon": "🌸", "image": "벚꽃 숲 (Cherry Blossom)", "desc": "부드럽고 다정한 당신에게는 평화로운 벚꽃 숲 테마가 어울려요!"},
    "용감한": {"color": "#FFCCBC", "icon": "🔥", "image": "황금빛 요새 (Bastion)", "desc": "강한 의지를 가진 당신은 뜨거운 열정의 네더 테마가 딱이네요!"},
    "차분한": {"color": "#C8E6C9", "icon": "🌿", "image": "푸른 숲 (Lush Caves)", "desc": "사색을 즐기는 당신에게는 싱그러운 이끼와 꽃이 가득한 지하 정원을 추천해요."},
    "총명한": {"color": "#BBDEFB", "icon": "💎", "image": "마법 도서관 (Stronghold Library)", "desc": "지적 호기심이 많은 당신은 신비로운 도서관 테마가 어울립니다."}
}

# 세션 상태 초기화
if 'step' not in st.session_state:
    st.session_state.step = 0
if 'scores' not in st.session_state:
    st.session_state.scores = {"E":0, "I":0, "S":0, "N":0, "T":0, "F":0, "P":0, "J":0}

# 메인 헤더
st.markdown("<h1 class='title-text'>⛏️ 마크 성격 검사</h1>", unsafe_allow_stdio=True)
st.markdown("<p style='text-align: center; color: #8D6E63; margin-bottom: 20px;'>나의 마인크래프트 속 본캐는 무엇일까?</p>", unsafe_allow_stdio=True)

if st.session_state.step < len(questions):
    # 진행도 표시
    q_idx = st.session_state.step
    progress = (q_idx + 1) / len(questions)
    st.markdown(f"<p class='progress-text'>{q_idx + 1} / {len(questions)}</p>", unsafe_allow_stdio=True)
    st.progress(progress)
    
    q_data = questions[q_idx]
    
    st.markdown(f"<div class='question-box'><h3>{q_data['q']}</h3></div>", unsafe_allow_stdio=True)
    
    # 답변 버튼
    if st.button(q_data['a']):
        st.session_state.scores[q_data['type'][0]] += 1
        st.session_state.step += 1
        st.rerun()
            
    if st.button(q_data['b']):
        st.session_state.scores[q_data['type'][1]] += 1
        st.session_state.step += 1
        st.rerun()

else:
    # 결과 계산 (MBTI 로직)
    s = st.session_state.scores
    mbti = ""
    mbti += "E" if s["E"] >= s["I"] else "I"
    mbti += "S" if s["S"] >= s["N"] else "N"
    mbti += "T" if s["T"] >= s["F"] else "F"
    mbti += "J" if s["J"] >= s["P"] else "P"
    
    # 성격 수식어 결정
    trait = "착한" if "F" in mbti else "똑똑한"
    if "E" in mbti and "P" in mbti: trait = "활기찬"
    if "I" in mbti and "J" in mbti: trait = "사려 깊은"
    if "S" in mbti and "T" in mbti: trait = "든든한"
    
    st.balloons()
    
    # 결과 섹션
    st.markdown(f"""
        <div style='background-color: #FFFFFF; padding: 40px; border-radius: 10px; text-align: center; border: 5px solid #A8D5BA; box-shadow: 8px 8px 0px #E0E0E0;'>
            <p style='font-size: 1.2rem; color: #666;'>당신의 성격은...</p>
            <h1 style='color: #2E7D32; font-size: 3rem; margin: 10px 0;'>"{trait} {mbti}"</h1>
            <p style='font-size: 1.1rem; line-height: 1.6;'>
                마치 마인크래프트에서 <b>마을의 중심</b>이 되는 <br>
                멋진 건축가이자 모험가 같은 분이시네요!
            </p>
        </div>
    """, unsafe_allow_stdio=True)
    
    st.write("")
    
    # 테마 추천 로직
    theme_key = "따뜻한" if "F" in mbti else "총명한"
    if "S" in mbti and "T" in mbti: theme_key = "용감한"
    if "N" in mbti and "P" in mbti: theme_key = "차분한"
    
    selected_theme = themes[theme_key]
    
    # 추천 테마 섹션
    st.markdown("<h3 style='text-align: center;'>🎨 추천 이미지 테마</h3>", unsafe_allow_stdio=True)
    
    # 결과 카드
    with st.container():
        col1, col2 = st.columns([1, 2])
        with col1:
            st.markdown(f"""
                <div style='background-color: {selected_theme['color']}; height: 160px; border-radius: 15px; 
                display: flex; align-items: center; justify-content: center; border: 4px solid #5D4037;'>
                    <span style='font-size: 5rem;'>{selected_theme['icon']}</span>
                </div>
            """, unsafe_allow_stdio=True)
        with col2:
            st.markdown(f"### {selected_theme['image']}")
            st.write(selected_theme['desc'])
            st.code(f"추천 컬러 칩: {selected_theme['color']}", language="")

    st.write("")
    if st.button("처음부터 다시 하기"):
        st.session_state.step = 0
        st.session_state.scores = {"E":0, "I":0, "S":0, "N":0, "T":0, "F":0, "P":0, "J":0}
        st.rerun()

st.markdown("---")
st.markdown("<p style='text-align: center; color: #BDBDBD; font-size: 0.8rem;'>© 2024 Minecraft Style Personality Test. All Bricks Reserved.</p>", unsafe_allow_stdio=True)
