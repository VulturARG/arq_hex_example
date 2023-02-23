from adapter.logic.package.package_logic import PackageLogic


class PackageViewSet:
    """Is good to be a viewsets.ViewSet."""

    def some_action(self):
        return PackageLogic.get_volumes()
