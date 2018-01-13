

## Linear models
### Logistic
The logistic function transforms real-valued input to an output number y between 0 and 1, interpreted as the probability the input object belongs to the positive class, given its input features (𝑥0, 𝑥1, ..., 𝑥𝑛)

* L2 Regularization is 'on' by default (like ridge regression). Parameter C controls amount of regularization (default 1.0).  
As with regularized linear regression, it can be important to normalize all features so that they are on the same scale.


### SVM
* Regularization: the strength of regularization is determined by C.   
Larger values of C: less regularization. Fit the training data as well as possible. Smaller values of C: more regularization. More tolerant of errors on individual data points.  




### Linear Models: Pros and Cons
* Pros:  
Fast prediction.  
Scales well to very large datasets.  
Works well with sparse data.  
* Cons:  
For lower-dimensional data, other models may have superior generalization performance.  
For classification, data may not be linearly separable (more on this in SVMs with non-linear kernels).  


### Linear Model: Important Parameters
Model complexity:  
* alpha: weight given to the L1 or L2 regularization term in regression models, default = 1.0.  
* C: regularization weight for LinearSVCand LogisticRegressionclassification models, default = 1.0.  
