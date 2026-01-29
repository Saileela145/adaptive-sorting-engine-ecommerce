
from sample_data import get_sample_products
from data_analyzer import DataAnalyzer
from decision_engine import DecisionEngine
from sorting_engine import SortingEngine

if __name__ == "__main__":
    products = get_sample_products()

    sort_key = "price"  # change to rating or date_added

    analyzer = DataAnalyzer()
    decision_engine = DecisionEngine()
    sorting_engine = SortingEngine()

    analysis = analyzer.analyze(products, sort_key)
    strategy = decision_engine.decide(analysis)
    sorted_products = sorting_engine.sort(products, sort_key, strategy)

    print("Sorting Key:", sort_key)
    print("Analysis:", analysis)
    print("Chosen Strategy:", strategy)
    print("\nSorted Products:\n")

    for product in sorted_products:
        print(product)
