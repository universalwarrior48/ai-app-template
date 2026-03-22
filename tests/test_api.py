"""
Tests for the API endpoints.
"""

import pytest
from fastapi.testclient import TestClient
from ..app.api.routes import router
from ..app.api.routes import InputRequest, OutputResponse


class TestAPI:
    """Test cases for API endpoints."""
    
    @pytest.fixture
    def client(self):
        """Create a test client."""
        from fastapi import FastAPI
        app = FastAPI()
        app.include_router(router)
        return TestClient(app)
    
    def test_health_check(self, client):
        """Test the health check endpoint."""
        response = client.get("/health")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "healthy"
        assert "AI Application is running" in data["message"]
    
    def test_root_endpoint(self, client):
        """Test the root endpoint."""
        response = client.get("/")
        assert response.status_code == 200
        data = response.json()
        assert "Welcome to the AI Application API" in data["message"]
    
    def test_process_text(self, client):
        """Test the text processing endpoint."""
        test_input = {"text": "Hello, world!"}
        response = client.post("/process", json=test_input)
        assert response.status_code == 200
        data = response.json()
        assert "result" in data
        assert "Processed: Hello, world!" in data["result"]
    
    def test_process_text_validation(self, client):
        """Test input validation for text processing."""
        # Test with missing text field
        response = client.post("/process", json={})
        assert response.status_code == 422  # Validation error
        
        # Test with empty text
        response = client.post("/process", json={"text": ""})
        assert response.status_code == 200  # Should still process empty text