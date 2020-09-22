import json
import os
import requests
import re
import lawrouge

input_path = "lawrouge/test.json"
prefix_path=""

def get_path(path):
    """Create the path if it does not exist.

    Args:
        path: path to be used

    Returns:
        Existed path
    """
    if not os.path.exists(path):
        os.makedirs(path)
    return path

if __name__ == "__main__":
    get_path(os.path.join("prediction"))
    pred_list = []
    with open(input_path.replace("../",""),'r', encoding='utf8') as fr:
        for line in fr:
            item = json.loads(line)
            pred_list.append(os.path.join("prediction", item['id'] + ".txt"))
            with open(os.path.join(prefix_path, "prediction", item['id']+".txt"),'w', encoding='utf8') as fw:
                #use your own summary API for summarization.
                fw.write(item['summary'])
    print(pred_list)

    get_path(os.path.join("gold"))
    gold_list = []
    with open(input_path.replace("../",""),'r', encoding='utf8') as fr:
        for line in fr:
            item = json.loads(line)
            gold_list.append(os.path.join(prefix_path, "gold", item['id'] + ".txt"))
            with open(os.path.join(prefix_path, "gold", item['id']+".txt"),'w', encoding='utf8') as fw:
                fw.write(item['summary'])
    print(gold_list)

    files_rouge = lawrouge.FoldersRouge()
    scores = files_rouge.get_scores(pred_list, gold_list, avg=True)
    print(scores)
    weighted_f1 = 0.2*scores['rouge-1']['f'] + 0.4*scores['rouge-2']['f']+ 0.4*scores['rouge-l']['f']
    print('weighted F1-score:', weighted_f1)


