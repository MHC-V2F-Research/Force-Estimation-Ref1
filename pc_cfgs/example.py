﻿import os
# Empty dict to store machine specific info
mdlParams = {}
# Define machine specific paths
mdlParams['pathBase'] = os.environ['HOME']

# Define machine specific vars
mdlParams['batchSizefac'] = 1