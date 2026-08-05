import unittest

from patient_flow_forecaster.models import Record
from patient_flow_forecaster.scoring import score_record


class DepthCheck17(unittest.TestCase):
    def test_017_control_mapping(self):
        record = Record(id="encounter-017", exposure=44632, signal=0.300, urgency=4)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
