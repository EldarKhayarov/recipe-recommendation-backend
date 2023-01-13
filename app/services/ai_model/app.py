import io
from collections import Counter

from PIL import Image
from torchvision.transforms import ToPILImage
import torch
import numpy as np


AI_APP_PATH = "app/services/ai_model/"

model = torch.hub.load(
    AI_APP_PATH + "yolov5/",
    "custom",
    source="local",
    path=AI_APP_PATH + "weights/weights.pt",
    force_reload=True,
)


def detect(image: bytes) -> tuple[dict[str, int], Image]:
    image = Image.open(io.BytesIO(image))
    results = model(np.asarray(image))

    out_img = np.asarray(results.render())
    out_img = out_img.reshape(tuple(out_img.shape[1:]))
    return dict(Counter(results.pandas().xyxy[0]["name"])), np.squeeze(
        ToPILImage()(out_img)
    )
