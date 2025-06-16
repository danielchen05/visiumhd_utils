"""
destripe.py
Includes function to reduce the striping effect of VisiumHD data.
Pre-processing using read_data functions is required.
Some functions are taken from bin2cell package.
"""
import bin2cell as b2c

def destripe_b2c(sdata, quantile = 0.99, only2um=):
    """
    function to destripe VisiumHD data. primarily taken from bin2cell package
    Note: bin2cell works on AnnData objects, which need to be extracted from spatialdata object

    Correct the raw counts of the input object for known variable width of 
    VisiumHD 2um bins. Scales the total UMIs per bin on a per-row and 
    per-column basis, dividing by the specified ``quantile``. The resulting 
    value is stored in ``.obs[factor_key]``, and is multiplied by the 
    corresponding total UMI ``quantile`` to get ``.obs[adjusted_counts_key]``.

    Args:
    sdata: the spatialdata object
    quantile: the quantile needed for destriping (default at 99% by b2c)

    Return:
    sdata: the resulting spatialdata object
    """


def plot_destriped_bins():
    """
    function to plot adjusted counts after destriping for bins
    """