def get_drift_function(algo: str):
    algo = algo.lower()
    if algo == "psi":
        return psi_drift
    elif algo == "ks":
        return ks_drift
    elif algo == "shap":
        return shap_drift
    elif algo == "tree":
        return tree_drift
    elif algo == "wasserstein":
        return wasserstein_drift
    else:
        raise ValueError(
            f"Unsupported drift algorithm: {algo}. Must be one of: "
            "'psi', 'ks', 'shap', 'tree', 'wasserstein'"
        )
