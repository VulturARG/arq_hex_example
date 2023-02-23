from unittest.mock import Mock

from domain.package.dtos import PackageVolume
from domain.package.entities import PackageEntity
from domain.package.package_service import PackageService
from domain.package.repository import PackageRepository


def test_parameter_is_none():
    repository = Mock(spec=PackageRepository)
    repository.get_packages.return_value = [
        PackageEntity(
            id=1,
            width=2,
            high=3,
            length=None
        )
    ]
    expected = [
        PackageVolume(
            id=1,
            volume=None,
            error="Error in dimensión parameter"
        )
    ]

    package_service = PackageService(repository)
    actual = package_service.get_volumes()
    assert actual == expected


def test_parameter_is_zero():
    repository = Mock(spec=PackageRepository)
    repository.get_packages.return_value = [
        PackageEntity(
            id=1,
            width=2,
            high=3,
            length=0
        )
    ]
    expected = [
        PackageVolume(
            id=1,
            volume=None,
            error="Error in dimensión parameter"
        )
    ]

    package_service = PackageService(repository)
    actual = package_service.get_volumes()
    assert actual == expected


def test_parameter_are_good():
    repository = Mock(spec=PackageRepository)
    repository.get_packages.return_value = [
        PackageEntity(
            id=1,
            width=2,
            high=3,
            length=4
        )
    ]
    expected = [
        PackageVolume(
            id=1,
            volume=24,
            error=None
        )
    ]

    package_service = PackageService(repository)
    actual = package_service.get_volumes()
    assert actual == expected
