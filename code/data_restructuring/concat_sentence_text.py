import os
import yaml
from yaml import SafeLoader
import pandas as pd
import glob

os.getcwd()

DATASET_PATH = r"dataset/APP-350_v1.1/annotations/"
ALL_FILES_PATH = glob.glob(DATASET_PATH + r"*")

list_df = []
final_df = pd.DataFrame()
row_count_ls = []

# NOTE: Change index to import for all yml files
for file_index, FILE in enumerate(ALL_FILES_PATH) :
    print(FILE)
    with open(FILE, encoding = "utf-8") as f:
        print("loading: " + str(file_index))
        doc = yaml.load(f, Loader=SafeLoader)
        df_doc = pd.json_normalize(doc, record_path=["segments"])
        
        # Flatten to sentence_text level
        sentence_dict = {"sentence_text" : [], "practice" : [], "modality" : []}
        # Iterate on the 4th column
        for row in df_doc.itertuples():
            # If there are tagged sentences
            if len(row[4]) != 0 :
                for sentence in row[4] :
                    sentence_dict["sentence_text"].append(sentence["sentence_text"])
                    # Index is to keep track if there are more than 1 practice associated with each sentence. 
                    # If there is, create a new key value pair for the same sentence with the 2nd (or more practice)
                    for index, annotation in enumerate(sentence["annotations"]) :
                        sentence_dict["practice"].append(annotation["practice"])
                        sentence_dict["modality"].append(annotation["modality"])
                        if index > 0 :
                            sentence_dict["sentence_text"].append(sentence["sentence_text"])
        
        temp_df = pd.DataFrame(sentence_dict)
        list_df.append(temp_df)
        row_count_ls.append(temp_df.shape[0])


        print("DONE")
        print("-" * 50)


final_df = pd.concat(list_df)

# Check that number of rows are the same in the final df
sum(row_count_ls) == final_df.shape[0]

# Sanity check
final_df.shape[0]
final_df.head(50)

# Export to csv
final_df.to_csv(r"dataset\concat.csv", index = False, encoding = "utf-8", header = True)