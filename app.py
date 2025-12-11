import streamlit as st

# --- 커스텀 CSS 삽입 (UI 전체 축소) ---
st.markdown("""
<style>

/* 전체 글씨 크기 줄이기 */
html, body, [class*="css"] {
    font-size: 13px !important;
}

/* 입력 박스 높이 줄이기 */
input, select, textarea {
    padding: 4px 6px !important;
    font-size: 13px !important;
    height: 32px !important;
}

/* number_input 의 +, - 버튼 크기 줄이기 */
.stNumberInput button {
    padding: 0px 6px !important;
    font-size: 13px !important;
}

/* selectbox 크기 */
.stSelectbox div[data-baseweb="select"] > div {
    min-height: 32px !important;
    font-size: 13px !important;
}

/* 헤더 크기 축소 */
h1 {
    font-size: 26px !important;
}
h2 {
    font-size: 20px !important;
}
h3 {
    font-size: 18px !important;
}

</style>
""", unsafe_allow_html=True)


st.set_page_config(page_title="경매 수익 계산기", layout="wide")

st.title("🏠 경매 수익 계산기 (UI Only)")

st.markdown("계산식 없이 **UI 구조만 먼저 구현한 버전**입니다.")

# -----------------------------
# 1. 기본 정보 입력
# -----------------------------
# --- A. 물건 기본 정보 그룹화 (Expander) ---
with st.expander("A. 입찰 정보", expanded=True):
    col1, col2 = st.columns(2)
    
    with col1:
        감정가 = st.number_input("감정가", value=298000000, step=1000000)
        낙찰가 = st.number_input("낙찰가", value=170000000, step=1000000)
        매도가 = st.number_input("예상 매도가", value=210000000, step=1000000)
    
    with col2:
        입찰최저가 = st.number_input("입찰최저가", value=152576000, step=1000000)
        유찰횟수 = st.number_input("유찰횟수", value=3, min_value=1, max_value=10)
        시세 = st.number_input("현재 시세", value=221000000, step=1000000)

# --- B. 매도 및 수익률 조건 그룹화 (Expander) ---
with st.expander("B. 물건 정보", expanded=True):
    col3, col4 = st.columns(2)
    
    with col3:
        주택면적 = st.number_input("주택면적", value=29.13, step=0.1)
        수리정도 = st.selectbox("수리정도", options=['청소만', "+도배/장판", "+옥실/주방", "샤시포함 올수리"])
        욕실개수 = st.number_input("욕실개수", value=1, min_value=1, max_value=3)
        
    with col4:
        매매유형 = st.selectbox("매매유형", options=["주택", "오피스텔/상가", "토지"])
        점유자유무 = st.selectbox("점유자유/무", options=["N", "Y"])
        층수 = st.number_input("층수", value=5, min_value=0, max_value=50)
        
# --- C. 대출 및 세금 조건 그룹화 (Expander) ---
with st.expander("C. 대출 및 세금", expanded=True):
    col5, col6 = st.columns(2)
    
    with col5:
        대출종류 = st.selectbox("대출종류", options=["개인 주담대", "서민실수요자대출", "매사자근저당", "매사자신탁", "전자상거래", "비주택담보대출", "무대출"])
        대출금리 = st.number_input("대출금리 (%)", value=4.50, min_value=3.5, max_value=20.0, step=0.01)
        대출상환기간 = st.number_input("대출상환기간(월)", value=6, min_value=1, max_value=360, step=1)
        중도상환수수료율 = st.selectbox("중도상환수수료율", options=["3개월후면제", "0.48%", "0.50%", "0.7%", "면제"])
        방공제 = st.selectbox("방공제", options=["N", "Y"])
    
    with col6:
        매도방식 = st.selectbox("매도방식", options=["매매사업자", "일반과세", "개인 - 1년내 매도", "개인 - 2년내 매도", "1세대 1주택 비과세"])
        주택수_취득시 = st.selectbox("주택수(취득시)", options=["1", "2", "3","4+"])
        지역 = st.selectbox("지역", options=["서울", "수도권", "광역시", "기타지역"])
        규제지역 = st.selectbox("규제지역(조정/투과/토허)", options=["N", "Y"])
        생애최초구입 = st.selectbox("생애최초구입", options=["N", "Y"])
        셀프등기 = st.selectbox("셀프등기", options=["N", "Y"])
        


        
    
st.markdown("---")


# -----------------------------
# 2. 대출 정보
# -----------------------------
st.header("2. 대출 정보")

col4, col5, col6 = st.columns(3)

with col4:
    loan_type = st.selectbox("대출종류", ["가계대출", "사업자대출", "담보대출"])
    loan_rate = st.number_input("대출금리 (%)", min_value=0.0, step=0.01)
    loan_period = st.number_input("대출상환기간(월)", min_value=1, step=1)

with col5:
    early_fee = st.selectbox("중도상환수수료율", ["3개월후면제", "6개월후면제", "1년후면제"])
    room_deduction = st.selectbox("방공제", ["Y", "N"])
    house_type = st.selectbox("매매유형", ["주택", "오피스텔", "상가"])

with col6:
    regulation_area = st.selectbox("규제지역 여부", ["N", "조정대상지역", "투기과열지구"])
    house_count = st.number_input("주택수(취득시)", min_value=0, step=1)
    first_time = st.selectbox("생애최초구입", ["Y", "N"])

# -----------------------------
# 3. 지역 및 등기 정보
# -----------------------------
st.header("3. 지역 및 등기 정보")

col7, col8 = st.columns(2)

with col7:
    region = st.selectbox("지역", ["서울", "경기", "인천", "기타"])
    self_register = st.selectbox("셀프등기 여부", ["Y", "N"])

with col8:
    st.text_input("채권할인율 확인 링크", "https://dbbond.co.kr/sub/_sale.php")

# -----------------------------
# 4. 비용 입력
# -----------------------------
st.header("4. 비용 입력")

col9, col10, col11 = st.columns(3)

with col9:
    repair_cost = st.number_input("수리비(도배/욕실 등)", min_value=0, step=10000)
    unpaid_fees = st.number_input("미납관리비", min_value=0, step=10000)

with col10:
    moving_cost = st.number_input("이사비/강제집행비", min_value=0, step=10000)
    legal_fee = st.number_input("법무사비", min_value=0, step=10000)

with col11:
    stamp_tax = st.number_input("수입인지", min_value=0, step=1000)
    admin_fee = st.number_input("등기 행정 수수료", min_value=0, step=1000)

# -----------------------------
# 5. 계산 버튼
# -----------------------------
st.header("5. 계산 실행")

if st.button("계산하기"):
    st.warning("⚠️ 현재는 UI만 구현된 상태입니다. 계산 로직은 추후 추가됩니다.")
    st.info("입력값은 정상적으로 수집되었습니다. 계산 모듈 연결 후 결과가 표시됩니다.")

# -----------------------------
# 6. 결과 출력 자리
# -----------------------------
st.header("6. 계산 결과 (Placeholder)")

st.success("여기에 계산 결과가 표시됩니다. (아직 계산식 없음)")

