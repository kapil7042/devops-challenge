from flask import Flask, jsonify
import os
import psycopg2
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)


def get_db_connection():
    try:
        connection = psycopg2.connect(
            host=os.getenv("DB_HOST", "postgres-service"),
            database=os.getenv("DB_NAME", "postgres"),
            user=os.getenv("DB_USER", "postgres"),
            password=os.getenv("DB_PASSWORD"),
            connect_timeout=3
        )
        return connection
    except Exception as error:
        logger.error(f"Database connection failed: {error}")
        return None


@app.route("/")
def home():
    return jsonify(
        message="Hello DevOps!",
        status="running",
        version="2.0.0"
    )


@app.route("/health")
def health():
    return jsonify(status="healthy"), 200


@app.route("/ready")
def ready():
    connection = get_db_connection()

    if connection:
        connection.close()
        return jsonify(status="ready"), 200

    return jsonify(status="not ready"), 503


@app.route("/db-test")
def db_test():
    connection = get_db_connection()

    if connection:
        connection.close()
        return jsonify(database="connected"), 200

    return jsonify(database="disconnected"), 503


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)