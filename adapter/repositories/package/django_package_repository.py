from typing import List

from domain.package.entities import PackageEntity
from domain.package.repository import PackageRepository
from seudo_django.package_model import Package


class DjangoPackageRepository(PackageRepository):
    def get_packages(self) -> List[PackageEntity]:
        """Get packages"""

        packages = Package.get_packages()  # Datos obtenidos de la DB
        return [
            PackageEntity(
                id=package["id"],
                width=package["width"],
                length=package["length"],
                high=package["high"],
            )
            for package in packages
        ]
