from typing import Iterator
from cog import BasePredictor, Input

class Predictor(BasePredictor):
    def setup(self):
        print("✨ 模型初始化完成（未載入真 SDXL）")

    def predict(self, prompt: str = Input(description="生成圖像的提示詞")) -> str:
        print(f"📥 接收到 prompt: {prompt}")
        return f"你輸入的 prompt 是: {prompt}"
