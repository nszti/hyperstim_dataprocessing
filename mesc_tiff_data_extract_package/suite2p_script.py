import os
import suite2p
from suite2p.run_s2p import run_s2p
from mesc_tiff_data_extract_package import tiff_file_merger

def run_suite2p(merged_folders, data_path, gcamp):
      '''

      Input parameters
      ----------
      merged_folders:
      data_path: outer folder containing 'merged' folders,  usually same as 'tiff_directory' (explained in pipeline_script)
      gcamp: f or s depending on the indicator in the experiments
      'run_s2p()' returns one ops dictionary for each plane processed, here the default parameters are used for the ops dictionary.
      The specific parameters for GCaMP6f and GCaMP6s are given in db lists, because parameters provided in db will overwrite parameters specified in ops
      The base code used for this part can be accessed in the github site of Suite2p. Additional useful scripts: https://github.com/MouseLand/suite2p/blob/main/jupyter/run_suite2p_colab_2023.ipynb
      Returns
      -------
      runs suite2p with predefined parameters
      output: 'suite2p' subfolder in each merged file folder with extracted data detailed here: https://suite2p.readthedocs.io/en/latest/outputs.html
      '''
      ops = suite2p.default_ops()
      db_list = []
      for sublist in [merged_folders]:
            for subfolder in sublist:
                  if gcamp == 'f':
                        db_list.append({
                              'h5py': [],  # a single h5 file path
                              'h5py_key': 'data',
                              'look_one_level_down': False,  # whether to look in ALL subfolders when searching for tiffs
                              'data_path': [subfolder],
                              'subfolders': [],  # choose subfolders of 'data_path' to look in (optional)
                              'tau': 0.5,
                              'fs': 31.0,
                              'batch_size': 500,
                              'spatial_scale': 1,
                              'denoise': True,
                              'threshold_scaling': 0.25,
                              'max_overlap': 0.7,
                              'high_pass': 300
                        })
                  if gcamp == 's':
                        db_list.append({
                              'h5py': [],  # a single h5 file path
                              'h5py_key': 'data',
                              'look_one_level_down': False,  # whether to look in ALL subfolders when searching for tiffs
                              'data_path': [subfolder],
                              'subfolders': [],  # choose subfolders of 'data_path' to look in (optional)
                              'tau': 1.25,
                              'fs': 31.0,
                              'batch_size': 500,
                              'spatial_scale': 2,
                              'denoise': True,
                              'threshold_scaling': 0.1,
                              'max_overlap': 0.7,
                              'high_pass': 300
                        })
      for dbi in db_list:
            opsEnd = run_s2p(ops=ops, db=dbi)
