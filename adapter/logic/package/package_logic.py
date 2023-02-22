from adapter.repositories.package.django_package_repository import DjangoPackageRepository
from domain.package.package_service import PackageService


class PackageLogic:
    """Have all use cases from package"""
    @staticmethod
    def get_volume():
        repository = DjangoPackageRepository()
        package_service = PackageService(repository)
        return package_service.get_volumes()
