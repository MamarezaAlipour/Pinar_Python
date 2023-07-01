"""
Test Calibration class.
"""
import unittest
from pathlib import Path
import pandas as pd

from pinar import CONFIG
from pinar.entity.entity_def import Entity
from pinar.hazard.base import Hazard
from pinar.engine import ImpactCalc
from pinar.engine.calibration_opt import calib_instance
from pinar.util.constants import ENT_DEMO_TODAY
import pinar.hazard.test as hazard_test

HAZ_TEST_MAT = Path(hazard_test.__file__).parent.joinpath('data', 'atl_prob_no_name.mat')

DATA_FOLDER = CONFIG.test_data.dir()

class TestCalib(unittest.TestCase):
    """Test engine calibration method."""

    def test_calib_instance(self):
        """Test save calib instance"""
         # Read default entity values
        ent = Entity.from_excel(ENT_DEMO_TODAY)
        ent.check()

        # Read default hazard file
        hazard = Hazard.from_mat(HAZ_TEST_MAT)

        # get impact function from set
        imp_func = ent.impact_funcs.get_func(hazard.tag.haz_type,
                                             ent.exposures.gdf.impf_TC.median())

        # Assign centroids to exposures
        ent.exposures.assign_centroids(hazard)

        # create input frame
        df_in = pd.DataFrame.from_dict({'v_threshold': [25.7],
                                        'other_param': [2],
                                        'hazard': [HAZ_TEST_MAT]})
        df_in_yearly = pd.DataFrame.from_dict({'v_threshold': [25.7],
                                               'other_param': [2],
                                               'hazard': [HAZ_TEST_MAT]})

        # Compute the impact over the whole exposures
        df_out = calib_instance(hazard, ent.exposures, imp_func, df_in)
        df_out_yearly = calib_instance(hazard, ent.exposures, imp_func,
                                       df_in_yearly,
                                       yearly_impact=True)
        # calc Impact as comparison
        impact = ImpactCalc(ent.exposures, ent.impact_funcs, hazard).impact(assign_centroids=False)
        IYS = impact.impact_per_year(all_years=True)

        # do the tests
        self.assertTrue(isinstance(df_out, pd.DataFrame))
        self.assertTrue(isinstance(df_out_yearly, pd.DataFrame))
        self.assertEqual(df_out.shape[0], hazard.event_id.size)
        self.assertEqual(df_out_yearly.shape[0], 161)
        self.assertTrue(all(df_out['event_id'] ==
                            hazard.event_id))
        self.assertTrue(all(df_out[df_in.columns[0]].isin(
                df_in[df_in.columns[0]])))
        self.assertTrue(all(df_out_yearly[df_in.columns[1]].isin(
                df_in[df_in.columns[1]])))
        self.assertTrue(all(df_out_yearly[df_in.columns[2]].isin(
                df_in[df_in.columns[2]])))
        self.assertTrue(all(df_out['impact_PINAR'].values ==
                            impact.at_event))
        self.assertTrue(all(df_out_yearly['impact_PINAR'].values == [*IYS.values()]))


# Execute Tests
if __name__ == "__main__":
    TESTS = unittest.TestLoader().loadTestsFromTestCase(TestCalib)
    unittest.TextTestRunner(verbosity=2).run(TESTS)
