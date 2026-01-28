from .regex_pattern import get_regex_pattern
from .spacyk import get_ner
from .io_utils import read_json, write_json #modularization

#mask data
def mask_text(text, targets):
    masked_text = text
    values = {
        t["value"] for t in targets} #get unique val to mask
    for v in sorted(values, key=len, reverse=True): #mask long string first
        masked_text = masked_text.replace(v, "*" * len(v))
    return masked_text

# test main
if __name__ == "__main__":

    input_data = read_json("input.json") #pii data only 
    text = input_data["text"]

    print("Original text:")
    print(text)
    print("-" * 50)

    regex_targets = get_regex_pattern(text)
    ner_targets = get_ner(text) 

    all_targets = regex_targets + ner_targets

    
    masked = mask_text(text, all_targets)
    print("Masked text:")
    print(masked)

    write_json("output/detected.json", all_targets)
    write_json("output/masked.json", {
        "masked_text": masked
    })

    write_json("output/result.json", {
        "original_text": text,
        "masked_text": masked,
        "detected": all_targets
    })

    print("DLP 전처리 완료")


    
