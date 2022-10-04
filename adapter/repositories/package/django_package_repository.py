from domain.package.entities import PackageEntity
from domain.package.repository import PackageRepository
from seudo_django.package_model import Package


class DjangoPackageRepository(PackageRepository):
    def get_packages(self):
        """Get packages"""

        packages = Package.get_packages()
        return [
            PackageEntity(
                id=package["id"],
                width=package["width"],
                length=package["length"],
                high=package["high"],
            )
            for package in packages
        ]
