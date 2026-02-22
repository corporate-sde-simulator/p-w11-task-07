import pytest, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from productCatalog import ProductCatalog

class TestOptimization:
    @pytest.fixture
    def catalog(self): return ProductCatalog()

    def test_optimized_exists(self, catalog):
        result = catalog.get_catalog_optimized()
        assert result is not None, "Optimized method not implemented"

    def test_same_output(self, catalog):
        original = catalog.get_catalog()
        optimized = catalog.get_catalog_optimized()
        assert len(original) == len(optimized), "Should return same number of products"
        for o, opt in zip(original, optimized):
            assert o['name'] == opt['name']
            assert o['category'] == opt['category']
