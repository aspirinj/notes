

## Confusion Matrix
| predicted negative | predicted positive |
| ---  | --- |
| TN | FP |
| FN | TP |

## Scores:
### The correct fraction + the incorrect fraction
$Accuracy + Error\:Rate = 1$  
$Accuracy = {TN+TP \over TN+TP+FN+FP}$  
$Error\:Rate = {FN+FP \over TN+TP+FN+FP}$  

### The correct rate for all positive prediction (vertical, right)
To increase precision, increase threshold to make fewer positive prediction.  
$Precision = {TP \over TP+FP}$  

### False Positive Rate (horizontal, upper)
The false prediction rate for all negative instances:  
$Specificity = {FP \over TN+FP}$  

### True Positive Rate (horizontal, lower)
The correct prediction rate for all positive instances:  
$Recall = {TP \over TP+FN}$  

$FPR + TNR= 1$  


## ROC
*ROC ~ plt.plot(FPR, TPR)*  
*ROC ~ plt.plot(1-specificity, recall)*  
where, both *FPR* and *TPR* are calculated horizontally.       

Once again there is a tradeoff: the higher the recall (TPR), the more false positives (FPR) the classifier produces. The dotted line represents the ROC curve of a purely random classifier; a good classifier stays as far away from that line as possible (toward the top-left corner). One way to compare classifiers is to measure the area under the curve (AUC). A perfect classifier will have a ROC AUC equal to 1, whereas a purely random classifier will have a ROC AUC equal to 0.5.
