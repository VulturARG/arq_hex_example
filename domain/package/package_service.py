from functools import reduce
from typing import List, Optional

from domain.package.dataclasses import PackageVolume
from domain.package.entities import PackageEntity
from domain.package.repository import PackageRepository


class PackageService:
    def __init__(self, repository: PackageRepository):
        self._repository = repository

    def get_volumes(self) -> List[PackageVolume]:
        """Calculate the volume of a package."""
        packages = self._repository.get_packages()
        return [
            PackageVolume(
                id=package.id,
                volume=self._calculate_volume(package)
            )
            for package in packages
        ]

    @staticmethod
    def _calculate_volume(package: PackageEntity) -> Optional[int]:
        dimensions = [package.high, package.width, package.length]
        if not all(dimensions):
            return None

        return reduce((lambda x, y: x * y), dimensions)




