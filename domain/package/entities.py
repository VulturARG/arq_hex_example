from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True, eq=True)
class PackageEntity:
    id: int
    width: Optional[int]
    high: Optional[int]
    length: Optional[int]
