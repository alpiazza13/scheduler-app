from fall2020_courses import classes_dict
import pandas as pd

failures = 0
classes_df = pd.DataFrame(columns=["course_id", "name", "course_number", "term", "professor", "am_pm", "days", "time", "link", "department"])
for department in classes_dict:
    for class1 in classes_dict[department]:
        try:
            values = list(class1.values())
            values.append(department)
            df_length = len(classes_df)
            classes_df.loc[df_length] = values
        except:
            # print(class1["course_id"])
            failures += 1

# print(classes_df.head(30))
# print(len(classes_df))

# print(failures)
