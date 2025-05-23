"""
mT5 (XLSum fine-tuned) дээр үндэслэсэн богино дүгнэлт
CPU-д шууд ажиллана (GPU илэрвэл автоматаар хэрэглэнэ).
"""
from pathlib import Path
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

MODEL_NAME = "csebuetnlp/mT5_multilingual_XLSum"   # summarization-д fine-tuned
_MAX_OUT   = 120

class Summarizer:
    def __init__(self, model_name: str = MODEL_NAME):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model     = AutoModelForSeq2SeqLM.from_pretrained(model_name)
        self.pipe      = pipeline(
            "summarization",
            model=self.model,
            tokenizer=self.tokenizer,
            device=-1     # -1=CPU, 0=GPU
        )

    def __call__(self, text: str, max_new_tokens: int = _MAX_OUT) -> str:
        text = text.strip().replace("\n", " ")
        if not text:
            raise ValueError("Оролтын текст хоосон байна.")
        result = self.pipe(text, max_length=max_new_tokens, truncation=True)
        return result[0]["summary_text"]

    # optional: файл руу хадгалах
    @staticmethod
    def save(summary: str, out_path: Path):
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(summary, encoding="utf-8")
