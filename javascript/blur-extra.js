let isBluringPreview = false;

const unblurText = "Unblur Preview Image";
const blurText = "Blur Preview Image";

function onBlurExtraNetworkPreviewChecked() {
    isBluringPreview = !isBluringPreview;

    update();
}

function init() {
    update();
}

function update() {
    for (let elem of document.getElementsByClassName("blur_extra_network_preview_images")) {
        elem.textContent = isBluringPreview ? unblurText: blurText;
    }

    for (let elem of document.querySelectorAll('.extra-network-cards .card .preview')){
        if (isBluringPreview) {
            elem.classList.add('blur-content');
        } else {
            elem.classList.remove('blur-content');
        }
    }
}

init();