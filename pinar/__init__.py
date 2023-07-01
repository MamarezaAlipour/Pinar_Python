"""
pinar init
"""
from shutil import copyfile
from pathlib import Path

from .util.config import CONFIG
from .util.constants import *


GSDP_DIR = SYSTEM_DIR.joinpath('GSDP')

REPO_DATA = {
    'data/system': [
        ISIMIP_GPWV3_NATID_150AS,
        GLB_CENTROIDS_MAT,
        ENT_TEMPLATE_XLS,
        HAZ_TEMPLATE_XLS,
        RIVER_FLOOD_REGIONS_CSV,
        NATEARTH_CENTROIDS[150],
        NATEARTH_CENTROIDS[360],
        SYSTEM_DIR.joinpath('WEALTH2GDP_factors_CRI_2016.csv'),
        SYSTEM_DIR.joinpath('GDP_TWN_IMF_WEO_data.csv'),
        SYSTEM_DIR.joinpath('FAOSTAT_data_country_codes.csv'),
        SYSTEM_DIR.joinpath('rcp_db.xls'),
        SYSTEM_DIR.joinpath('tc_impf_cal_v01_TDR1.0.csv'),
        SYSTEM_DIR.joinpath('tc_impf_cal_v01_EDR.csv'),
        SYSTEM_DIR.joinpath('tc_impf_cal_v01_RMSF.csv'),
    ],
    'data/system/GSDP': [
        GSDP_DIR.joinpath(f'{cc}_GSDP.xls')
        for cc in ['AUS', 'BRA', 'CAN', 'CHE', 'CHN', 'DEU', 'FRA', 'IDN', 'IND', 'JPN', 'MEX',
                   'TUR', 'USA', 'ZAF']
    ],
    'data/demo': [
        ENT_DEMO_TODAY,
        ENT_DEMO_FUTURE,
        EXP_DEMO_H5,
        HAZ_DEMO_FL,
        HAZ_DEMO_MAT,
        HAZ_DEMO_H5,
        TC_ANDREW_FL,
        DEMO_DIR.joinpath('demo_emdat_impact_data_2020.csv'),
        DEMO_DIR.joinpath('nl_rails.gpkg'),
    ] + WS_DEMO_NC
}


def test_installation():
    """Run this function to check whether pinar is working properly.
    If the invoked tests pass and an OK is printed out, the installation was successfull.
    """
    from unittest import TestLoader, TextTestRunner
    suite = TestLoader().discover(start_dir='pinar.engine.test',
                                  pattern='test_cost_benefit.py')
    suite.addTest(TestLoader().discover(start_dir='pinar.engine.test',
                                        pattern='test_impact.py'))
    TextTestRunner(verbosity=2).run(suite)


def setup_pinar_data(reload=False):
    """This function is called when pinar is imported.
    It creates a pinar directory by default in the home directory.
    Other locations can be configured in the pinar.conf file.


    Parameters
    ----------
    reload : bool, optional
        in case system or demo data have changed in the github repository, the local copies of
        these files can be updated by setting reload to True,
        by default False
    """
    for dirpath in [DEMO_DIR, SYSTEM_DIR, GSDP_DIR]:
        dirpath.mkdir(parents=True, exist_ok=True)

    for src_dir, path_list in REPO_DATA.items():
        for path in path_list:
            if not path.exists() or reload:
                src = Path(__file__).parent.parent.joinpath(src_dir, path.name)
                copyfile(src, path)

setup_pinar_data()
