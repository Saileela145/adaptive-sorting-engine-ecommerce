

class SortingEngine:
    def sort(self, products, key, strategy):
        """
        Sort products based on the selected strategy.
        key: attribute to sort by (price, rating, date_added)
        strategy: selected sorting strategy
        """

        if strategy == "simple_sort":
            return self._simple_sort(products, key)

        if strategy == "adaptive_sort":
            return self._adaptive_sort(products, key)

        if strategy == "duplicate_aware_sort":
            return self._duplicate_aware_sort(products, key)

        if strategy == "efficient_sort":
            return self._efficient_sort(products, key)

        # Fallback
        return self._efficient_sort(products, key)

    def _simple_sort(self, products, key):
        # Simple sorting for small datasets
        return sorted(products, key=lambda p: getattr(p, key))

    def _adaptive_sort(self, products, key):
        # Adaptive sorting assumes partial order
        return sorted(products, key=lambda p: getattr(p, key))

    def _duplicate_aware_sort(self, products, key):
        # Duplicate-aware sorting (stable sort)
        return sorted(products, key=lambda p: getattr(p, key))

    def _efficient_sort(self, products, key):
        # Efficient general-purpose sorting
        return sorted(products, key=lambda p: getattr(p, key))
