"""
Main application entry point.
Supports both FastAPI server and Hugging Face Space deployment.
"""

import os
from fastapi import FastAPI
from app.api.routes import router
from app.core.config import settings
from app.utils.port_finder import find_free_port

# Create FastAPI app instance
app = FastAPI(
    title=settings.app_name, description="AI Application API", version="1.0.0"
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
    # Check if running as Hugging Face Space
    if os.environ.get("SPACE_ID") or os.environ.get("SPACE_HOST"):
        # Launch as Hugging Face Space with Gradio interface
        try:
            from app.ui.interface import create_interface

            print(f"🚀 Starting Hugging Face Space: {settings.app_name}")
            print(f"Space ID: {os.environ.get('SPACE_ID', 'Not set')}")
            print(f"Space Host: {os.environ.get('SPACE_HOST', 'Not set')}")
            print(f"Space Port: {os.environ.get('SPACE_PORT', 'Not set')}")

            # Find available port for Gradio interface
            # gradio_port = int(os.environ.get("SPACE_PORT", 7860))
            
            interface = create_interface()
            interface.launch(
                server_name="0.0.0.0",
                server_port=find_free_port(7860, 100),
                share=False,  # Don't create public share links
                debug=settings.debug,
            )
        except ImportError:
            print("❌ Gradio interface not available, falling back to FastAPI")
            _start_fastapi_server()
        except Exception as e:
            print(f"❌ Error starting Space interface: {e}")
            _start_fastapi_server()
    else:
        # Launch as FastAPI server
        _start_fastapi_server()


def _start_fastapi_server():
    """Start the FastAPI server."""
    print("AI Application starting...")
    print(f"App Name: {settings.app_name}")
    print(f"Debug Mode: {settings.debug}")
    print(f"API Server: http://{settings.api_host}:{settings.api_port}")

    # TODO: Initialize application components
    # - Load configuration
    # - Initialize models
    # - Start API server
    # - Start UI interface

    print("AI Application ready!")

    # Start the server
    import uvicorn

    uvicorn.run(
        "app.main:app",
        host=settings.api_host,
        port=settings.api_port,
        reload=settings.debug,
    )


if __name__ == "__main__":
    main()
