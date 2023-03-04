from aplication.get_volume_use_case import GetVolumesUseCase
from infrastructure.repositories.package.django_package_repository import DjangoPackageRepository


class PackageLogic:
    """Have all use cases from package"""
    @staticmethod
    def get_volumes():
        repository = DjangoPackageRepository()
        return GetVolumesUseCase(repository).execute()
