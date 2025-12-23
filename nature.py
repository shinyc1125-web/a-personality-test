import streamlit as st
from langchain_openai import ChatOpenAI
#from langchain.prompts import PromptTemplate
from langchain_core.prompts import PromptTemplate
#from langchain.chains import LLMChain
import os

# OpenAI API 키 가져오기
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    st.error("❌ OpenAI API 키가 설정되지 않았습니다. 환경 변수 'OPENAI_API_KEY'를 설정하세요.")
    st.stop()

# 모델 설정
model = ChatOpenAI(api_key=OPENAI_API_KEY, model="gpt-4o-mini")

# 해양관련 문구 생성 프롬프트
slogan_prompt_template = """
당신은 해양 전문가입니다.
입력된 키워드에 기반하여 연구·보호 프로젝트 제목을 3가지 제안하세요.
각 제목은 간결하고 핵심을 담아 30자 이내로 작성해주세요.

키워드: {keyword}
"""

slogan_prompt = PromptTemplate.from_template(slogan_prompt_template)
#slogan_chain = LLMChain(llm=model, prompt=slogan_prompt)
slogan_chain = slogan_prompt | model

# 해양관 계획서 프롬프트
plan_prompt_template = """
당신은 해양 기획자입니다.
아래 프로젝트 제목을 중심으로, 간단한 해양 프로젝트 기획서를 작성하세요.
기획서는 다음 내용을 포함해야 합니다:
1. 프로젝트 목적
2. 대상 지역/생태
3. 주요 실행 전략
4. 기대 효과

해양관 문구: "{slogan}"
"""

plan_prompt = PromptTemplate.from_template(plan_prompt_template)
#plan_chain = LLMChain(llm=model, prompt=plan_prompt)
plan_chain = plan_prompt | model

# Streamlit UI
st.title("🎯 키워드 기반 해양 프로젝트 기획서 생성기")

# Step 1: 키워드 입력
keyword = st.text_input("해양 프로젝트 키워드를 입력하세요", placeholder="예: 산호초 복원, 해양쓰레기 제거 등")

# Step 2: 문구 생성
if st.button("1️⃣ 프로젝트 제목 생성") and keyword.strip():
    with st.spinner("프로젝트 제목 생성 중..."):
        result = slogan_chain.invoke({"keyword": keyword})
        lines = [line.strip("- ").strip() for line in result["text"].strip().split("\n") if line.strip()]
        st.session_state["slogans"] = lines

# Step 3: 문구 선택 및 계획서 작성
if "slogans" in st.session_state and st.session_state["slogans"]:
    st.subheader("💡 생성된 해양 관련 문구")
    selected_slogan = st.radio("사용할 문구를 선택하세요", st.session_state["slogans"])

    if st.button("2️⃣ 기획서 생성 생성"):
        with st.spinner("기획서 생성성 중..."):
            plan_result = plan_chain.invoke({"slogan": selected_slogan})
            st.subheader("📋 해양 프로젝트 기획서")
            st.write(plan_result["text"])
