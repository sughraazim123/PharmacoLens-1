""" 
Contains all the threshholds, constants, and defaults.
Maps common synonyms to the conical column names used internally
"""

column_aliases = {   # All the synonyms of samples that are reduced to 'sample_id' for internal consistency.
    # Updatable list based on the most common column names used in pharacology research datasets.
    
    # Sample identifiers
    'Sample id': 'sample_id',
    'sampleid': 'sample_id',
    'id': 'sample_id',
    'sample': 'sample_id',

    # Treatment / groups
    'treatement': 'group',
    'condition': 'group',
    
    # Replicates
    'replicate': 'replicate',
    'repeat': 'replicate', 
    'trial': 'replicate',
    
    # Timepoints
    'day': 'day', 
    'timepoint': 'day',
    'time': 'day',
    'visit': 'day' 

}

# Risk Scoring Weights
sensetivity_weights = {

    'strict': {'HIGH': 40, 'MEDIUM': 15, 'LOW': 5, 'INFO': 0},
    'standard': {'HIGH': 25, 'MEDIUM': 10, 'LOW': 3, 'INFO': 0},
    'lenient': {'HIGH': 15, 'MEDIUM': 5, 'LOW': 1, 'INFO':0}

}

# Risk Band Thresholds (normalisedscore 0-100)
risk_bands = [
    (0, 25, 'LOW'),
    (26, 60, 'MEDIUM'),
    (61, 100, 'HIGH')
]

# krusal-wallis test thresholds for drift detection as it is more robust to outliers and skewed data. Compared medians across three or more independent samples.
# Control Group Threshold
cv_warn_threshold: float = 15.0 #% cv above which --> medium
cv_high_threshold: float = 30.0 #% cv above which --> high
control_drift_p_value: float = 0.05 # p value for Krusal-Wallis drift

# replicate / outlier thresholds
outlier_z_threshold: float = 3.5 # z score above which a sample is considered an outlier

# range/missing thresholds
iqr_fence_multiplier: float = 3.0 #IQR multiplier for extreme values
missing_medium_pct: float = 5.0 # % missing above which --> medium concern
missing_high_pct: float = 20.0 # % missing above which --> high concern

# label fuzzy matching
fuzzy_math_threshold: int = 80 # 0-100; 80 catches typos reliably

# output / file handling
supported_extensions: list = ['.csv', '.xlsx', '.xls']
default_output_dir: str = './reports/'
report_data_format: str = '&Y%m%d_%H%M%S' # timestamp format for report naming

# Control Heuristic labels
# if metadata provided look for these strings in the group column
column_label_hints = ['control', 'ctrl', 'untreated', 'vehicle', 'placebo', 'baseline']






