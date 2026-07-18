import streamlit as st
import pandas as pd

# 1. 페이지 기본 설정
st.set_page_config(
    page_title="박성진 | 금융 IT 수석 컨설턴트 프로필",
    page_icon="👨‍💼",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. 상단 프로필 헤더
st.title("👨‍💼 포트폴리오 및 프로필")
st.subheader("박성진 (Park Seong-Jin) | 금융 IT 수석 컨설턴트")

# 주요 인적 사항 및 연락처
col_meta1, col_meta2 = st.columns(2)
with col_meta1:
    st.write("✉️ **Email:** whitenuclear@gmail.com")
    st.write("📍 **Location:** 서울시 은평구 진관동")
with col_meta2:
    st.write("🏅 **기술 등급:** 소프트웨어 특급 기술자")
    st.write("🚀 **전문 분야:** 금융 인프라 / 차세대 시스템 구축")

st.markdown("---")

# 3. 핵심 역량 지표 (Core Metrics)
st.markdown("### 🚀 Core Competencies")
cm_col1, cm_col2, cm_col3 = st.columns(3)
with cm_col1:
    st.metric(label="총 경력 기간", value="20년 이상", delta="금융 IT 특화")
with cm_col2:
    st.metric(label="주요 전문 역할", value="PM / PL / SM")
with cm_col3:
    st.metric(label="핵심 도메인", value="은행 대외계 / 카드 발급")

st.markdown("---")

# 4. 전체 프로젝트 수행 이력 데이터 정의 (문법 오류 완벽 차단)
project_list = [
    {
        "기간": "2021.03 ~ 2024.12",
        "발주처": "신한은행",
        "프로젝트명": "신한은행 차세대 대외계 시스템 구축 및 고도화",
        "역할": "PM / 수석 컨설턴트",
        "구분": "대형 구축 (SI)",
        "상세업무": [
            "차세대 대외계 시스템 아키텍처 설계 및 총괄 관리",
            "대외 기관 연계 인프라 고도화 및 대용량 트랜잭션 최적화",
            "프로젝트 리스크 관리 및 발주처 요구사항 조율"
        ]
    },
    {
        "기간": "2018.06 ~ 2020.12",
        "발주처": "국민은행 / BC카드",
        "프로젝트名": "금융 플랫폼 연계 및 코어 뱅킹 대외 채널 확장",
        "역할": "PM / PL",
        "구분": "개발/컨설팅",
        "상세업무": [
            "이 기종 금융 시스템 간 인터페이스 표준화 및 연계 개발 총괄",
            "대내외 채널 연계 모듈 안정성 검증 및 성능 튜닝",
            "개발 파트너사 리딩 및 품질 관리(QA) 프로세스 확립"
        ]
    },
    {
        "기간": "2015.05 ~ 2018.02",
        "발주처": "신한카드",
        "프로젝트명": "신용카드 승인 및 코어 시스템 구조 개선",
        "역할": "PL / SM",
        "구분": "운영/고도화",
        "상세업무": [
            "카드 승인 및 정산 시스템 핵심 모듈 리팩토링",
            "대용량 금융 데이터 배치 처리 성능 개선 및 최적화",
            "시스템 장애 예방 조치 및 상시 모니터링 체계 구축"
        ]
    },
    {
        "기간": "2011.05 ~ 2015.02",
        "발주처": "신한은행",
        "프로젝트명": "나라사랑카드 발급 및 정산 시스템 유지보수",
        "역할": "PL / SM",
        "구분": "개발/운영",
        "상세업무": [
            "나라사랑카드 발급 대행 및 은행 내부 계정계 연계 운영 총괄",
            "군인 고객 대상 특화 서비스 인터페이스 안정적 유지보수",
            "정기 보안 점검 대응 및 법적 규제 준수를 위한 시스템 보완"
        ]
    }
]

# 데이터프레임 변환 (통계용)
df = pd.DataFrame(project_list)

# 5. 메인 탭 구성
tab1, tab2 = st.tabs(["📋 프로젝트 수행 이력", "📊 경력 요약 및 통계"])

with tab1:
    st.markdown("### 💻 상세 수행 프로젝트")
    st.write("최신 순으로 정렬된 프로젝트 수행 이력입니다. 각 프로젝트를 클릭하시면 상세 업무를 보실 수 있습니다.")
    
    # 반복문을 통해 확장 프로그램(Expander) 형태로 깔끔하게 배치
    for row in project_list:
        with st.expander(f"🔹 [{row['기간']}] {row['프로젝트명']} ({row['발주처']})", expanded=True):
            p_col1, p_col2 = st.columns(2)
            with p_col1:
                st.markdown(f"🏢 **발주처:** {row['발주처']}")
                st.markdown(f"📅 **수행 기간:** {row['기간']}")
            with p_col2:
                st.markdown(f"👤 **담당 역할:** {row['역할']}")
                st.markdown(f"🏷️ **프로젝트 구분:** {row['구분']}")
            
            st.markdown("**📝 주요 수행 업무 및 성과:**")
            for task in row['상세업무']:
                st.markdown(f"- {task}")

with tab2:
    st.markdown("### 📊 경력 데이터 요약 테이블")
    
    # 인터랙티브 테이블 제공 (상세 업무 제외하고 깔끔하게 표출)
    display_df = df[["기간", "발주처", "프로젝트명", "역할", "구분"]]
    st.dataframe(
        display_df, 
        use_container_width=True,
        hide_index=True
    )
    
    # 요약 카드 정보
    st.markdown("### 🔍 Career Summary")
    summary_col1, summary_col2 = st.columns(2)
    with summary_col1:
        st.info(f"💡 **총 프로젝트 수행:** {len(df)}개 대형 프로젝트 기술")
    with summary_col2:
        st.success("🎯 **주요 고객사:** 신한금융그룹(은행/카드), KB국민은행 등")

# 6. 푸터 (Footer) 영역
st.markdown("---")
st.caption("© 2026 Park Seong-Jin. All Rights Reserved.")
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
