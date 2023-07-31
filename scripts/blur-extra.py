import modules.scripts as scripts
import gradio as gr
import os

from modules import images, script_callbacks
from modules.processing import process_images, Processed
from modules.processing import Processed
from modules.shared import opts, cmd_opts, state


class BlurExtraNetwork(scripts.Script):
    # Extension title in menu UI
    def title(self):
        return "Blur extra network previews."

    def show(self, is_img2img):
        return scripts.AlwaysVisible

    isBlur = False
    elemIdsToAddTo = [
        "txt2img_textual_inversion_cards_html",
        "txt2img_hypernetworks_cards_html",
        "txt2img_checkpoints_cards_html",
        "txt2img_lora_cards_html",
        "img2img_textual_inversion_cards_html",
        "img2img_hypernetworks_cards_html",
        "img2img_checkpoints_cards_html",
        "img2img_lora_cards_html",
    ]

    
    def before_component(self, component, **kwargs):
        if kwargs.get("elem_id") in self.elemIdsToAddTo:
            button = gr.Button("Blur Preview Image", elem_classes=["blur_extra_network_preview_images"])
            button.click(None, [], None, _js="() => onBlurExtraNetworkPreviewChecked()")

    # Setup menu ui detail
    def ui(self, is_img2img):
        return []
