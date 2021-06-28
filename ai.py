from question_generation import pipelines

nlp = pipelines.pipeline("multitask-qa-qg", model="valhalla/t5-small-qa-qg-hl")

def ask(question , context):
    return nlp({"question" : question , "context":context})
