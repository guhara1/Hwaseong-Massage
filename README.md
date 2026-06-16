# 간다GO — 화성 출장마사지·홈타이 지역 SEO 사이트

경기도 화성특례시에서 방문형 마사지(출장마사지)·홈타이를 찾는 사용자가
본인 위치에 맞는 지역 정보를 쉽게 확인할 수 있도록 만든 정적 지역 SEO 사이트입니다.
화성특례시 4개 구청(만세구·효행구·병점구·동탄구) 체제를 그대로 반영합니다.

- **상호:** 간다GO
- **예약전화:** 0508-202-4719
- **핵심 키워드:** 출장마사지 / **보조:** 홈타이
- **지역 키워드:** 화성 출장마사지, 화성시 출장마사지, 화성특례시 출장마사지, 화성 홈타이

## 구조 (총 47페이지)

```
메인 1
행정구 4        (만세구·효행구·병점구·동탄구)
대표 읍·면·동 20  (만세구 10 · 효행구 5 · 병점구 4 · 동탄구 1)
역세권 7        (동탄역·병점역·어천역·야목역·서화성역·화성시청역·향남역)
생활권·거점 10   (동탄신도시·동탄호수공원·동탄센트럴파크·병점역 생활권·향남지구·
                남양뉴타운·봉담 생활권·새솔동/송산그린시티·전곡항/제부도·화성시청 인근)
안내 페이지 5    (예약안내·이용 전 확인사항·홈타이 이용 가이드·개인정보처리방침·고객센터)
```

번호 행정동은 개별 페이지를 만들지 않고 대표 페이지로 통합합니다.
병점1·2동 → 병점동, 동탄1~9동 → 동탄 대표 페이지.

## URL 규칙

| 구분 | 경로 |
|------|------|
| 메인 | `/` |
| 행정구 | `/hwaseong/<gu>-gu-chuljangmassage/` |
| 읍·면·동 | `/hwaseong/<gu-short>/<slug>-chuljangmassage/` |
| 역세권 | `/hwaseong/<station>-station-chuljangmassage/` |
| 생활권·거점 | `/hwaseong/<slug>-chuljangmassage/` |

> 메인페이지는 배포 도메인 루트(`/`)에 위치합니다. 워드프레스 슬러그
> `/hwaseong-chuljangmassage/`로 운영하려면 해당 경로로 리다이렉트하세요.

## 빌드

```bash
python3 build.py
```

`content/` 패키지의 페이지 정의를 읽어 각 경로에 `index.html`을 생성하고
`sitemap.xml`, `robots.txt`, `.nojekyll`을 갱신합니다.

- 본문 텍스트 2,000자 미만 페이지는 자동으로 `noindex` 처리됩니다.
- 모든 페이지에 `WebPage`·`BreadcrumbList` 구조화 데이터가 자동 삽입되고,
  메인에는 `Organization`·`FAQPage`가 추가됩니다.
- 실제 오프라인 매장 주소가 없으므로 `LocalBusiness` 스키마는 사용하지 않습니다.

## 배포 전 설정

- `content/site.py`의 `BASE_URL`을 실제 도메인으로 변경한 뒤 `python3 build.py` 재실행.

## 디렉터리

```
build.py                    빌드 스크립트
content/
  site.py                   공통 설정(브랜드·지역·역·생활권·메뉴)
  pricing.py                코스별 요금 블록
  main.py                   메인(허브) 페이지
  districts.py              행정구 4페이지
  areas.py                  읍·면·동 집계
  areas_manse.py            만세구 10페이지
  areas_hyohaeng.py         효행구 5페이지
  areas_byeongjeom_dongtan.py  병점구 4 + 동탄 1페이지
  stations.py               역세권 7페이지
  living.py                 생활권·거점 10페이지
  info.py                   안내 5페이지
assets/                     style.css, nav.js, 파비콘/OG 이미지
```
