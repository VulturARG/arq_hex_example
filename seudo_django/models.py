from typing import Dict, List


class Package:
    @staticmethod
    def get_packages() -> List[Dict[str, int]]:
        """Simulo la llamada a la DB"""

        return [
            {
                "id": 1,
                "width": 10,
                "high": 10,
                "length": 10
            },
            {
                "id": 2,
                "width": 20,
                "high": 20,
                "length": 20
            },
            {
                "id": 3,
                "width": 0,
                "high": 20,
                "length": 20
            },
            {
                "id": 4,
                "width": 20,
                "high": None,
                "length": 20
            }
        ]
