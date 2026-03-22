"""
Gradio UI interface for the AI application.
"""

import gradio as gr


def create_interface():
    """Create and return the Gradio interface."""

    def process_input(user_input):
        """Process user input and return response."""
        # TODO: Implement actual processing logic
        return f"Processed: {user_input}"

    # Create Gradio interface
    interface = gr.Interface(
        fn=process_input,
        inputs=gr.Textbox(label="Input"),
        outputs=gr.Textbox(label="Output"),
        title="AI Application Interface",
        description="A Gradio interface for the AI application",
    )

    return interface


if __name__ == "__main__":
    interface = create_interface()
    interface.launch()
