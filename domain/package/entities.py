from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class PackageEntity:
    id: int
    width: Optional[int]
    high: Optional[int]
    length: Optional[int]
