"""
Main application entry point.
"""

from fastapi import FastAPI
from app.api.routes import router
from app.core.config import settings

# Create FastAPI app instance
app = FastAPI(
    title=settings.app_name,
    description="AI Application API",
    version="1.0.0"
)

# Include API routes
app.include_router(router)

@app.get("/")
async def root():
    """Root endpoint."""
    return {"message": f"Welcome to {settings.app_name} API"}

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "message": f"{settings.app_name} is running"}

def main():
    """Application entry point."""
    print(f"AI Application starting...")
    print(f"App Name: {settings.app_name}")
    print(f"Debug Mode: {settings.debug}")
    print(f"API Server: http://{settings.api_host}:{settings.api_port}")
    
    # TODO: Initialize application components
    # - Load configuration
    # - Initialize models
    # - Start API server
    # - Start UI interface
    
    print("AI Application ready!")

if __name__ == "__main__":
    main()
