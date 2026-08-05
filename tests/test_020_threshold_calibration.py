import unittest

from patient_flow_forecaster.models import Record
from patient_flow_forecaster.scoring import score_record


class DepthCheck20(unittest.TestCase):
    def test_020_threshold_calibration(self):
        record = Record(id="encounter-020", exposure=56343, signal=0.392, urgency=8)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
