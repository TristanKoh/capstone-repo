# Draft structure of capstone
## Research question:
How far are AI NLP models that are trained on legal datasets interpretable?
- Interpretable means the ability to explain or to present in understandable terms to a human.
- I'll be using the APP-350 corpus as a representative legal dataset as it contains real-world legal data. 
- The main literature that I'll be using as a guide for the capstone methodology is "Towards a Rigorous Science of Interpretable Machine Learning". ("Rigorous Science")

## Introduction / Abstract
Objective of capstone + methodology

- What is XAI
- What is legal tech 
- What are AI models used for in the legal tech context

## Rationale of capstone: Why is interpretability important in the context ML models that are trained on legal datasets?
- Increase legitimacy of predictions and user trust in the system - because law is equally (if not more) concerned about the justification for a decision compared to the decision itself (We The Robots Chapter 6, pg 146)
- Ensure that the system is optimising for the ultimate objective (instead of a proxy objective) - interpretability as a diagnostic tool to train better performing models that are specific to legal vocabulary (Rigorous Science, section 2, pg 3)
- While current trend of AI techniques are more accurate, complexity has also increased.

Need citations: 
- Uptake of legal tech in industry
- What type of AI models are used
- Increasing complexity of AI models in recent years

## Explaining current XAI Techniques for NLP
- Current methods for NLP XAI
- Why Interpret was chosen? 

## Why this dataset was chosen
- What are the features of this dataset that makes it suitable for the capstone?
- How can we generalise our observations from this example dataset?

Need citations: 
- How are NLP models trained on datasets usually? OR
- How are legal tech AI models trained in the industry?

## Methodology: User surveys
To assess the interpretability of the XAI models that I'll be training, I intend to conduct user surveys on law and non-law students. 

In particular, these user surveys would ask three types of questions (from Section 3.2 of Rigorous Science):
- Binary forced choice: humans are presented with pairs of explanations, and must choose the one that they find of higher quality.
- Forward simulation/prediction: humans are presented with an explanation and an input, and must correctly simulate the model's output (regardless of the true output).
- Counterfactual simulation: humans are presented with an explanation, an input, and an output, and are asked what must be changed to change the method's prediction to a desired output (and related variants).

## Timeline of project
The rough timeline of the capstone project would be:
- Semester 1: Train and assess performance of XAI models (in terms of data science performance metrics)
- Semester 2: Conduct user surveys to assess the interpretability of the models' explanations.
