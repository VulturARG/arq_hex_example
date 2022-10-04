from abc import ABC, abstractmethod


class PackageRepository(ABC):
    @abstractmethod
    def get_packages(self):
        """Get packages"""
