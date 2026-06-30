#!/usr/bin/env python3
"""IndexNow 즉시 색인 통보 — 빙(Bing)·네이버(Naver)·얀덱스 등에 변경 URL을 알린다.

IndexNow는 한 곳에 제출하면 참여 검색엔진(Bing, Naver, Yandex, Seznam 등)에
공유된다. 구글은 IndexNow에 참여하지 않으므로 google_indexing.py 를 사용한다.

사용법:
  # sitemap.xml 의 전체 URL 제출(기본)
  python3 tools/indexnow.py

  # 특정 URL만 제출(글 새로 올릴 때마다)
  python3 tools/indexnow.py https://hwaseong-massage.netlify.app/hwaseong/dongtan/dongtan-chuljangmassage/

키 파일(<KEY>.txt)이 사이트 루트에 실제로 게시(배포)된 뒤에 호출해야 한다.
표준 라이브러리만 사용하므로 별도 설치가 필요 없다.
"""
import json
import os
import re
import sys
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from content.site import BASE_URL, INDEXNOW_KEY, SITE_HOST  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENDPOINT = "https://api.indexnow.org/indexnow"
BASE = BASE_URL.rstrip("/")


def sitemap_urls():
    path = os.path.join(ROOT, "sitemap.xml")
    if not os.path.exists(path):
        sys.exit("sitemap.xml 이 없습니다. 먼저 python3 build.py 를 실행하세요.")
    with open(path, encoding="utf-8") as f:
        return re.findall(r"<loc>(.*?)</loc>", f.read())


def submit(urls):
    urls = [u for u in urls if u.startswith(BASE)]
    if not urls:
        sys.exit("제출할 URL이 없습니다. (도메인이 BASE_URL과 일치하는지 확인)")
    payload = {
        "host": SITE_HOST,
        "key": INDEXNOW_KEY,
        "keyLocation": f"{BASE}/{INDEXNOW_KEY}.txt",
        "urlList": urls,
    }
    req = urllib.request.Request(
        ENDPOINT,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            code = resp.getcode()
    except urllib.error.HTTPError as e:
        code = e.code
    # 200 OK, 202 Accepted 가 정상. 403=키 파일 미게시, 422=URL/호스트 불일치
    note = {
        200: "정상 접수",
        202: "정상 접수(검증 대기)",
        400: "잘못된 요청",
        403: "키 파일이 루트에 게시되지 않음(.txt 배포 확인)",
        422: "URL/호스트 불일치",
        429: "요청 과다 — 잠시 후 재시도",
    }.get(code, "")
    print(f"IndexNow: {len(urls)}개 URL 제출 → HTTP {code} {note}")
    for u in urls:
        print(f"  - {u}")
    return code in (200, 202)


if __name__ == "__main__":
    targets = sys.argv[1:] or sitemap_urls()
    ok = submit(targets)
    sys.exit(0 if ok else 1)
