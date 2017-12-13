
* `pbinom()`, `pnorm()`, `pgamma()`, `ppois()`, `punif()` = returns the cumulative probabilities from 0 up to a specified value from the binomial, normal, Gamma, Poisson, and uniform distributions


* `dnorm()`, `dgamma()`, `dpois()`, `dunif()` = return probability of a certain value from the normal, Gamma, Poisson, and uniform distributions


* if $A$ is ***independent*** of $B$, then the following are true
	* $A^c$ is independent of $B$
	* $A$ is independent of $B^c$
	* $A^c$ is independent of $B^c$




	`qbeta(quantileInDecimals, 2, 1)` = returns quantiles for beta distribution
	    * works for `qnorm()`, `qbinom()`, `qgamma()`, `qpois()`, etc.
	* median estimated in this fashion = a population median
	* probability model connects data to population using assumptions
		* population median = ***estimand***, sample median = ***estimator***

		

        * *coin flip example*: $E[X] = 0 \times (1-p) + 1 \times p = p$
	* ***continuous variable***
		* for $X$ with PDF $f(x)$, the expected value = the center of mass of the density
		* instead of summing over discrete values, the expectation ***integrates*** over a continuous function
			* PDF = $f(x)$
			* $\int xf(x)$ = area under the PDF curve = mean/expected value of $X$



		## Diagnostic Test
		* Let $+$ and $-$ be the results, positive and negative respectively, of a diagnostic test
		* Let $D$ = subject of the test has the disease, $D^c$ = subject does not
		* **sensitivity** = $P(+ | D)$ = probability that the test is positive given that the subject has the disease (the higher the better)
		* **specificity** = $P(- | D^c)$ = probability that the test is negative given that the subject does not have the disease (the higher the better)
		* **positive predictive value** = $P(D | +)$ = probability that that subject has the disease given that the test is positive
		* **negative predictive value** = $P(D^c | -)$ = probability that the subject does not have the disease given the test is negative
		* **prevalence of disease** = $P(D)$ = marginal probability of disease

		### Example
		* specificity of 98.5%, sensitivity = 99.7%, prevalence of disease = .1%
		$$\begin{aligned}
		P(D ~|~ +) & = \frac{P(+~|~D)P(D)}{P(+~|~D)P(D) + P(+~|~D^c)P(D^c)}\\
		& = \frac{P(+~|~D)P(D)}{P(+~|~D)P(D) + \{1-P(-~|~D^c)\}\{1 - P(D)\}} \\
		& = \frac{.997\times .001}{.997 \times .001 + .015 \times .999}\\
		& =  .062
		\end{aligned}$$
		* low positive predictive value $\rightarrow$ due to low prevalence of disease and somewhat modest specificity
			* suppose it was know that the subject uses drugs and has regular intercourse with an HIV infect partner (his probability of being + is higher than suspected)
			* evidence implied by a positive test result


		### Likelihood Ratios
		* **diagnostic likelihood ratio** of a **positive** test result is defined as $$DLR_+ = \frac{sensitivity}{1-specificity} =  \frac{P(+ | D)}{P(+ | D^c)}$$
		* **diagnostic likelihood ratio** of a **negative** test result is defined as $$DLR_- = \frac{1 - sensitivity}{specificity} =  \frac{P(- | D)}{P(- | D^c)}$$
		* from Baye's Rules, we can derive the *positive predictive value* and *false positive value*
		$$P(D | +) = \frac{P(+ | D)P(D)}{P(+ | D)P(D)+P(+ | D^c)P(D^c)}~~~~~~\mbox{(1)}$$
		$$P(D^c | +) = \frac{P(+ | D^c)P(D^c)}{P(+ | D)P(D)+P(+ | D^c)P(D^c)}~~~~~~\mbox{(2)}$$
		* if we divide equation $(1)$ over $(2)$, the quantities over have the same denominator so we get the following $$\frac{P(D | +)}{P(D^c | +)} = \frac{P(+ | D)}{P(+ | D^c)} \times \frac{P(D)}{P(D^c)}$$ which can also be written as $$\mbox{post-test odds of D} = DLR_+ \times \mbox{pre-test odds of D}$$
			* **odds** = $p/(1-p)$
			* $\frac{P(D)}{P(D^c)}$ = **pre-test odds**, or odds of disease in absence of test
			* $\frac{P(D | +)}{P(+ | D^c)}$ = **post-test odds**, or odds of disease given a positive test result
			* $DLR_+$ = factor by which the odds in the presence of a positive test can be multiplied to obtain the post-test odds
			* $DLR_-$ = relates the decrease in odds of disease after a negative result
		* following the previous example, for sensitivity of 0.997 and specificity of 0.985, so the diagnostic likelihood ratios are as follows $$DLR_+ = .997/(1-.985) = 66 ~~~~~~ DLR_- =(1-.997)/.985 = 0.003$$
			* this indicates that the result of the positive test is the odds of disease is 66 times the pretest odds
