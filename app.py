import streamlit as st

st.set_page_config(page_title="경매 수익 계산기", layout="wide")

st.title("🏠 경매 수익 계산기 (UI Only)")

st.markdown("계산식 없이 **UI 구조만 먼저 구현한 버전**입니다.")

# -----------------------------
# 1. 기본 정보 입력
# -----------------------------
st.header("1. 기본 정보 입력")

col1, col2, col3 = st.columns(3)

with col1:
    appraisal_price = st.number_input("감정가", min_value=0, step=10000)
    min_bid_price = st.number_input("입찰최저가", min_value=0, step=10000)
    winning_bid = st.number_input("낙찰가", min_value=0, step=10000)
    standard_price = st.number_input("시가표준액", min_value=0, step=10000)

with col2:
    sale_price = st.number_input("매도가", min_value=0, step=10000)
    market_price = st.number_input("시세", min_value=0, step=10000)
    bond_discount_rate = st.number_input("채권할인율 (%)", min_value=0.0, step=0.01)
    auction_fail_count = st.number_input("유찰횟수", min_value=0, step=1)

with col3:
    repair_level = st.selectbox("수리정도", ["도배만", "욕실/주방 추가", "전체 리모델링"])
    bathroom_count = st.number_input("욕실 개수", min_value=0, step=1)
    occupant = st.selectbox("점유자 유/무", ["Y", "N"])
    sale_type = st.selectbox("매도방식", ["매매사업자", "일반과세"])

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

