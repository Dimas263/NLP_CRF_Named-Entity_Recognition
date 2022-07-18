# NLP
# Named Entity Recognition (NER) - CRF

## <img src="https://img.icons8.com/external-smashingstocks-flat-smashing-stocks/64/000000/external-manager-hotel-smashingstocks-flat-smashing-stocks-2.png"/> **`Slamet Riyanto S.Kom., M.M.S.I.`**

## <img src="https://img.icons8.com/external-fauzidea-flat-fauzidea/64/undefined/external-man-avatar-avatar-fauzidea-flat-fauzidea.png"/> **`Dimas Dwi Putra`**

## Architecture
<img src="NER-CRF%20Architecture.png" width="2046">

## Dataset
| Sentence #  | Word        | POS | Tag       |
| ----------- | ----------- | --- | --------- |
| Sentence: 0 | studies     | NNS | O         |
| Sentence: 0 | on          | IN  | O         |
| Sentence: 0 | magnesium   | NN  | O         |
| Sentence: 0 | s           | NN  | O         |
| Sentence: 0 | mechanism   | NN  | O         |
| Sentence: 0 | of          | IN  | O         |
| Sentence: 0 | action      | NN  | O         |
| Sentence: 0 | in          | IN  | O         |
| Sentence: 0 | digitalis   | NN  | B-plant   |
| Sentence: 0 | induced     | VBD | O         |
| Sentence: 0 | arrhythmias | NNS | B-disease |
...

## Eval
| Entities     | precision | recall | f1-score | support | time    |
| ------------ | --------- | ------ | -------- | ------- | ------- |
| Disease      | 0,776     | 0,648  | 0,706    | 219     | 0.00.13 |
| Plant        | 0,841     | 0,851  | 0,846    | 168     |         |
| micro avg    | 0,807     | 0,736  | 0,770    | 387     |         |
| macro avg    | 0,809     | 0,750  | 0,776    | 387     |         |
| weighted avg | 0,804     | 0,736  | 0,767    | 387     |         |
| F-1 Scores   |           |        | 77%      |         |         |


# Predict
```yaml
Top positive:
4.842843 plant    word.lower():garlic
4.709949 plant    word.lower():onion
4.073929 disease  word.lower():toxicity
4.054944 plant    word.lower():coriander
4.027413 disease  word.lower():fracture
3.990277 plant    word.lower():pomegranate
3.653315 plant    word.lower():cannabis
3.653315 plant    word[-3:]:bis
3.576833 disease  word.lower():malignancies
3.425418 plant    word.lower():wheat
3.279002 plant    word.lower():soybean
3.225197 plant    word.lower():pecan
3.170079 disease  word.lower():hypertension
3.148002 disease  word.lower():tumors
3.122960 plant    word[-3:]:lis
3.075669 plant    +1:word.lower():oil
3.048397 disease  word.lower():diabetic
3.013212 disease  +1:word.lower():cavity
2.998055 disease  word.lower():allergy
2.995630 plant    word[-3:]:rry
2.992128 disease  word.lower():cataract
2.981014 disease  word.lower():bleeding
2.979117 disease  word.lower():cancer
2.978557 disease  word.lower():tuberculosis
2.965201 O        word.lower():apoptosis
2.927497 disease  word[-2:]:dm
2.881254 disease  word.lower():cancers
2.833302 O        word.lower():virus
2.810619 disease  word.lower():diabetes
2.798214 plant    +1:word.lower():edulis

Top negative:
-3.359532 O        word.lower():onion
-3.066623 O        -1:word.lower():amounts
-2.745636 O        word.lower():hypertension
-2.708038 O        word.lower():soybean
-2.644523 O        word.lower():wheat
-2.623507 O        word.lower():diabetic
-2.338203 O        word.lower():tumors
-2.152337 O        -1:word.lower():neoplasia
-2.130136 O        word.lower():onions
-2.130066 O        word.lower():wheezing
-2.118473 O        word[-2:]:za
-2.094815 O        +1:word.lower():specimens
-2.090329 O        word[-2:]:ra
-2.073248 O        -1:word.lower():therapy
-2.055149 O        word[-2:]:ia
-2.020333 O        word[-2:]:go
-2.011253 O        word.lower():garlic
-1.958288 O        +1:word.lower():korean
-1.946295 O        word.lower():cancers
-1.893636 disease  -1:word.lower():tumors
-1.880753 O        word.lower():soreness
-1.869144 O        word[-2:]:na
-1.867619 O        word.lower():cytotoxicity
-1.836304 O        word[-3:]:oes
-1.826616 disease  -1:word.lower():diseases
-1.777637 O        word[-2:]:oa
-1.766677 O        word[-2:]:ae
-1.765827 O        word.lower():intestinal
-1.751468 O        word.lower():occlusion
-1.743117 O        word[-3:]:nut
```
