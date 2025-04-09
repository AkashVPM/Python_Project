import os
import shutil

def list_folders(parent_folder, destination_folder, file_name):
    run_counter = 1 
    for root, dirs, files in os.walk(parent_folder):
        if file_name in files:
            try:
                new_file_name = f'run_{run_counter}.h3d'
                destination_file = os.path.join(destination_folder, new_file_name)
                file_path = os.path.join(root, 'DOE_morph.h3d')
                shutil.copy(file_path, destination_file) 
                run_counter += 1
                print(f"{file_name} found in folder: {root} and copied to {destination_folder} as {new_file_name}")
            except PermissionError:
                print(f"Permission denied: Unable to copy to {destination_file}")
            except Exception as e:
                print(f"An error occurred: {e}")

# Parent folder where you start the search
parent_folder = r"D:\Hypermesh_v25\DoE\approaches\doe_2"
destination_folder =r"D:\Hypermesh_v25\Doe_Morph_result"
file_name = 'DOE_morph.h3d'
list_folders(parent_folder=parent_folder,destination_folder=destination_folder,file_name=file_name)
