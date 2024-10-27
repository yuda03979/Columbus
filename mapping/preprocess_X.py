import pandas as pd
import numpy as np


class PreprocessX:
    """
    take the numerical features and make them discrete values.
    also handle all the possibilities for all the data.
    """
    def __init__(self, X, numerical_features, num_splits=3, split_method='median'):
        self.X = X
        self.numerical_features = numerical_features
        self.num_splits = 2 ** num_splits
        self.split_method = split_method
        self.verify_init()


    def verify_init(self):
        split_methods = []
        if self.split_method not in split_methods:
            raise f"split method ({self.split_method}) not in split methods: ({split_methods})"

        max_num_splits = 2 ** 4
        if self.num_splits > max_num_splits:
            raise f"num_splits: ({self.num_splits}) > max_num_splits: ({max_num_splits})"

        for col in self.numerical_features:
            if col not in self.X.columns:
                raise f"col {col} not in X.columns"

