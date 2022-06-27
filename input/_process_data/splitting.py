import random

from raw_utils import set_seed


def save_data(data, fpath):
    with open(fpath, 'w') as out:
        for instance in data:
            for token in instance:
                out.write(token)
            out.write("\n")


if __name__ == "__main__":

    set_seed(26092020)

    fpath = "/content/drive/MyDrive/bert_bilstm_crf_named_entity_recognition/CRF-NER/input/_process_data/BIO/final-data.txt"

    file = open(fpath)
    lines = file.readlines()
    file.close()

    data = []
    instance = []

    for l in lines:
        if l[:-1] == "":  # if it's empty
            data.append(instance)
            instance = []
        else:
            instance.append(l)

    random.shuffle(data)

    train_size = int(0.6 * len(data))

    train_fpath = "/content/drive/MyDrive/bert_bilstm_crf_named_entity_recognition/CRF-NER/input/raw_data/train.txt"
    test_fpath = "/content/drive/MyDrive/bert_bilstm_crf_named_entity_recognition/CRF-NER/input/raw_data/test.txt"
    dev_fpath = "/content/drive/MyDrive/bert_bilstm_crf_named_entity_recognition/CRF-NER/input/raw_data/dev.txt"

    save_data(data[:train_size], train_fpath)
    save_data(data[train_size:], test_fpath)
    save_data(data[train_size + 24:], dev_fpath)
