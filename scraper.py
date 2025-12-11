import requests
from bs4 import BeautifulSoup
import json
import datetime

# -----------------------------
# 사건번호 기반 검색 스크래핑
# -----------------------------
def scrape_case(year, sno):
    url = "https://winsauction.com/auction/search.html"
    params = {
        "syear": year,
        "sno": sno,
        "ams": "1",
        "page": "1"
    }

    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        res = requests.get(url, params=params, headers=headers, timeout=10)
        res.raise_for_status()
    except Exception as e:
        return {"status": "error", "msg": f"요청 실패: {e}"}

    soup = BeautifulSoup(res.text, "html.parser")

    # 결과 예: product_id 추출
    link = soup.select_one("a[href*='product_id']")
    if not link:
        return {"status": "error", "msg": "해당 사건번호의 물건을 찾을 수 없습니다."}

    detail_url = link["href"]  # /auction/view.html?product_id=xxxx

    scraped_data = {
        "year": year,
        "sno": sno,
        "detail_page": f"https://winsauction.com{detail_url}",
        "scraped_at": str(datetime.datetime.now())
    }

    # -----------------------------
    # 결과 파일 저장
    # -----------------------------
    with open("scraped_data.json", "w", encoding="utf-8") as f:
        json.dump(scraped_data, f, ensure_ascii=False, indent=4)

    return {"status": "ok", "data": scraped_data}
