"""
init test
"""

from pinar.util.api_client import Client


def get_test_file(ds_name, file_format=None):
    """convenience method for downloading test files from the PINAR Data API.
    By convention they have a status 'test_dataset', their name is unique and they contain a single
    file. These conventions are used to identify and download the file to the
    PINAR data folder.

    Parameters
    ----------
    ds_name : str
        name of the dataset
    file_format : str, optional
        file format to look for within the datasets files.
        Any format is accepted if it is ``None``.
        Default is ``None``.
    Returns
    -------
    pathlib.Path
        the path to the downloaded file
    """
    client = Client()
    test_ds = client.get_dataset_info(name=ds_name, status='test_dataset')
    _, files = client.download_dataset(test_ds)
    [test_file] = [fil for fil in files if fil.name in [
        dsf.file_name 
        for dsf in test_ds.files 
        if file_format is None or dsf.file_format == file_format]]
    return test_file
