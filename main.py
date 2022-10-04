from adapter.repositories.package.django_package_repository import DjangoPackageRepository
from domain.package.package_service import PackageService


def main():
    repository = DjangoPackageRepository()
    package_service = PackageService(repository)
    packages_volume = package_service.get_volumes()
    for volume in packages_volume:
        print(f"Volumen paquete #{volume.id}: {volume.volume}")


if __name__ == '__main__':
    main()
