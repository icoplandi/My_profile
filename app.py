import streamlit as st
import pandas as pd

# 1. 페이지 기본 설정 및 디자인 테마 적용 (금융의 신뢰감을 주는 Deep Navy 테마)
st.set_page_config(
    page_title="금융 IT 전문 PM · PMO | 박성진 포트폴리오",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="collapsed" # 모바일에서 사이드바가 기본으로 접혀 화면을 가리지 않도록 설정
)

# 커스텀 CSS 주입 (모바일 화면 가로 잘림 방지 최적화)
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;700;900&display=swap');
        html, body, [class*="css"] {
            font-family: 'Noto Sans KR', sans-serif;
        }
        
        /* 모바일 가로 스크롤 및 잘림 방지 */
        .main .block-container {
            padding: 15px 10px !important;
            max-width: 100% !important;
            overflow-x: hidden;
        }
        
        /* 메인 배너 스타일 (모바일 대응 여백 조절) */
        .hero-section {
            background: linear-gradient(135deg, #0A192F 0%, #172A45 100%);
            color: #FFFFFF;
            padding: 25px 20px;
            border-radius: 12px;
            margin-bottom: 20px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            border-left: 6px solid #F5A623;
        }
        
        /* 핵심 메트릭 카드 (모바일에서 세로로 예쁘게 정렬되도록 설정) */
        .metric-card {
            background-color: #F8FAFC;
            border: 1px solid #E2E8F0;
            border-radius: 10px;
            padding: 15px;
            text-align: center;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
            margin-bottom: 10px;
        }
        .metric-num {
            font-size: 28px;
            font-weight: 800;
            color: #0A192F;
        }
        .metric-label {
            font-size: 13px;
            color: #64748B;
            margin-top: 3px;
        }
        
        /* 기술 태그 */
        .tech-tag {
            display: inline-block;
            background-color: #E2E8F0;
            color: #1E293B;
            padding: 4px 10px;
            border-radius: 15px;
            font-size: 12px;
            font-weight: 500;
            margin: 3px;
        }
    </style>
""", unsafe_allow_html=True)

# 2. 프로필 영역 (모바일 상단 배치를 위해 사이드바 대신 메인 화면 윗부분에 배치)
st.markdown("""
    <div style='text-align: center; margin-bottom: 25px; padding: 20px; background-color: #F8FAFC; border-radius: 12px; border: 1px solid #E2E8F0;'>
        <span style='font-size: 60px;'>👨‍💼</span>
        <h2 style='margin: 10px 0 5px 0; color:#0A192F; font-weight: 700;'>박성진 수석</h2>
        <p style='color: #64748B; font-size: 14px; margin-bottom: 15px;'>금융 IT 수석 컨설턴트 · 특급 기술자 | whitenuclear@gmail.com</p>
        <div style='max-width: 500px; margin: 0 auto; text-align: center;'>
            <span class='tech-tag'>PM / PMO</span>
            <span class='tech-tag'>QA & TA</span>
            <span class='tech-tag'>C / Pro*C</span>
            <span class='tech-tag'>Java</span>
            <span class='tech-tag'>금융 그룹웨어</span>
            <span class='tech-tag'>마케팅 플랫폼</span>
            <span class='tech-tag'>펌뱅킹</span>
        </div>
    </div>
""", unsafe_allow_html=True)

# 3. 메인 소개 배너
st.markdown("""
    <div class="hero-section">
        <span style="font-size: 11px; text-transform: uppercase; letter-spacing: 1px; color: #F5A623; font-weight: 700;">Financial IT Expert Portfolio</span>
        <h2 style="margin: 5px 0 10px 0; font-size: 24px; font-weight: 800; color: white; line-height: 1.3;">금융 시스템의 가치를 만드는 전문가</h2>
        <p style="font-size: 14px; font-weight: 300; line-height: 1.6; color: #E2E8F0; margin: 0;">
            지난 25년간 제일은행, 신한은행 등 대한민국 금융권의 핵심 인프라를 구축하고 안정적으로 관리해 왔습니다. 
            대규모 프로젝트의 성공적인 납품을 이끄는 파트너가 되겠습니다.
        </p>
    </div>
""", unsafe_allow_html=True)

# 핵심 성과 지표 (모바일 반응형 레이아웃)
col1, col2 = st.columns(2)
with col1:
    st.markdown('<div class="metric-card"><div class="metric-num">25Y+</div><div class="metric-label">총 IT 경력</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="metric-card"><div class="metric-num">특급</div><div class="metric-label">SW 기술자 등급</div></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="metric-card"><div class="metric-num">7건</div><div class="metric-label">PM/PL 프로젝트 총괄</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="metric-card"><div class="metric-num">100%</div><div class="metric-label">프로젝트 성공 수행률</div></div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# 4. 경력 상세 및 검색/필터링 기능
st.markdown("<h3 style='color:#0A192F; font-weight: 700;'>💼 프로젝트 수행 이력</h3>", unsafe_allow_html=True)

# 프로젝트 데이터셋
projects_data = [
    {"기간": "2024.08 ~ 2025.09", "발주처": "신한DS", "프로젝트명": "스윙 (신한금융그룹 그룹웨어) 유지보수", "역할": "품질점검, 제3자 테스트", "구분": "PMO/QA"},
    {"기간": "2022.12 ~ 2023.06", "발주처": "신한금융지주", "프로젝트명": "ESG Data 플랫폼 구축", "역할": "PMO (QA, TA)", "구분": "PMO/QA"},
    {"기간": "2022.03 ~ 2022.09", "발주처": "신한은행", "프로젝트명": "기업신용정보시스템 업그레이드 개발", "역할": "PM", "구분": "PM"},
    {"기간": "2021.02 ~ 2021.09", "발주처": "신한은행", "프로젝트명": "영업지원 원클릭 마케팅 플랫폼 구축", "역할": "PM", "구분": "PM"},
    {"기간": "2019.06 ~ 2020.12", "발주처": "신한금융지주", "프로젝트명": "신한경력컨설팅센터 통합", "역할": "PM", "구분": "PM"},
    {"기간": "2019.06 ~ 2020.12", "발주처": "신한은행", "프로젝트명": "사회공헌 홈페이지 통합 구축", "역할": "PM", "구분": "PM"},
    {"기간": "2015.03 ~ 2019.03", "발주처": "신한은행", "프로젝트명": "ATMS / 가상계좌 / 펌뱅킹 시스템 유지보수", "역할": "PL / SM", "구분": "개발/운영"},
    {"기간": "2011.05 ~ 2015.02", "발주처": "신한은행", "프로젝트명": "나라사랑카드 발급 시스템 유지보수", "역할": "PL / SM", "구분": "개발/운영"},
    {"기간": "2009.09 ~ 2011.05", "발주처": "신한은행", "프로젝트명": "등록금 웹 시스템 구축 및 유지보수", "역할": "PM / PL", "구분": "PM"},
    {"기간": "2007.11 ~ 2009.08", "발주처": "신한은행", "프로젝트명": "부수 업무 유지보수", "역할": "개발자", "구분": "개발/운영"},
    {"기간": "2002.03 ~ 2007.11", "발주처": "제일은행", "프로젝트명": "제일은행 부수 업무 유지보수", "역할": "개발자", "구분": "개발/운영"},
]

df = pd.DataFrame(projects_data)

# 필터 인터페이스 (경고를 피하기 위해 st.selectbox에 label_visibility 적용)
filter_col1, filter_col2 = st.columns(2)
with filter_col1:
    role_filter = st.selectbox("업무 구분", ["전체 보기", "PM", "PMO/QA", "개발/운영"])
with filter_col2:
    client_filter = st.selectbox("발주처", ["전체 보기", "신한은행", "신한금융지주", "신한DS", "제일은행"])

search_query = st.text_input("프로젝트명 직접 검색 🔍", placeholder="검색어를 입력하세요...")

# 필터링 로직 작동
filtered_df = df.copy()
if role_filter != "전체 보기":
    filtered_df = filtered_df[filtered_df["구분"] == role_filter]
if client_filter != "전체 보기":
    filtered_df = filtered_df[filtered_df["발주처"] == client_filter]
if search_query:
    filtered_df = filtered_df[filtered_df["프로젝트명"].str.contains(search_query, case=False)]

# 결과 테이블 출력 (모바일 가로잘림 현상이 없도록 대안 UI 적용)
st.markdown("<br>", unsafe_allow_html=True)
if not filtered_df.empty:
    # 모바일 기기 배려: 일반 표 대신 세로형 카드 레이아웃으로 데이터 리스트 표현
    for idx, row in filtered_df.iterrows():
        st.markdown(f"""
            <div style="background-color: #FFFFFF; border: 1px solid #E2E8F0; padding: 12px 15px; border-radius: 8px; margin-bottom: 10px;">
                <div style="display: flex; justify-content: space-between; font-size: 12px; color: #64748B; margin-bottom: 5px;">
                    <span>📅 {row['기간']}</span>
                    <span style="background-color: #E0F2FE; color: #0369A1; padding: 2px 6px; border-radius: 4px; font-weight: bold;">{row['발주처']}</span>
                </div>
                <div style="font-weight: 700; font-size: 14px; color: #0F172A; margin-bottom: 5px;">{row['프로젝트명']}</div>
                <div style="font-size: 13px; color: #475569;"><span style="color:#0A192F; font-weight: 500;">담당 역할:</span> {row['역할']}</div>
            </div>
        """, unsafe_allow_html=True)
else:
    st.info("조건에 일치하는 프로젝트가 없습니다.")

# 5. 푸터 영역 (연락처 및 저작권 정보)
st.markdown("""
    <div style="text-align: center; margin-top: 40px; padding: 20px; background-color: #0A192F; color: #94A3B8; border-radius: 10px;">
        <p style="margin: 0; font-size: 12px;">본 페이지는 스마트폰 반응형에 최적화되어 제작되었습니다.</p>
        <p style="margin: 5px 0 0 0; font-size: 12px; color: #F5A623; font-weight: bold;">© 2026 Park Seong-Jin. All Rights Reserved.</p>
    </div>
""", unsafe_allow_html=True)
            padding: 20px;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0,0,0,0.05);
            transition: transform 0.2s;
        }
        .metric-card:hover {
            transform: translateY(-5px);
            border-color: #0A192F;
        }
        .metric-num {
            font-size: 32px;
            font-weight: 800;
            color: #0A192F;
        }
        .metric-label {
            font-size: 14px;
            color: #64748B;
            margin-top: 5px;
        }
        
        /* 기술 태그 */
        .tech-tag {
            display: inline-block;
            background-color: #E2E8F0;
            color: #1E293B;
            padding: 4px 10px;
            border-radius: 15px;
            font-size: 13px;
            font-weight: 500;
            margin: 3px;
        }
    </style>
""", unsafe_allow_html=True)

# 2. 사이드바 - 핵심 프로필 정보
with st.sidebar:
    st.markdown("<h2 style='color:#0A192F; text-align:center;'>PROFILE</h2>", unsafe_allow_html=True)
    
    # 아바타 대체 아이콘 및 이름
    st.markdown("""
        <div style='text-align: center; margin-bottom: 20px;'>
            <span style='font-size: 80px;'>👨‍💼</span>
            <h3 style='margin: 10px 0 5px 0; color:#0A192F;'>박성진</h3>
            <p style='color: #64748B; font-size: 14px;'>금융 IT 수석 컨설턴트 / 특급 기술자</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # 인적사항 요약 (리스트 스타일)
    st.markdown("""
        **📧 이메일**<br>whitenuclear@gmail.com<br><br>
        **🎓 학력**<br>광운대학교 대학원 (석사)<br><br>
        **🏆 등급**<br>특급 IT 기술자 (경력 25년+)<br><br>
        **🎯 핵심 역량**<br>PM / PMO / 시스템 설계 & 개발
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # 핵심 기술 태그 클라우드
    st.markdown("**🛠️ Technical Stack**")
    tech_stacks = ["PM / PMO", "QA & TA", "C / Pro*C", "Java", "금융 그룹웨어", "대고객 마케팅 플랫폼", "펌뱅킹", "가상계좌"]
    tags_html = "".join([f"<span class='tech-tag'>{tech}</span>" for tech in tech_stacks])
    st.markdown(tags_html, unsafe_allow_html=True)

# 3. 메인 콘텐츠 영역
# 헤더 비주얼 영역 (Hero Section)
st.markdown("""
    <div class="hero-section">
        <span style="font-size: 14px; text-transform: uppercase; letter-spacing: 1.5px; color: #F5A623; font-weight: 700;">Financial IT Expert Portfolio</span>
        <h1 style="margin: 5px 0 15px 0; font-size: 38px; font-weight: 900; color: white;">박성진 | 금융 시스템의 가치를 만드는 전문가</h1>
        <p style="font-size: 16px; font-weight: 300; line-height: 1.6; max-width: 900px; color: #E2E8F0;">
            지난 25년간 제일은행, 신한은행, 신한금융지주 등 대한민국 선두 금융권의 핵심 인프라를 구축하고 안정적으로 운영해 왔습니다. 
            대규모 프로젝트의 총괄 PM 및 품질을 보증하는 PMO(QA/TA)로서 사업의 성공적인 납품을 약속합니다.
        </p>
    </div>
""", unsafe_allow_html=True)

# 핵심 성과 하이라이트 (Metrics)
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown('<div class="metric-card"><div class="metric-num">25Y+</div><div class="metric-label">총 IT 경력</div></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="metric-card"><div class="metric-num">7건</div><div class="metric-label">PM / PL 프로젝트 총괄</div></div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="metric-card"><div class="metric-num">특급</div><div class="metric-label">소프트웨어 기술 등급</div></div>', unsafe_allow_html=True)
with col4:
    st.markdown('<div class="metric-card"><div class="metric-num">100%</div><div class="metric-label">금융 프로젝트 성공률</div></div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# 4. 경력 상세 및 필터링 기능 (인터랙티브 기능 추가)
st.markdown("<h2 style='color:#0A192F;'>💼 프로젝트 수행 이력</h2>", unsafe_allow_html=True)
st.write("금융권에서 수행한 주요 프로젝트 목록입니다. 역할이나 발주처별로 필터링하여 확인하실 수 있습니다.")

# 프로젝트 데이터셋 생성
projects_data = [
    {"프로젝트명": "스윙 (신한금융그룹 그룹웨어) 시스템 유지보수", "기간": "2024.08 ~ 2025.09", "역할": "품질점검, 제3자 테스트", "발주처": "신한DS", "구분": "PMO/QA"},
    {"프로젝트명": "ESG Data 플랫폼 구축", "기간": "2022.12 ~ 2023.06", "역할": "PMO (QA, TA)", "발주처": "신한금융지주", "구분": "PMO/QA"},
    {"프로젝트명": "기업신용정보시스템 업그레이드 개발", "기간": "2022.03 ~ 2022.09", "역할": "PM", "발주처": "신한은행", "구분": "PM"},
    {"프로젝트명": "영업지원 원클릭 마케팅 플랫폼 구축", "기간": "2021.02 ~ 2021.09", "역할": "PM", "발주처": "신한은행", "구분": "PM"},
    {"프로젝트명": "신한경력컨설팅센터 통합", "기간": "2019.06 ~ 2020.12", "역할": "PM", "발주처": "신한금융지주", "구분": "PM"},
    {"프로젝트명": "사회공헌 홈페이지 통합 구축", "기간": "2019.06 ~ 2020.12", "역할": "PM", "발주처": "신한은행", "구분": "PM"},
    {"프로젝트명": "ATMS / 가상계좌 / 펌뱅킹 시스템 유지보수", "기간": "2015.03 ~ 2019.03", "역할": "PL / SM", "발주처": "신한은행", "구분": "개발/운영"},
    {"프로젝트명": "나라사랑카드 발급 시스템 유지보수", "기간": "2011.05 ~ 2015.02", "역할": "PL / SM", "발주처": "신한은행", "구분": "개발/운영"},
    {"프로젝트명": "등록금 웹 시스템 구축 및 유지보수", "기간": "2009.09 ~ 2011.05", "역할": "PM / PL", "발주처": "신한은행", "구분": "PM"},
    {"프로젝트명": "부수 업무 유지보수", "기간": "2007.11 ~ 2009.08", "역할": "개발자", "발주처": "신한은행", "구분": "개발/운영"},
    {"프로젝트명": "제일은행 부수 업무 유지보수", "기간": "2002.03 ~ 2007.11", "역할": "개발자", "발주처": "제일은행", "구분": "개발/운영"},
]

df = pd.DataFrame(projects_data)

# 필터 인터페이스 구성 (가로 배치)
filter_col1, filter_col2, filter_col3 = st.columns([1.5, 1.5, 2])

with filter_col1:
    role_filter = st.selectbox("업무 구분 필터", ["전체 보기", "PM", "PMO/QA", "개발/운영"])

with filter_col2:
    client_filter = st.selectbox("발주처 필터", ["전체 보기", "신한은행", "신한금융지주", "신한DS", "제일은행"])

with filter_col3:
    search_query = st.text_input("프로젝트명 검색 🔍", placeholder="검색할 단어를 입력하세요...")

# 필터링 로직 작동
filtered_df = df.copy()

if role_filter != "전체 보기":
    filtered_df = filtered_df[filtered_df["구분"] == role_filter]

if client_filter != "전체 보기":
    filtered_df = filtered_df[filtered_df["발주처"] == client_filter]

if search_query:
    filtered_df = filtered_df[filtered_df["프로젝트명"].str.contains(search_query, case=False)]

# 결과 테이블 스타일링 및 출력
st.markdown("<br>", unsafe_allow_html=True)
if not filtered_df.empty:
    st.dataframe(
        filtered_df[["기간", "발주처", "프로젝트명", "역할"]],
        use_container_width=True,
        hide_index=True
    )
else:
    st.info("조건에 부합하는 프로젝트 이력이 없습니다. 필터 조건을 확인해 주세요.")

# 5. 나의 신조 및 핵심 전문성 소개
st.markdown("<br><hr>", unsafe_allow_html=True)
intro_col1, intro_col2 = st.columns(2)

with intro_col1:
    st.markdown("""
        <h3 style='color:#0A192F; margin-top:0;'>💡 업무 철학: '안정과 혁신의 균형'</h3>
        <p style='line-height:1.7; color:#475569;'>
            금융 IT는 단 1초의 장애도 허용하지 않는 극도의 <b>'안정성'</b>과 빠르게 변화하는 시장 트렌드에 대응하는 <b>'혁신성'</b>이 공존해야 하는 무대입니다. <br>
            25년간 수많은 메이저 프로젝트를 조율해 오며, 완벽한 품질 관리 프로세스(QA)를 확립하고 개발 초기 단계부터 위험 요소를 선제적으로 예방(TA)하는 것을 가장 최우선으로 삼고 있습니다.
        </p>
    """, unsafe_allow_html=True)

with intro_col2:
    st.markdown("""
        <h3 style='color:#0A192F; margin-top:0;'>🤝 협업 문의 및 제안</h3>
        <p style='line-height:1.7; color:#475569;'>
            대규모 차세대 금융 시스템 구축, 비즈니스 특화 플랫폼 런칭, 또는 신규 프로젝트의 체계적인 관리가 필요한 금융사 및 수행사분들의 제안을 환영합니다. <br>
            풍부한 실무 경험을 바탕으로, 신뢰할 수 있는 든든한 PM/PMO 파트너가 되어 드리겠습니다.
        </p>
    """, unsafe_allow_html=True)

# 6. 푸터 영역 (연락처 및 저작권 정보)
st.markdown("""
    <div style="text-align: center; margin-top: 50px; padding: 20px; background-color: #0A192F; color: #94A3B8; border-radius: 10px;">
        <p style="margin: 0; font-size: 14px;">본 포트폴리오 페이지는 Streamlit 모바일 반응형으로 제작되었습니다.</p>
        <p style="margin: 5px 0 0 0; font-size: 13px; color: #F5A623;">© 2026 Park Seong-Jin. All Rights Reserved.</p>
    </div>
""", unsafe_allow_html=True)
   
