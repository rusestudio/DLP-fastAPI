from kiwipiepy import Kiwi
import spacy

nlp = spacy.load("ko_core_news_lg") #todo later add custom spacy model
kiwi = Kiwi()

def kiwip(text: str) -> str:
    tokens = kiwi.tokenize(text)
    return " ".join(t.form for t in tokens)

#SENSITIVE_KEYWORD = ["API"] 
#add more label and ner label
#add sensitive keyword matching if match scan more deeply

#extract entity target
def get_ner(text):
    clean_text = kiwip(text)
    doc = nlp(clean_text)
    results = []

    for ent in doc.ents:
        if ent.label_ in {"PS", "OG","LC", "QT", "TI", "DT", "MA", "AD", "AP", "CV", "SO", "AN", "PRODUCT", "EVENT", "LAW", "FAC"} :  #add more labels if needed
            results.append({
                "type": "NER",
                "label": ent.label_,
                "value": ent.text
            })

    return results

#get only string for kiwip masking
#def extract_ner_texts(ner_targets):
    #return [ent["value"] for ent in ner_targets]
