#!/usr/bin/env python3
"""Google Indexing API — 변경 URL을 구글에 직접 통보한다.

구글은 IndexNow에 참여하지 않으므로 즉시 색인 통보는 이 API로 한다.
공식 지원 대상은 JobPosting·BroadcastEvent 구조화 데이터지만, 실무에서는
일반 페이지 색인 가속에도 널리 사용된다. 보조 수단이며, 기본 색인은 항상
구글 서치콘솔 + sitemap.xml 제출이 우선이다.

사전 준비(1회):
  1) Google Cloud 프로젝트 생성 → "Indexing API" 사용 설정
  2) 서비스 계정 생성 → JSON 키 발급 → service_account.json 으로 저장
  3) 서치콘솔(search.google.com/search-console)에서 해당 사이트 속성에
     서비스 계정 이메일(...@....iam.gserviceaccount.com)을 '소유자'로 추가
  4) 의존성 설치: pip install google-auth requests

사용법:
  export GOOGLE_APPLICATION_CREDENTIALS=service_account.json
  python3 tools/google_indexing.py                 # sitemap 전체
  python3 tools/google_indexing.py <URL> [URL ...]  # 특정 URL
  python3 tools/google_indexing.py --delete <URL>   # 삭제 통보(URL_DELETED)
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from content.site import BASE_URL  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = BASE_URL.rstrip("/")
SCOPES = ["https://www.googleapis.com/auth/indexing"]
ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"


def sitemap_urls():
    path = os.path.join(ROOT, "sitemap.xml")
    if not os.path.exists(path):
        sys.exit("sitemap.xml 이 없습니다. 먼저 python3 build.py 를 실행하세요.")
    with open(path, encoding="utf-8") as f:
        return re.findall(r"<loc>(.*?)</loc>", f.read())


def get_session():
    try:
        from google.oauth2 import service_account
        from google.auth.transport.requests import AuthorizedSession
    except ImportError:
        sys.exit("pip install google-auth requests 를 먼저 실행하세요.")
    cred_path = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS", "service_account.json")
    if not os.path.exists(cred_path):
        sys.exit(f"서비스 계정 키 파일을 찾을 수 없습니다: {cred_path}\n"
                 "GOOGLE_APPLICATION_CREDENTIALS 환경변수로 경로를 지정하세요.")
    creds = service_account.Credentials.from_service_account_file(cred_path, scopes=SCOPES)
    return AuthorizedSession(creds)


def main(argv):
    notif = "URL_UPDATED"
    if argv and argv[0] == "--delete":
        notif = "URL_DELETED"
        argv = argv[1:]
    targets = [u for u in (argv or sitemap_urls()) if u.startswith(BASE)]
    if not targets:
        sys.exit("제출할 URL이 없습니다.")
    session = get_session()
    ok = 0
    for url in targets:
        r = session.post(ENDPOINT, json={"url": url, "type": notif}, timeout=30)
        status = "OK" if r.status_code == 200 else f"ERR {r.status_code}"
        if r.status_code == 200:
            ok += 1
        else:
            status += f" {r.text[:160]}"
        print(f"  [{status}] {url}")
    print(f"\nGoogle Indexing API: {ok}/{len(targets)} 통보 성공 ({notif})")
    return 0 if ok == len(targets) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
