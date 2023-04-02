import pytest

import Window.mainW



class TestMainW:
    def test_create_app(self):
        with pytest.raises(Exception):
            Window.mainW.create_app()
