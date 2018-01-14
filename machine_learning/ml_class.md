

## Confusion Matrix
| test negative | test positive |
| ---  | --- |
| TN | FP |
| FN | TP |

Horizontally:  
*TNR:* specificity  
*TPR:* recall  
*FPR = 1 - TNR*


Vertically:  
*precision:* TP / (FP + TP)  

## ROC
*ROC ~ plt.plot(FPR, TPR)*  
*ROC ~ plt.plot(1-specificity, recall)*  
where, both *FPR* and *TPR* are calculated horizontally.       

Once again there is a tradeoff: the higher the recall (TPR), the more false positives (FPR) the classifier produces. The dotted line represents the ROC curve of a purely random classifier; a good classifier stays as far away from that line as possible (toward the top-left corner). One way to compare classifiers is to measure the area under the curve (AUC). A perfect classifier will have a ROC AUC equal to 1, whereas a purely random classifier will have a ROC AUC equal to 0.5.
 
