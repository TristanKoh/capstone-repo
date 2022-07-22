# Applying Explainable AI techniques using Interpret Text to the APP-350 Corpus
This project is for the purposes of fulfilling the law and liberal arts capstone under the Yale-NUS and NUS Law Double Degree Program.
## Definitions
1. **Explainable AI** is a branch of AI that seeks to explain the predictions of machine learning models through statistical explanations and visualisations.

2. **Natural Language Processing** (NLP) is a subset of machine learning that aims to quantifiably analyse natural language. 

3. **Interpret Text** is a Python framework that makes it easier to interpret the predictions of NLP models.

4. **APP-350 Corpus** is a corpus of 350 Android app privacy policies annotated with privacy practices (i.e. behaviour that can have privacy implications). 

## Objective of capstone
Using _Interpret Text_, I aim to train a machine learning model using the _APP-350_ corpus to predict the type of privacy practices within app privacy policies. I then use _Interpret Text's_ tools to visualise why the model made such predictions from a machine learning perspective. I then compare and contrast this with how a legally-trained human would reason about the privacy policy.

## Rationale of capstone
Natural language forms the bread & butter of the legal industry, as expressed in contracts, judgements and legislation. There has been an increasing trend within the legal industry to adopt more machine learning techniques to automate and assist low level legal analysis. Within the specific context of data privacy, it would be useful to have a tool that assesses the possible data privacy risks of user policies. Such a tool would naturally use NLP techniques. Nevertheless, these tools should still be accessible to the layperson lawyer that might not be trained in data science.

While NLP techniques have substantially increased in performance in recent years, it has come at the cost of explainability of predictions because of the usage of artificial neural networks which are architecturally more complex than traditional machine learning models. This lack of explainability of more advanced machine learning models could potentially be a significant hindrance towards their adoption within the legal industry because the lawyer / law firm which uses these models still ultimately bear the responsibility of ensuring that the analysis is legally sound. 

However, the intersection in skillset between data science and legal analysis is still nascent and it is also unrealistic all legally trained personnel to be trained in data science to the extent required to interpret the predictions of machine learning models without aid.
Therefore, my capstone aims to bridge the gap between the lawyer and the data scientist by using _Interpret Text_ to explain the predictions of a machine learning model in the context of assessing data privacy practices of app policies.

## More about the APP-350 corpus
The APP-350 Corpus consists of 350 annotated Android app privacy policies. Each annotation consists of a practice and a modality.

A *privacy practice* (or *practice*) describes a certain behaviour of an app that can have privacy implications (e.g., collection of a phone's device identifier or sharing of its location with ad networks). We have annotations for 58 different practices. 

There are only two modalities: PERFORMED  (i.e., a practice is explicitly described as being performed) and NOT_PERFORMED (i.e., a practice is explicitly described as not being performed).

A more detailed overview of the corpus can be found [here](dataset/APP-350_v1.1/README_APP-350.md).

## How Interpret Text explains predictions

[Interpret Text](https://github.com/interpretml/interpret-text#interpret-text---alpha-release) is a Python package developed by Microsoft. It is an XAI package that is specific to explaining text classification models. 

More details to be added. 