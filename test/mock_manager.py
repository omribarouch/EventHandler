from unittest.mock import patch, MagicMock


class MockManager:
    _patches: list[patch]

    def __init__(self):
        self._patches = []

    def mock(self, mock_path: str) -> MagicMock:
        patch_instance: patch = patch(mock_path)
        self._patches.append(patch_instance)

        return patch_instance.start()

    def deconstruct_patches(self):
        for patch_instance in self._patches:
            patch_instance.stop()
