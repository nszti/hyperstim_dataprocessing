import numpy as np
import os
from pathlib import Path
import tifftools


def tiff_merge(exp_file_name, list_of_file_nums, output_root_directory):
    '''
    Parameters
    ----------
    'exp_file_name': name of the experiment file (from MESc)
    'list_of_file_nums': the numbers of the TIFF files which are to be concatenated in the process
    'output_root_directory': base directory, contains the TIFF files
    -------

    Returns
    -------
    makes 'merged_tiffs' directory, saves merged (concatenated) files to separate folders
    the function gets the list of numbers and matches them to the tiff file names, then concatenates the files and saves them into the 'merged_tiffs' directory
    each concatenated file gets the prefix of 'merged', then the original tiff file name, and the numbers of the merged files separated by '_'.  this structure is for easier file management later,
    '''

    suffix = '_MUnit_'
    outer_directory = os.path.join(output_root_directory, 'merged_tiffs')
    os.makedirs(outer_directory, exist_ok=True)
    print(f"MESc file name: {exp_file_name}")
    output_subfolders = []
    for numbers_to_merge in list_of_file_nums:
        base_filename = exp_file_name + suffix

        tiff_files_li = [os.path.join(output_root_directory, f"{base_filename}{num}.tif") for num in numbers_to_merge]
        for file in tiff_files_li:
            if not os.path.isfile(file):
                print(f"Error: File {file} does not exist:(")
                exit(1)

        output_dirname = 'merged_' + base_filename + '_'.join(map(str, numbers_to_merge))
        output_filepath = outer_directory + '/' + output_dirname
        os.makedirs(output_filepath, exist_ok=True)

        output_filename = 'merged_' + base_filename + '_'.join(map(str, numbers_to_merge)) + '.tif'
        output_fpath = output_filepath + '/' + output_filename
        tifftools.tiff_concat(tiff_files_li, output_fpath, overwrite=True)
        output_subfolders.append(output_filepath)
        print(f"Files {tiff_files_li} merged into {output_filepath}")

    return output_subfolders








