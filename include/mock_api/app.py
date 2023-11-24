from flask import Flask, jsonify, request
import random
from datetime import datetime

app = Flask(__name__)


def get_random_feedback():
    feedback_options = [
        "I love this product, been using it for all my machine learning pipelines! Especially the UI is great.",
        "I don't like the product, been using it for machine learning pipelines and struggling with the UI.",
        "Fantastic experience with the customer service team!",
        "Not very satisfied with the performance of the product.",
        "This product has transformed the way I work, absolutely fantastic UX!",
        "I found the product difficult to use and not very intuitive.",
        "Excellent value for money, highly recommend it.",
        "The product did not meet my expectations, ugly UI.",
        "A game changer in the industry, very impressed with the user experience!",
        "Quite disappointed with the overall quality of the user interface.",
    ]
    return random.choice(feedback_options)


def get_random_rating():
    return random.randint(1, 5)


def get_random_customer_id():
    return random.randint(1000, 2000)


def get_random_date():
    return datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")


def get_customer_feedback(num_reviews):
    reviews = []
    for _ in range(num_reviews):
        review = {
            "customer_feedback": get_random_feedback(),
            "customer_rating": get_random_rating(),
            "customer_id": get_random_customer_id(),
            "timestamp": get_random_date(),
            "customer_location": "Switzerland",
            "product_type": "cloud service A",
            "ab_test_group": "A",
        }
        reviews.append(review)
    return reviews


@app.route("/api/data")
def get_data():
    num_reviews = request.args.get("num_reviews", default=5, type=int)

    num_reviews = max(0, min(num_reviews, 500))

    mock_data = get_customer_feedback(num_reviews)
    return jsonify(mock_data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
