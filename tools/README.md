# 색인(인덱싱) 가속 도구

화성 출장마사지 사이트를 네이버·구글·빙에 가장 빠르게 색인시키기 위한 도구 모음입니다.

## 생성되는 파일 (`python3 build.py` 시 자동)

| 파일 | 용도 |
|------|------|
| `sitemap.xml` | 표준 사이트맵 (lastmod·changefreq·priority 포함). 네이버·구글·빙에 제출 |
| `rss.xml` | RSS 2.0 피드. 구글·빙은 RSS도 사이트맵으로 인식해 새 글을 빠르게 발견 |
| `robots.txt` | 크롤 허용 + `sitemap.xml`·`rss.xml` 위치 명시 |
| `900b3cd64cd27b2ba78482905d003368.txt` | IndexNow 키 파일 (루트 게시 필수) |

## 1. IndexNow — 빙·네이버 즉시 통보 (의존성 없음)

네이버와 빙은 IndexNow 파트너입니다. 한 번 제출하면 두 곳에 즉시 공유됩니다.

```bash
# 사이트가 배포되어 키 파일(.txt)이 실제 URL로 열린 뒤 실행
python3 tools/indexnow.py                       # sitemap 전체 제출
python3 tools/indexnow.py <새로 올린 URL>         # 글 올릴 때마다 즉시 통보
```

> HTTP 200/202 = 정상. 403이 뜨면 키 파일이 아직 배포되지 않은 것이니,
> `https://hwaseong-massage.pages.dev/900b3cd64cd27b2ba78482905d003368.txt`
> 가 브라우저에서 열리는지 먼저 확인하세요.

## 2. Google Indexing API — 구글 직접 통보 (구글은 IndexNow 미참여)

```bash
pip install google-auth requests
export GOOGLE_APPLICATION_CREDENTIALS=service_account.json
python3 tools/google_indexing.py                # sitemap 전체
python3 tools/google_indexing.py <URL>          # 특정 URL
```

사전 준비(1회): Google Cloud에서 **Indexing API** 사용 설정 → 서비스 계정 JSON 키 발급
→ 구글 **서치콘솔** 사이트 속성에 서비스 계정 이메일을 **소유자**로 추가.
자세한 단계는 `google_indexing.py` 상단 주석 참고.

## 3. 검색엔진 콘솔 등록 (가장 중요 — 1회)

| 검색엔진 | 할 일 |
|----------|-------|
| **네이버** | [서치어드바이저](https://searchadvisor.naver.com) → 사이트 등록 → 소유확인(메인페이지 메타태그 이미 삽입됨) → `sitemap.xml`·`rss.xml` 제출 |
| **구글** | [서치콘솔](https://search.google.com/search-console) → 속성 추가 → `sitemap.xml` 제출 |
| **빙** | [Bing Webmaster](https://www.bing.com/webmasters) → 사이트 추가(구글 서치콘솔에서 가져오기 가능) → `sitemap.xml` 제출. IndexNow 키도 여기서 확인 가능 |

## 참고: sitemap ping 자동화는 더 이상 권장하지 않음

구글은 2023년 6월 `/ping?sitemap=` 엔드포인트를 **폐기**했고 빙도 마찬가지입니다.
따라서 핑(ping) 대신 위의 방식을 사용합니다.

- **빙·네이버 즉시 색인** → IndexNow (`tools/indexnow.py`)
- **구글 즉시 통보** → Indexing API (`tools/google_indexing.py`)
- **공통 기본** → 서치콘솔/서치어드바이저에 `sitemap.xml` 1회 제출 (이후 lastmod로 자동 재크롤)

## 글 새로 올릴 때 루틴

```bash
python3 build.py                                  # 사이트맵·RSS 갱신
git add -A && git commit -m "..." && git push     # 배포(Cloudflare Pages)
python3 tools/indexnow.py <새 URL>                 # 빙·네이버 즉시 통보
python3 tools/google_indexing.py <새 URL>          # 구글 즉시 통보(선택)
```
