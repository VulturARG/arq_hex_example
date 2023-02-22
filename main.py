from seudo_django.views import PackageViewSet


def some_endpoint():
    endpoint = PackageViewSet()
    packages_volume = endpoint.some_action()
    for volume in packages_volume:
        print(f"Volumen paquete #{volume.id}: {volume.volume}")


if __name__ == '__main__':
    some_endpoint()
