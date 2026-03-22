"""
Tests for the inference module.
"""

import pytest
from app.core.inference import InferenceEngine


class TestInferenceEngine:
    """Test cases for the InferenceEngine."""

    def test_initialization(self):
        """Test inference engine initialization."""
        engine = InferenceEngine()
        assert engine.model is None
        assert engine.is_loaded is False

    def test_load_model(self):
        """Test model loading."""
        engine = InferenceEngine()
        result = engine.load_model()
        assert result is True
        assert engine.is_loaded is True
        assert engine.model is not None

    def test_predict_without_loading(self):
        """Test prediction without loading model."""
        engine = InferenceEngine()
        with pytest.raises(ValueError, match="Model not loaded"):
            engine.predict("test input")

    def test_predict_with_loaded_model(self):
        """Test prediction with loaded model."""
        engine = InferenceEngine()
        engine.load_model()

        result = engine.predict("test input")
        assert "input" in result
        assert "prediction" in result
        assert "confidence" in result
        assert result["input"] == "test input"

    def test_batch_predict(self):
        """Test batch prediction."""
        engine = InferenceEngine()
        engine.load_model()

        inputs = ["input 1", "input 2", "input 3"]
        results = engine.batch_predict(inputs)

        assert len(results) == 3
        for i, result in enumerate(results):
            assert "input" in result
            assert "prediction" in result
            assert result["input"] == inputs[i]
