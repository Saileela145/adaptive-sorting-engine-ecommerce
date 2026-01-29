
from sample_data import get_sample_products
from data_analyzer import DataAnalyzer
from decision_engine import DecisionEngine

if __name__ == "__main__":
    products = get_sample_products()

    analyzer = DataAnalyzer()
    decision_engine = DecisionEngine()

    analysis = analyzer.analyze(products, "price")

    print("Data Analysis Result:")
    for k, v in analysis.items():
        print(f"{k}: {v}")

    strategy = decision_engine.decide(analysis)

    print("\nSelected Sorting Strategy:")
    print(strategy)
