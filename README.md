# hyperstim_dataprocessing
Package for processing recorded two-photon calcium imaging data with suite2p



# README

### Location of the Scripts:
```bash
git clone -v git@github.com:nszti/hyperstim_dataprocessing.git
```

---

### Basic Description of Our Process:
1. **TIFF File Extraction**: 
   - TIFF files from the two-photon recording sessions are extracted from the MESc file. These TIFF files are used exclusively for the rest of the process. Each file represents a single recording of an experiment with a specific stimulus parameter set to observe its effect.

2. **TIFF File Concatenation**: 
   - TIFF files from one recording session are concatenated based on the changed parameter type.
   - For example, if `tiff_1`, `tiff_2`, and `tiff_3` are recordings of experiments performed with different current amplitudes (e.g., -10, -20 and -30 uA), they will be concatenated.

3. **Input to Suite2p**:
   - The merged (or individual) TIFF files serve as the input to Suite2p, which runs with adjusted parameter values optimized for GCaMP6f and GCaMP6s indicators.

---

### Folder Structure Created by the Pipeline:
- **Root Directory**: Contains the TIFF files of the experiment.
  - **`merged_tiffs` Folder**: Contains subfolders of concatenated (merged) TIFF files necessary for running Suite2p.
    - **concatenated TIFF Files**: Each subfolder contains a single merged TIFF file.

---

### Contents:
1. **`pipeline_script_rev.py`**:
   - This script calls functions to process the data.
   - The meanings of input parameters (root_directory, tiff_directory, exp_file_name, mesc_DATA_file, list_of_file_nums) are explained within the script.
   - **`Mesc_data.npy`**: The input for parameter "mesc_DATA_file". This file is a Pandas DataFrame containing three datasets extracted from the MESc recordings, converted into a `.npy` file.
     - **Datasets in the DataFrame**:
       - **`FileID`**: ID of the TIFF file extracted from individual recordings.
       - **`FrameNo`**: Number of frames in an individual recording.https://github.com/nszti/hyperstim_dataprocessing/tree/main
       - **`Trigger`**: The frame number corresponding to the time point at which the electrical stimulation started.

2. **`mesc_data_handling_rev.py`**:
   - Contains the function `tiff_merge()`, which:
     - Creates the `merged_tiffs` folder.
     - Receives input from `pipeline_script_rev.py`.
     - Merges the corresponding TIFF files into separate folders.
   - **Nomenclature**:
     - **Folder Name**: `merged_experimentname_MUnit_number1_number2`
     - **TIFF File Name**: `merged_experimentname_MUnit_number1_number2.tif`

3. **`suite2p_script_rev.py`**:
   - Based on Suite2p notebooks available on [GitHub](https://github.com/MouseLand/suite2p.git).
   - Defines parameters for GCaMP6f and GCaMP6s indicators.

---

### Additional Explanations:
Descriptions of parameter lists for functions are provided at the beginning of each script.

---

### Help to Avoid Errors:
1. Suite2p only works with **Python version 3.9**.
2. Code runs best with the **Suite2p interpreter**.
3. Ensure the `.suite2p` folder is present to access the default ops dictionary.
