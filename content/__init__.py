# 전체 페이지 목록 집계
from . import main, districts, areas, stations, living, info

PAGES = (
    [main.PAGE]
    + districts.PAGES
    + areas.PAGES
    + stations.PAGES
    + living.PAGES
    + info.PAGES
)
