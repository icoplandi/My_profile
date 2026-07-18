import streamlit as st
import pandas as pd

# 1. 페이지 기본 설정
st.set_page_config(
    page_title="박성진 | 프로필",
    page_icon="👨‍💼",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. 타이틀 및 상단 프로필 헤더
st.title("👨‍💼 포트폴리오 및 프로필")
st.subheader("금융 IT 수석 컨설턴트 · 특급 기술자")

# 주요 연락처 정보 (안정적인 마크다운 사용)
st.write("✉️ **Email:** whitenuclear@gmail.com")
st.write("📍 **Location:** 서울시 은평구 진관동")
st.markdown("---")

# 3. 핵심 메트릭 (주요 역량 키워드)
st.markdown("### 🚀 Core Strengths")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="전문 분야", value="금융 IT 컨설팅")
with col2:
    st.metric(label="기술 등급", value="특급 기술자")
with col3:
    st.metric(label="주요 역할", value="PL / SM / PM")

st.markdown("---")

# 4. 프로젝트 수행 이력 데이터 정의 (들여쓰기 오류 원천 차단)
project_list = [
    {
        "기간": "2011.05 ~ 2015.02",
        "발주처": "신한은행",
        "프로젝트명": "나라사랑카드 발급 시스템 유지보수",
        "역할": "PL / SM",
        "구분": "개발/운영"
    }
    # 추가 프로젝트 이력이 필요할 경우 이 아래로 동일한 형식으로 추가하시면 됩니다.
]

# 데이터프레임 변환
df = pd.DataFrame(project_list)

# 5. 메인 화면 탭 구성
tab1, tab2 = st.tabs(["📋 프로젝트 수행 이력", "🔍 경력 요약 분석"])

with tab1:
    st.markdown("### 💻 수행 프로젝트 상세")
    
    # 각 프로젝트를 깔끔한 카드 형태로 출력
    for idx, row in df.iterrows():
        with st.container(border=True):
            st.markdown(f"#### 🔹 {row['프로젝트명']}")
            
            # 2단 레이아웃으로 정보 정렬
            p_col1, p_col2 = st.columns(2)
            with p_col1:
                st.write(f"📅 **기간:** {row['기간']}")
                st.write(f"🏢 **발주처:** {row['발주처']}")
            with p_col2:
                st.write(f"👤 **역할:** {row['역할']}")
                st.write(f"🏷️ **구분:** {row['구분']}")

with tab2:
    st.markdown("### 📊 프로젝트 통계 데이터")
    
    # 인터랙티브 데이터 테이블 제공
    st.dataframe(
        df, 
        use_container_width=True,
        hide_index=True
    )
    
    # 간단한 요약 정보
    st.info(f"💡 현재 등록된 총 프로젝트 수: {len(df)}건")

# 6. 푸터 (Footer) 영역
st.markdown("---")
st.caption("© 2026 Park Seong-Jin. All Rights Reserved.")
