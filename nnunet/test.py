from batchgenerators.utilities.file_and_folder_operations import *
plans_file = 'preprocessing_output_dir/Task04_Hippocampus/nnUNetPlans_plans_2D.pkl'
plans = load_pickle(plans_file)
print(plans)