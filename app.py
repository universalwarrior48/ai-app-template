"""
Hugging Face Space entry point for AI Application Template.
This file serves as the main entry point for the Space deployment.
"""

import os
from app.ui.interface import create_interface

def main():
    """Main entry point for Hugging Face Space."""
    # Get Space configuration
    port = int(os.environ.get("SPACE_PORT", 7860))
    host = os.environ.get("SPACE_HOST", "0.0.0.0")
    
    # Create and launch the interface
    interface = create_interface()
    
    # Launch the Space
    interface.launch(
        server_name=host,
        server_port=port,
        share=False,  # Don't create public share links
        debug=True    # Enable debug mode for template
    )

if __name__ == "__main__":
    main()