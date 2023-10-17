# Pizza Order  API with FastAPI

### Requirements:

- Python 3.6 >
- FastAPI
- SQLAlchemy
- SQLite3
- Docker
- Helm
### Instructions:


Create a database file:
touch pizza_orders.db
Run the migrations:
alembic upgrade head
Start the server:
uvicorn main:app
API endpoints:

```/health (GET)```: Returns a simple health check.

```curl http://localhost:8000/health```

```/order (POST)```: Creates a new pizza order.

```
curl -X POST http://localhost:8000/order -H "Content-Type: application/json" -d '{
    "pizza-type": "margherita",
    "size": "family",
    "amount": 2
}'
```

This is a simple Pizza Order API built with FastAPI and Python. It allows you to place pizza orders and retrieve the health status of the service.

## Getting Started

Follow these steps to set up and run the Pizza Order API on your local machine.

### Prerequisites

- Python 3.9
- Docker (if you want to build and run the API in a container)
- A PostgreSQL or SQLite database (update the configuration accordingly)

### Installation

1. Clone this repository:

```shell
   git clone https://github.com/yourusername/pizza-service.git
   cd pizza-service
```

2. Create a virtual environment (recommended):

```shell
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```
3. Install the required dependencies:

```shell
pip install -r requirements.txt
```
4. Create a database file:
```shell
touch pizza_orders.db
```
5. Run the migrations:
```shell
alembic upgrade head:
```

6. Start the server:
```shell
uvicorn app.main:app --host 0.0.0.0 --port 8000
```
The API will be accessible at http://localhost:8000.

### API endpoints:

- /health (GET): Returns a simple health check.
```shell
curl http://localhost:8000/health
```
- /order (POST): Creates a new pizza order.

```shell
curl -X POST http://localhost:8000/order -H "Content-Type: application/json" -d '{
    "pizza-type": "margarita",
    "size": "family",
    "amount": 2
}'
```

### Configuration
The application configuration can be found in app/main.py. You can update database settings and CORS origins according to your requirements.


### Running Tests
To run the unit tests, use pytest:

``` shell
pytest
```

### Docker Support

To build and run the application in a Docker container, make sure you have Docker installed and then run the following commands:

```shell
docker build -t pizza-order-api:latest .
docker run -p 8000:8000 pizza-order-api:latest
```

### API Endpoints
- Health Check: http://localhost:8000/health (GET)
- Place an Order: http://localhost:8000/order (POST)

### CI/CD
We have set up a GitHub Actions workflow for continuous integration. It runs tests, builds the Docker image, and pushes it to Docker Hub. To set up CI/CD on your repository, create the necessary secrets for Docker Hub access in your GitHub repository settings.

### Helm Deployment (Kubernetes)
If you want to deploy this API to a Kubernetes cluster using Helm, you can find the Helm chart in the helm/ directory. Modify the values.yaml and other resources as needed, and then use Helm to deploy the application.

### License
This project is licensed under the MIT License - see the LICENSE file for details.

### Make order

This server will take orders in the form of json loads:
```jsonc
{
"pizza-type": "<margarita|pugliese|marinara>"
"size": "<personal|family>"
"amount": <int>
}
```

You can **clone and test the app locally** with:
```
docker build -t pizza-service .
docker run -p 8080:8080 pizza-service
```

To deploy with scale please see the **helm chart in the pizza-service folder**. 
Connect to your k8s cluster and run:
```
helm upgrade --install pizza-service ./helm -f values.yaml
```
Alternatively you can set up the repo with ArgoCD application.


