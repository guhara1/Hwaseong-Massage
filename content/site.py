# 사이트 공통 설정
BASE_URL = "https://hwaseong-massage.pages.dev"

BRAND = "간다GO"
BRAND_MARK = "GO"
PHONE = "0508-202-4719"
PHONE_DISPLAY = "0508-202-4719"

# 행정구 4곳 (slug, 한글명) — 화성특례시 4개 구청 체제
DISTRICTS = [
    ("manse-gu-chuljangmassage", "만세구"),
    ("hyohaeng-gu-chuljangmassage", "효행구"),
    ("byeongjeom-gu-chuljangmassage", "병점구"),
    ("dongtan-gu-chuljangmassage", "동탄구"),
]

# 대표 읍·면·동 20곳 (district_short, slug, 한글명)
# 번호 행정동(병점1·2동 → 병점동, 동탄1~9동 → 동탄)은 대표 페이지로 통합한다.
AREAS = [
    # 만세구 10
    ("manse", "ujeong-eup-chuljangmassage", "우정읍"),
    ("manse", "hyangnam-eup-chuljangmassage", "향남읍"),
    ("manse", "namyang-eup-chuljangmassage", "남양읍"),
    ("manse", "mado-myeon-chuljangmassage", "마도면"),
    ("manse", "songsan-myeon-chuljangmassage", "송산면"),
    ("manse", "seosin-myeon-chuljangmassage", "서신면"),
    ("manse", "paltan-myeon-chuljangmassage", "팔탄면"),
    ("manse", "jangan-myeon-chuljangmassage", "장안면"),
    ("manse", "yanggam-myeon-chuljangmassage", "양감면"),
    ("manse", "saesol-dong-chuljangmassage", "새솔동"),
    # 효행구 5
    ("hyohaeng", "bongdam-eup-chuljangmassage", "봉담읍"),
    ("hyohaeng", "maesong-myeon-chuljangmassage", "매송면"),
    ("hyohaeng", "bibong-myeon-chuljangmassage", "비봉면"),
    ("hyohaeng", "jeongnam-myeon-chuljangmassage", "정남면"),
    ("hyohaeng", "gibae-dong-chuljangmassage", "기배동"),
    # 병점구 4
    ("byeongjeom", "jinan-dong-chuljangmassage", "진안동"),
    ("byeongjeom", "byeongjeom-dong-chuljangmassage", "병점동"),
    ("byeongjeom", "banwol-dong-chuljangmassage", "반월동"),
    ("byeongjeom", "hwasan-dong-chuljangmassage", "화산동"),
    # 동탄구 1 (동탄1~9동 통합 대표)
    ("dongtan", "dongtan-chuljangmassage", "동탄"),
]

# 역세권 7곳 (slug, 한글명) — 실제 이용 가능한 역 기준 1역 1URL
STATIONS = [
    ("dongtan-station-chuljangmassage", "동탄역"),
    ("byeongjeom-station-chuljangmassage", "병점역"),
    ("eocheon-station-chuljangmassage", "어천역"),
    ("yamok-station-chuljangmassage", "야목역"),
    ("seohwaseong-station-chuljangmassage", "서화성역"),
    ("hwaseong-cityhall-station-chuljangmassage", "화성시청역"),
    ("hyangnam-station-chuljangmassage", "향남역"),
]

# 생활권·주요 거점 10곳 (slug, 한글명)
LIVING = [
    ("dongtan-newtown-chuljangmassage", "동탄신도시"),
    ("dongtan-lakepark-chuljangmassage", "동탄호수공원"),
    ("dongtan-centralpark-chuljangmassage", "동탄센트럴파크"),
    ("byeongjeom-area-chuljangmassage", "병점역 생활권"),
    ("hyangnam-area-chuljangmassage", "향남지구"),
    ("namyang-newtown-chuljangmassage", "남양뉴타운"),
    ("bongdam-area-chuljangmassage", "봉담 생활권"),
    ("saesol-songsan-greencity-chuljangmassage", "새솔동·송산그린시티"),
    ("jebudo-jeongok-port-chuljangmassage", "전곡항·제부도 생활권"),
    ("hwaseong-cityhall-area-chuljangmassage", "화성시청 인근"),
]

# 행정구별 소속 읍·면·동 (메인·행정구 페이지 내부링크용)
DISTRICT_AREAS = {
    "manse-gu-chuljangmassage": [a for a in AREAS if a[0] == "manse"],
    "hyohaeng-gu-chuljangmassage": [a for a in AREAS if a[0] == "hyohaeng"],
    "byeongjeom-gu-chuljangmassage": [a for a in AREAS if a[0] == "byeongjeom"],
    "dongtan-gu-chuljangmassage": [a for a in AREAS if a[0] == "dongtan"],
}


def district_url(slug):
    return f"/hwaseong/{slug}/"


def area_url(district_short, slug):
    return f"/hwaseong/{district_short}/{slug}/"


def station_url(slug):
    return f"/hwaseong/{slug}/"


def living_url(slug):
    return f"/hwaseong/{slug}/"


# 상단 메뉴 — 하위 메뉴에는 키워드를 반복하지 않고 지역명·역명만 표시한다.
NAV = [
    ("홈", "/", []),
    ("출장마사지 안내", "/#service", [
        ("서비스 안내", "/#service"),
        ("전지역 방문 가능", "/#coverage"),
        ("예약 전 확인 기준", "/#check"),
        ("홈타이 이용 가이드", "/hometai-guide/"),
    ]),
    ("행정구별 안내", "/#districts", [
        (name, district_url(slug)) for slug, name in DISTRICTS
    ]),
    ("지역별 안내", "/#areas", [
        (name, area_url(ds, slug)) for ds, slug, name in AREAS
    ]),
    ("역세권별 안내", "/#stations", [
        (name, station_url(slug)) for slug, name in STATIONS
    ]),
    ("생활권별 안내", "/#living", [
        (name, living_url(slug)) for slug, name in LIVING
    ]),
    ("예약안내", "/reservation/", [
        ("예약 방법", "/reservation/#how"),
        ("예약 가능 시간", "/reservation/#hours"),
        ("방문 가능 지역", "/reservation/#place"),
        ("결제·이동비 안내", "/reservation/#payment"),
        ("변경·취소 안내", "/reservation/#change"),
    ]),
    ("이용 전 확인사항", "/precautions/", [
        ("방문 전 준비", "/precautions/#prepare"),
        ("외곽 지역 이동 기준", "/precautions/#outer"),
        ("위생·안전 기준", "/precautions/#hygiene"),
        ("자주 묻는 질문", "/precautions/#faq"),
    ]),
    ("고객센터", "/support/", [
        ("공지사항", "/support/#notice"),
        ("자주 묻는 질문", "/support/#faq"),
        ("1:1 문의", "/support/#contact"),
        ("개인정보처리방침", "/privacy/"),
    ]),
]
