import gradio as gr
from src.summarizer import summarize_pdf_gradio
import os

def main():
    input_pdf_path = gr.File(file_count="single", file_types=["pdf"])
    output_summary = gr.outputs.Textbox(label="Summary")

    iface = gr.Interface(
        fn=summarize_pdf_gradio,
        inputs=[input_pdf_path],
        examples=[[[os.path.join(os.getcwd(),"data/s43588-022-00234-z.pdf")]]],
        outputs=[output_summary],
        title="PDF Summarizer",
        description="Enter the path to a PDF file and get its summary.",
    )

    iface.launch(share=True)


if __name__ == "__main__":
    main()