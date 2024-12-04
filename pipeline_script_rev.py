from pathlib import Path
from mesc_tiff_data_extract_package import mesc_data_handling_rev
from mesc_tiff_data_extract_package import suite2p_script_rev

import os
'''
'root_directory': base directory, contains the TIFF files, all the subfolders and processed files get saved here 
i.e.: 'C:/Hyperstim/data_analysis/2024_09_GCaMP6s_in_vivo/'
'tiff_directory': it will always be the path of {root_directory}/merged_tiffs/ because of the folder system of the pipeline
i.e.: 'C:/Hyperstim/data_analysis/2024_09_GCaMP6s_in_vivo/merged_tiffs/'
'exp_file_name': name of the experiment file (from MESc)
i.e.: '2024_09_GCaMP6s_in_vivo' 
be aware: the experimental file name ends before the '_MUnit_' suffix
'mesc_DATA_file': it will always be 'mesc_data.npy' there is no need to change this
'list_of_file_nums': the numbers of the TIFF files which are to be concatenated in the process, it is possible to give more lists
be aware: the order of the numbers given in the list will be the order of concatenation
possible forms: [[1,2,3], [1,2]] ; [['1', '2']] ; [1] the order of the lists are not relevant
gcamp: for GCaMP6f: 'f', for GCaMP6s: 's' optimised parameter values
'''
#------VALUES TO CHANGE------

root_directory = 'C:/Hyperstim/test4juan/' #
tiff_directory = 'C:/Hyperstim/test4juan/merged_tiffs/'
exp_file_name = '2024_09_18_GCamp6s_in_vivo_2'
mesc_DATA_file = 'mesc_data.npy'
list_of_file_nums = [
  [4,5,6]
]
gcamp = 's' #for GCaMP6s: 's' , for GCaMP6f: 'f'

#------VALUES TO CHANGE END------

output_subfolders = mesc_data_handling_rev.tiff_merge(exp_file_name, list_of_file_nums, root_directory)
suite2p_script_rev.run_suite2p(output_subfolders, tiff_directory, gcamp)

#--------------Suite2p manual sorting------------------


