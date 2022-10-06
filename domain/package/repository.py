from abc import ABC, abstractmethod
from typing import List

from domain.package.entities import PackageEntity


class PackageRepository(ABC):
    @abstractmethod
    def get_packages(self) -> List[PackageEntity]:
        """Get packages"""
