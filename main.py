from fastapi import FastAPI,Body
import json
from dlp.regex_pattern import get_regex_pattern
from dlp.spacyk import get_ner
from dlp.dlp import mask_text

app = FastAPI()

#get only plain masked result
@app.post("/process/")
async def process_text(text: str = Body(..., media_type="text/plain")):
    regex_targets = get_regex_pattern(text)
    ner_targets = get_ner(text)

    #ner_text = extract_ner_texts(ner_targets)
    #kiwi_ner = kiwip(ner_text) #tokenize ner targets using kiwi to only mask exact words

    all_targets = regex_targets + ner_targets
    masked_data = mask_text(text, all_targets)
    #want to return data for (text,maksed_text, all_targets) in json format
    return {
        "원본": text,
        "처리된_데이터": masked_data,
        "추출된_타깃": all_targets
    }

@app.get("/health/")
async def health_check():
    return {"status": "healthy"}
