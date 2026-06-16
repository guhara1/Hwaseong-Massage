# 대표 읍·면·동 20개 페이지 집계.
# 번호 행정동(병점1·2동 → 병점동, 동탄1~9동 → 동탄)은 대표 페이지로 통합한다.
from .areas_manse import PAGES as _MANSE
from .areas_hyohaeng import PAGES as _HYOHAENG
from .areas_byeongjeom_dongtan import PAGES as _BD

PAGES = _MANSE + _HYOHAENG + _BD
