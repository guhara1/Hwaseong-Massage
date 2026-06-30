# 메인 페이지 — 허브 역할. 모든 키워드를 밀어 넣지 않고 상세 페이지로 연결한다.
from .site import (AREAS, BASE_URL, BRAND, DISTRICTS, LIVING, PHONE,
                   PHONE_DISPLAY, STATIONS, area_url, district_url,
                   living_url, station_url)
from .pricing import PRICING

_DISTRICT_CARDS = "".join(
    f'<li><a href="{district_url(slug)}">{name} 출장마사지</a></li>'
    for slug, name in DISTRICTS
)
_AREA_CARDS = "".join(
    f'<li><a href="{area_url(ds, slug)}">{name} 출장마사지</a></li>'
    for ds, slug, name in AREAS
)
_STATION_CARDS = "".join(
    f'<li><a href="{station_url(slug)}">{name} 출장마사지</a></li>'
    for slug, name in STATIONS
)
_LIVING_CARDS = "".join(
    f'<li><a href="{living_url(slug)}">{name} 출장마사지</a></li>'
    for slug, name in LIVING
)

_JSONLD = f"""<meta name="naver-site-verification" content="018a953d3ebf9dab157bd7aa9d636ac8be401a42" />
<link rel="preload" as="image" href="/assets/hero.webp" type="image/webp" fetchpriority="high">
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "{BRAND}",
  "url": "{BASE_URL}/",
  "telephone": "{PHONE}",
  "image": "{BASE_URL}/assets/og-image.png",
  "logo": "{BASE_URL}/assets/icon-512.png",
  "description": "화성특례시 전지역 방문 출장마사지·홈타이 예약 안내",
  "areaServed": {{
    "@type": "AdministrativeArea",
    "name": "경기도 화성특례시"
  }}
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {{
      "@type": "Question",
      "name": "화성특례시 전지역 방문이 가능한가요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "만세구, 효행구, 병점구, 동탄구 4개 구청 체제를 기준으로 화성특례시 전지역을 안내합니다. 향남·남양·송산·서신 등 서부권은 차량 이동 기준으로 가능 여부를 확인합니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "병점1동·병점2동, 동탄1~9동은 왜 따로 없나요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "병점1·2동은 병점동 대표 페이지로, 동탄1동부터 9동까지는 동탄 대표 페이지로 통합해 중복 페이지 위험을 줄였습니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "서부·외곽 지역은 추가 이동비가 있나요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "서신면, 송산면, 장안면, 양감면처럼 이동 거리가 먼 서부·외곽 지역은 추가 이동비가 발생할 수 있으며, 예약 시 총비용으로 먼저 안내합니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "동탄역·병점역 주변도 예약할 수 있나요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "동탄역, 병점역, 향남역, 화성시청역, 어천역 등 역세권 인근은 역세권 안내 페이지에서 주변 생활권과 함께 확인할 수 있습니다."
      }}
    }}
  ]
}}
</script>
"""

_HERO = f"""<section class="hero">
  <div class="hero-inner hero-grid">
    <div class="hero-text">
      <p class="hero-badge">Premium Visiting Spa · 화성특례시 전지역</p>
      <h1>화성 출장마사지·화성특례시 홈타이<br>지역별 예약 안내</h1>
      <p class="hero-lead">샵까지 갈 필요 없이, 계신 곳에서 받는 방문 관리.<br>만세구·효행구·병점구·동탄구 어디든 전화 한 통이면 예약이 끝납니다.</p>
      <div class="hero-actions">
        <a class="hero-btn primary" href="tel:{PHONE}">📞 {PHONE_DISPLAY}</a>
        <a class="hero-btn" href="#areas">지역별 안내 보기</a>
      </div>
      <ul class="hero-stats">
        <li><strong>4개</strong><span>행정구</span></li>
        <li><strong>20곳</strong><span>대표 읍·면·동</span></li>
        <li><strong>7개</strong><span>역세권</span></li>
        <li><strong>24시간</strong><span>예약 상담</span></li>
      </ul>
    </div>
    <div class="hero-media">
      <picture>
        <source srcset="/assets/hero.webp" type="image/webp">
        <img src="/assets/hero.jpg" alt="화성 출장마사지·화성특례시 홈타이 방문 관리 안내" width="1200" height="675" fetchpriority="high" decoding="async">
      </picture>
    </div>
  </div>
</section>
"""

_BODY = f"""
<section id="service">
<h2>화성특례시에서 출장마사지를 찾는 이유</h2>
<p>화성 출장마사지를 찾는 분들은 대부분 지금 계신 곳에서 가까운 방문 가능 지역을 먼저 확인합니다. 화성특례시는 면적이 넓고 생활권 차이가 큰 도시입니다. 동탄은 동탄역, 동탄신도시, 동탄호수공원, 동탄센트럴파크 중심의 신도시 생활권이고, 병점은 병점역과 진안동, 화산동, 반월동을 함께 보는 동부 생활권입니다. 향남, 남양, 우정, 장안, 팔탄, 송산, 서신 쪽은 화성 서부와 남부 차량 이동 생활권이고, 봉담과 기배동은 수원·오산·화성 사이를 연결하는 생활권입니다. {BRAND}는 예약 확인부터 방문 관리까지 정해진 절차에 따라 진행하며, 이 페이지는 화성 전체 구조를 설명하는 허브 역할을 합니다. 더 자세한 내용은 행정구·대표 읍면동 페이지와 역세권 페이지에서 확인하실 수 있습니다.</p>
<p>화성 홈타이는 자택, 숙소, 사무실 인근에서 예약 가능 여부를 먼저 확인한 뒤 이용하는 방문형 관리 서비스입니다. 화성은 도시 면적이 넓기 때문에 동탄역 주변과 서신면, 송산면, 우정읍, 장안면의 이동 기준이 완전히 다릅니다. 본문과 제목에는 화성 출장마사지, 화성시 출장마사지, 화성특례시 출장마사지, 화성 홈타이 표현을 자연스럽게 함께 사용합니다.</p>
</section>

<section id="districts">
<h2>만세구·효행구·병점구·동탄구 생활권 차이</h2>
<p>화성 홈타이 사이트에서 가장 중요한 부분은 현재 행정구 구조를 반영하는 것입니다. 화성특례시는 4개 구청 체제로 나뉘었기 때문에 메인페이지 아래에 만세구, 효행구, 병점구, 동탄구 행정구 페이지를 먼저 두었습니다. 만세구는 향남·남양·송산·서신 등 서부·남부 생활권, 효행구는 봉담·매송·정남 등 수원 인접 생활권, 병점구는 병점역·진안동·반월동 동부 생활권, 동탄구는 동탄역·동탄신도시 신도시 생활권을 담당합니다. 본인이 있는 위치를 빠르게 찾을 수 있도록 행정구를 먼저 선택해 주세요.</p>
<ul class="card-grid">
{_DISTRICT_CARDS}
</ul>
</section>

<section id="areas">
<h2>대표 읍면동별 방문 가능 지역 안내</h2>
<p>지역별 안내는 화성특례시 대표 읍·면·동 20곳을 기준으로 구성됩니다. 각 페이지에서는 해당 생활권의 특징, 가까운 역, 방문 전 확인사항, 예약 가능 시간, 추가 이동비 여부를 지역마다 고유한 내용으로 설명합니다. 병점1동과 병점2동은 병점동 대표 페이지로, 동탄1동부터 9동까지는 동탄 대표 페이지로 통합해 지역명만 바뀐 반복 페이지를 만들지 않았습니다. 거주하시거나 머무시는 지역을 선택해 주세요.</p>
<ul class="card-grid">
{_AREA_CARDS}
</ul>
<p>만세구는 향남·남양의 중심 생활권, 서신·송산의 해안 생활권, 팔탄·장안·양감의 차량 이동 기준을 다르게 안내합니다. 효행구는 봉담지구·수원대 인근, 어천역·야목역 접근성, 정남면 오산 인접 생활권을 다룹니다. 병점구는 병점역 중심 상권과 진안동·화산동·반월동을, 동탄구는 동탄역과 동탄신도시 생활권을 대표 페이지로 안내합니다.</p>
</section>

<section id="stations">
<h2>동탄역·병점역·향남역·화성시청역 역세권 안내</h2>
<p>역세권별 안내는 화성특례시 안에서 실제 이용 가능한 역을 기준으로 구성합니다. 동탄역은 SRT·GTX-A 환승 성격이 있어도 1개 URL로, 병점역은 1호선과 향후 GTX-C 연장 이슈를 나누지 않고 1개 URL로 만듭니다. 각 역 페이지에서는 주변 읍·면·동, 이동 동선, 이용 시간대, 예약 전 확인사항을 역마다 다르게 설명하며, 노선·방향별 중복 페이지는 만들지 않습니다. 서동탄역은 행정구역상 오산시 역이므로 단독 페이지를 만들지 않습니다.</p>
<ul class="card-grid">
{_STATION_CARDS}
</ul>
<p>동탄역은 동탄신도시 생활권과, 병점역은 병점동·진안동 중심 생활권과, 향남역·화성시청역·서화성역은 서해선 화성 서부권 생활권과, 어천역·야목역은 수인분당선 매송·비봉 인접 생활권과 연결됩니다.</p>
</section>

<section id="living">
<h2>동탄·병점·향남·봉담·남양 생활권 구성 방식</h2>
<p>생활권·주요 거점 페이지는 실제 검색 의도가 있는 거점을 기준으로만 구성합니다. 동탄은 동탄신도시·동탄호수공원·동탄센트럴파크 생활권으로, 병점은 병점역 생활권으로, 향남은 향남지구로, 남양은 남양뉴타운으로, 봉담은 봉담 생활권으로 나눕니다. 서부 해안권은 새솔동·송산그린시티와 전곡항·제부도 생활권으로 안내합니다.</p>
<ul class="card-grid">
{_LIVING_CARDS}
</ul>
</section>

<section id="coverage">
<h2>화성특례시 전지역 방문 가능 안내</h2>
<p>화성특례시는 만세구, 효행구, 병점구, 동탄구 4개 구청 관할로 나뉩니다. 동탄권은 신도시 생활권이라 도로 접근이 수월하고, 병점권은 1호선과 상권 중심으로 이동이 빠른 편입니다. 반면 우정·장안·서신·송산·양감 같은 서부·남부 지역은 차량 이동 시간이 길어질 수 있어 예약 가능 시간과 추가 이동비를 명확히 안내합니다. 어느 지역이든 화성특례시 안이라면 방문이 가능하니, 우선 거주하시는 위치를 알려주시면 가장 정확하게 도와드릴 수 있습니다.</p>
</section>

<section id="check">
<h2>화성 홈타이 예약 전 확인사항</h2>
<p>예약 전에는 방문 가능 지역, 관리 가능 시간, 추가 이동비, 결제 방식, 취소 기준, 서비스 범위를 먼저 확인해야 합니다. 화성은 같은 시 안에서도 동탄역 주변과 서신면·송산면·장안면의 이동 시간이 크게 다를 수 있습니다. 특히 서부권과 남부권은 차량 이동 기준 안내가 중요하므로, 자세한 준비 방법은 <a href="/precautions/">이용 전 확인사항</a>에서, 예약 절차와 결제·이동비 안내는 <a href="/reservation/">예약안내</a>에서 확인해 주세요. 홈타이가 처음이라면 <a href="/hometai-guide/">홈타이 이용 가이드</a>를 함께 보시면 도움이 됩니다.</p>
</section>

<section id="guide">
<h2>화성 출장마사지 사이트 이용 가이드</h2>
<p>메인페이지는 화성특례시 전체 안내를 담당하고, 행정구 페이지는 만세구·효행구·병점구·동탄구 생활권을 설명합니다. 대표 읍면동 페이지는 향남읍, 남양읍, 봉담읍, 병점동, 동탄 같은 지역 검색을 담당하고, 역세권 페이지는 동탄역, 병점역, 향남역, 화성시청역, 어천역, 야목역 검색 의도를 담당합니다. 어느 페이지를 보셔도 예약 절차와 비용 기준은 동일하며, 최종 안내는 언제나 정확한 주소를 기준으로 이루어집니다. 과장된 표현이나 허위 후기, 불법·선정적인 안내는 사용하지 않으며, 이용 가능 지역과 예약 절차, 취소 기준, 개인정보 처리 기준을 분명하게 보여드리는 것을 원칙으로 합니다.</p>
</section>

<section id="faq">
<h2>자주 묻는 질문</h2>
<div class="faq-item">
<h3>화성특례시 전지역 방문이 가능한가요?</h3>
<p>만세구·효행구·병점구·동탄구 4개 구청 체제를 기준으로 화성특례시 전지역을 안내합니다. 서부·남부 면 지역은 차량 이동 기준으로 가능 여부를 확인합니다.</p>
</div>
<div class="faq-item">
<h3>병점1동·동탄1동처럼 번호 동은 왜 페이지가 없나요?</h3>
<p>병점1·2동은 병점동, 동탄1동부터 9동까지는 동탄 대표 페이지에서 통합 안내합니다. 같은 생활권을 나눠 반복 설명하지 않기 위해서입니다.</p>
</div>
<div class="faq-item">
<h3>서부·외곽 지역은 추가 이동비가 붙나요?</h3>
<p>서신면, 송산면, 장안면, 양감면처럼 이동 거리가 먼 지역은 추가 이동비가 발생할 수 있습니다. 예약 시 총비용으로 먼저 안내해 드립니다.</p>
</div>
<div class="faq-item">
<h3>동탄역·병점역 같은 역세권도 예약되나요?</h3>
<p>동탄역, 병점역, 향남역, 화성시청역, 어천역, 야목역, 서화성역 인근은 역세권 안내 페이지에서 주변 생활권과 함께 확인하실 수 있습니다.</p>
</div>
</section>

{PRICING}
<section id="contact" class="cta">
<h2>예약문의</h2>
<p>화성 방문 관리 예약과 상담은 전화로 가장 빠르게 진행됩니다. 위치와 희망 시간을 알려주시면 가능 여부를 바로 확인해 드립니다.</p>
<a class="cta-phone" href="tel:{PHONE}">{PHONE_DISPLAY}</a>
</section>
"""

PAGE = {
    "path": "",
    "title": "화성 출장마사지｜화성특례시 홈타이 지역별 예약 안내",
    "desc": "화성 출장마사지·홈타이 예약 전 4개 구청, 역세권, 이용 기준을 정리했습니다.",
    "h1": "화성 출장마사지 · 화성특례시 홈타이 지역별 예약 안내",
    "body": _BODY,
    "extra_head": _JSONLD,
    "breadcrumb": [],
    "hero": _HERO,
}
