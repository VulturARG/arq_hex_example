from domain.package.package_service import PackageService
from domain.package.repository import PackageRepository


class GetVolumesUseCase:
    def __init__(self, repository: PackageRepository):
        self._repository = repository

    def execute(self):
        package_service = PackageService(self._repository)
        return package_service.get_volumes()
