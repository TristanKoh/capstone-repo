This is the directory structure for the supporting documents for the article.


|   directory.txt
|   README.txt
|   
+---code (*contains all the code necessary to run the analysis and visualisations for the report*)
|   |   nlp_sentence_lime.ipynb
|   |   nlp_sentence_model_performance.ipynb
|   |   report_visualisations.ipynb
|   |   survey_results.ipynb
|   |   
|   +---data_restructuring (*contains the code used to compile all the policies from .yml to .csv file*)
|   |       concat_segment_text.py
|   |       concat_sentence_text.py
|   |       data_restructuring.ipynb
|   |       eda_sentence_text.ipynb
|   |       
|   \---visualisations (*contains the files needed to generate the explanations used for the survey*)
|           nlp_sentence_visualisation.ipynb
|           visualisations_and_expalnations_only.ipynb
|           
+---datasets 
|   |   concat_sentence_text.csv
|   |   
|   \---APP-350_v1.1 (*structure follows the authors who compiled the dataset*)
|       |   features.yml
|       |   LICENSE
|       |   README_APP-350.md
|       |   
|       +---annotations
|       |       *contains .yml files, one .yml file for each data privacy policy*
|       |
|       +---documentation
|       |       annotator_agreement.md
|       |       annotator_instructions.md
|       |       README.md
|       |       
|       \---original_documents
|               *contains the data privacy policies in .html, one file each for each data privacy policy*
|               
\---survey (*contains the survey questions and summary of answers, as well as the .csv file of the responses*)
        survey_questions.pdf
        survey_responses_summary.pdf
        survey_results_updated.csv
        
