import falcon,pytest
from falcon import testing 
from python-api-challenge.app import app
from urllib.parse import urlencode
@pytest.fixture
def client():
	return testing.TestClient(app)
def test_put(client):
	body=urlencode({
		'title':"New",
		'status':"Working"
		})
	response=client.simulate_put('/todos/1',body=body)
	assert response.status=falcon.HTTP_200
def test_post(client):
	body=urlencode({
		'title':"second",
		'status':"Sleeping"
		})
	response=client.simulate_post('/todos',body=body)
	assert response.status=falcon.HTTP_200


