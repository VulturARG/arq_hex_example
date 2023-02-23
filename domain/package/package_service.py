from functools import reduce
from typing import List, Optional

from domain.package.dtos import PackageVolume
from domain.package.entities import PackageEntity
from domain.package.exceptions import DimensionError
from domain.package.repository import PackageRepository


class PackageService:
    def __init__(self, repository: PackageRepository):
        self._repository = repository

    def get_volumes(self) -> List[PackageVolume]:
        """Calculate the volume of a package."""
        packages = self._repository.get_packages()
        calculated_volumes = []
        for package in packages:
            try:
                volume = PackageVolume(
                    id=package.id,
                    volume=self._calculate_volume(package),
                    error=None
                )

            except DimensionError as error:
                volume = PackageVolume(
                    id=package.id,
                    volume=None,
                    error=error.MESSAGE
                )
            calculated_volumes.append(volume)
        return calculated_volumes

    @staticmethod
    def _calculate_volume(package: PackageEntity) -> Optional[int]:
        dimensions = [package.high, package.width, package.length]
        if not all(dimensions):
            raise DimensionError()

        return reduce((lambda x, y: x * y), dimensions)




