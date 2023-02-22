from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class PackageVolume:
    id: int
    volume: Optional[int]
