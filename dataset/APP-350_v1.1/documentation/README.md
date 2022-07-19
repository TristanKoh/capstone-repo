# Additional Documentation

## Creation of the Annotations

All 350 policies were consistently annotated by one of the authors, who is a lawyer with experience in data privacy law. In order to evaluate the reliability of the annotations we hired two law students who each annotated a randomly selected subset of 35 policies. We measured the agreement levels between the three annotators based on Krippendorff's Alpha. The results are contained in `annotator_agreement.md`. The annotations provided in this release are those of the author.

In order to obtain consistent annotations we provided annotation instructions to the annotators, which are contained in `annotator_instructions.md`. In addition, we trained the annotators and provided them with feedback on preliminary policy annotations that we asked them to do. We gave feedback to the annotators after they had annotated the set of preliminary policies. Once we were satisfied with their performance they were given the set of policies on which we want to measure agreement [1].


## Creation of Synthetic Data

In order to have more instances for negative practices (e.g., Location_3rdParty NOT_PERFORMED) we created synthetic data. We randomly selected a set of our annotated policies and derived new policies by manually changing the policy text from a positive to a negative instance (e.g., "We allow third parties to collect your location information." became "We do not allow third parties to collect your location information") and changing the labels accordingly. We apply the most common forms of negation [2].

We only added synthetic data to our training and validation sets.

[1] In total, we hired four laws students. However, as it turned out that our first two student annotators did not show a high level of agreement, we decided to not use their annotations. We took what we learnt and improved the process with two different annotators.

[2] Gunnel Tottie, [Negation in English Speech and Writing](https://www.ln.edu.hk/eng/rhetoric/Argumentative/Negation.html).
