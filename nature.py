import streamlit as st

# 페이지 설정
st.set_page_config(page_title="Personal Pastel Test", page_icon="✨", layout="centered")

# 커스텀 CSS로 파스텔 톤 디자인 적용
st.markdown("""
    <style>
    .main {
        background-color: #fdfcf0;
    }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        border: 2px solid #ffcfdf;
        background-color: #ffffff;
        color: #555;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #ffcfdf;
        color: white;
        border: 2px solid #ffcfdf;
    }
    .question-box {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #d0e1ff;
        margin-bottom: 20px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.05);
    }
    h1, h2, h3 {
        color: #6d6d6d;
    }
    .result-card {
        background-color: #f0f7f4;
        padding: 30px;
        border-radius: 20px;
        border: 1px dashed #a3d2ca;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# 질문 리스트 (12개)
questions = [
    "새로운 사람을 만나는 자리가 즐거우신가요?",
    "주말에는 집에서 쉬는 것보다 밖으로 나가는 게 좋나요?",
    "결정을 내릴 때 감정보다는 논리가 더 중요한가요?",
    "계획이 틀어지면 스트레스를 많이 받으시나요?",
    "주변 사람들의 기분을 잘 살피는 편인가요?",
    "창의적인 아이디어를 생각하는 것을 즐기시나요?",
    "어려운 일이 생기면 혼자 해결하는 편인가요?",
    "책이나 영화를 볼 때 감정 이입이 잘 되나요?",
    "정리정돈된 환경에서 더 효율이 오르나요?",
    "남들 앞에 서서 이야기하는 것이 두렵지 않나요?",
    "과거의 기억보다 미래의 가능성에 더 집중하시나요?",
    "반복적인 일상보다 변화무쌍한 삶이 더 좋나요?"
]

def main():
    st.title("✨ 나의 파스텔 성격 찾기")
    st.write("12개의 간단한 질문을 통해 당신의 성격과 어울리는 테마를 알아보세요.")
    st.divider()

    # 세션 상태 초기화
    if 'answers' not in st.session_state:
        st.session_state.answers = [None] * 12
    if 'step' not in st.session_state:
        st.session_state.step = 0

    # 검사 진행 로직
    if st.session_state.step < 12:
        current_q = st.session_state.step
        
        st.markdown(f"<div class='question-box'><h3>Q{current_q + 1}. {questions[current_q]}</h3></div>", unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("그렇다 (YES)"):
                st.session_state.answers[current_q] = True
                st.session_state.step += 1
                st.rerun()
        with col2:
            if st.button("아니다 (NO)"):
                st.session_state.answers[current_q] = False
                st.session_state.step += 1
                st.rerun()
        
        # 진행 바
        progress = (current_q) / 12
        st.progress(progress)
        st.caption(f"진행도: {current_q}/12")

    else:
        # 결과 계산 로직 (간단한 포인트 시스템)
        yes_count = sum(1 for a in st.session_state.answers if a is True)
        
        st.success("검사가 완료되었습니다! 결과를 분석 중입니다...")
        st.divider()

        # 결과 매칭
        result_title = ""
        result_desc = ""
        theme_image = ""

        if yes_count >= 10:
            result_title = "눈부신 햇살 같은 리더"
            result_desc = "당신은 에너지가 넘치고 사람들에게 밝은 영향을 주는 분이군요! 책임감이 강하고 다정한 성격입니다."
            theme_image = "따스한 오후의 정원"
        elif yes_count >= 7:
            result_title = "포근한 구름 같은 관찰자"
            result_desc = "주변을 잘 살피고 공감 능력이 뛰어난 분입니다. 평화를 사랑하며 조화로운 관계를 소중히 여깁니다."
            theme_image = "몽글몽글한 솜사탕 하늘"
        elif yes_count >= 4:
            result_title = "차분한 새벽녘의 사색가"
            result_desc = "논리적이고 독립적인 성향을 가지고 계시네요. 자신만의 세계가 뚜렷하며 깊이 있는 생각을 즐깁니다."
            theme_image = "정적인 미니멀리즘 작업실"
        else:
            result_title = "신비로운 숲 속의 요정"
            result_desc = "개성이 강하고 남다른 직관을 가진 분입니다. 조용하지만 내면에는 아주 큰 열정을 품고 있군요."
            theme_image = "비 온 뒤 촉촉한 숲길"

        # 결과 화면 출력
        st.markdown(f"""
            <div class='result-card'>
                <p style='font-size: 1.2rem; color: #888;'>당신의 성격은...</p>
                <h2 style='color: #ff9aa2;'>[{result_title}]</h2>
                <p style='font-size: 1.1rem; line-height: 1.6;'>{result_desc}</p>
                <hr style='border: 0.5px solid #eee;'>
                <p style='color: #a3d2ca; font-weight: bold;'>🎨 추천 이미지 테마: {theme_image}</p>
            </div>
        """, unsafe_allow_html=True)

        if st.button("다시 테스트하기"):
            st.session_state.answers = [None] * 12
            st.session_state.step = 0
            st.rerun()

if __name__ == "__main__":
    main()
