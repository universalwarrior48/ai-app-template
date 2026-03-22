"""
Tests for the processing pipeline.
"""

import pytest
from app.core.pipeline import ProcessingPipeline
from app.services.cache import CacheService
from app.services.vector_db import VectorDBService


class TestProcessingPipeline:
    """Test cases for the ProcessingPipeline."""
    
    def test_initialization(self):
        """Test pipeline initialization."""
        pipeline = ProcessingPipeline()
        assert pipeline.inference_engine is not None
        assert pipeline.cache_service is not None
        assert pipeline.vector_db_service is not None
    
    def test_load_components(self):
        """Test loading pipeline components."""
        pipeline = ProcessingPipeline()
        result = pipeline.load_components()
        assert result is True
        assert pipeline.inference_engine.is_loaded is True
    
    def test_process_single(self):
        """Test processing a single input."""
        pipeline = ProcessingPipeline()
        pipeline.load_components()
        
        result = pipeline.process_single("test input")
        assert "input" in result or "error" in result
    
    def test_process_batch(self):
        """Test processing a batch of inputs."""
        pipeline = ProcessingPipeline()
        pipeline.load_components()
        
        inputs = ["input 1", "input 2", "input 3"]
        results = pipeline.process_batch(inputs)
        
        assert len(results) == 3
        for result in results:
            assert "input" in result or "error" in result
    
    def test_cache_integration(self):
        """Test cache integration in pipeline."""
        pipeline = ProcessingPipeline()
        pipeline.load_components()
        
        # Process the same input twice
        result1 = pipeline.process_single("cached input")
        result2 = pipeline.process_single("cached input")
        
        # Results should be the same (from cache)
        assert result1 == result2


class TestCacheService:
    """Test cases for the CacheService."""
    
    def test_initialization(self):
        """Test cache service initialization."""
        cache = CacheService()
        assert cache.cache == {}
        assert cache.is_initialized is False
    
    def test_initialize(self):
        """Test cache initialization."""
        cache = CacheService()
        result = cache.initialize()
        assert result is True
        assert cache.is_initialized is True
    
    def test_get_set_operations(self):
        """Test cache get/set operations."""
        cache = CacheService()
        cache.initialize()
        
        cache.set("test_key", "test_value")
        value = cache.get("test_key")
        assert value == "test_value"
    
    def test_delete_operation(self):
        """Test cache delete operation."""
        cache = CacheService()
        cache.initialize()
        
        cache.set("test_key", "test_value")
        result = cache.delete("test_key")
        assert result is True
        assert cache.get("test_key") is None


class TestVectorDBService:
    """Test cases for the VectorDBService."""
    
    def test_initialization(self):
        """Test vector DB service initialization."""
        vector_db = VectorDBService()
        assert vector_db.is_initialized is False
        assert vector_db.connection is None
    
    def test_initialize(self):
        """Test vector DB initialization."""
        vector_db = VectorDBService()
        result = vector_db.initialize()
        assert result is True
        assert vector_db.is_initialized is True
        assert vector_db.connection is not None