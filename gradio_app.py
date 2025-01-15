# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/02_gradio_app.ipynb.

# %% auto 0
__all__ = ['create_app', 'test_create_app']

# %% ../nbs/02_gradio_app.ipynb 2
import gradio as gr
from itertools import groupby
from operator import attrgetter
from app_starter_gui.core import Button, load_buttons
from app_starter_gui.css import generate_css

# %% ../nbs/02_gradio_app.ipynb 4
def create_app(yaml_file='buttons.yaml', css_generator=generate_css):
    """Create a Gradio dashboard for the button interface
    
    Args:
        yaml_file: Path to YAML file containing button data (default: 'buttons.yaml')
        css_generator: Function to generate CSS (default: generate_css)
    Returns:
        gr.Blocks: Gradio interface
    """
    buttons = load_buttons(yaml_file)
    css = generate_css(buttons)

    buttons_sorted = sorted(buttons, key=attrgetter('app_type'))
    buttons_grouped = {k: list(g) for k, g in groupby(buttons_sorted, key=attrgetter('app_type'))}

    with gr.Blocks(css=css) as blocks:
        with gr.Row():
            # Create a column for each app type
            for app_type, type_buttons in buttons_grouped.items():
                with gr.Column():
                    gr.Markdown(f"### {app_type}")
                    for i, button in enumerate(type_buttons, 1):
                        btn = gr.Button(
                            value=button.label,
                            elem_id=f"btn_{app_type}_{i}",
                            scale=1,
                        )
                        btn.click(
                            fn=None,
                            inputs=None,
                            outputs=None,
                            js=f"() => {{ window.open('{button.link_url}', '_blank'); }}"
                        )
    return blocks

if __name__ == '__main__':
    demo = create_app()
    demo.launch(share=True)