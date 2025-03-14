def confusion_matrix(y_true, y_pred):
    true_positive = 0
    true_negative = 0
    false_positive = 0
    false_negative = 0
    for true, pred in zip(y_true, y_pred):
        if true == 1 and pred == 1:
            true_positive += 1
        elif true == 0 and pred == 0:
            true_negative += 1
        elif true == 1 and pred == 0:
            false_negative += 1
        elif true == 0 and pred == 1:
            false_positive += 1
    return {
        'TP': true_positive,
        'FP': false_positive,
        'TN': true_negative,
        'FN': false_negative
    }

def calculate_precision(y_true, y_pred): # its again a value between 0 and 1, and high chances that it is a float
    cm = confusion_matrix(y_true, y_pred)
    if cm['TP'] + cm['FP'] == 0:
        return 0.0 # float number
    precision = cm['TP'] / (cm['TP'] + cm['FP'])
    return precision

def calculate_recall(y_true, y_pred): # its again a value between 0 and 1, and high chances that it is a float
    cm = confusion_matrix(y_true, y_pred)
    if cm['TP'] + cm['FN'] == 0:
        return 0.0 # float number
    recall = cm['TP']/ (cm['TP'] + cm['FN'])
    return recall

def calculate_f1_precision_recall(y_true, y_pred): # its again a value between 0 and 1, and high chances that it is a float
    precision = calculate_precision(y_true, y_pred)
    recall = calculate_recall(y_true, y_pred)
    if precision + recall == 0:
        return 0.0
    f1_score = 2*(precision * recall)/ (precision + recall)
    return precision, recall, f1_score

def calculate_all_metrices(y_true, y_pred):
    cm = confusion_matrix(y_true, y_pred)
    precision, recall, f1_score = calculate_f1_precision_recall(y_true, y_pred)
    return {
        'precision': precision,
        'recall': recall,
        'f1_score': f1_score,
        'confusion_matrix': cm
    }

def test_metrices():
    y_true = [1,1,1,0,0,0,1]
    y_pred = [0,1,1,0,0,1,0]
    metrices = calculate_all_metrices(y_true, y_pred)
    return metrices

output = test_metrices()
print("hello there")
print(output)
