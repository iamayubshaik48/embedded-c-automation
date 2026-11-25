
import subprocess
import unittest
from pathlib import Path

APP = (
    Path(__file__).resolve().parents[1]
    / "build"
    / "temperature_monitor"
)


class TemperatureTests(unittest.TestCase):

    def check_temperature(self, value, expected):
        result = subprocess.run(
            [str(APP), str(value)],
            capture_output=True,
            text=True
        )

        self.assertEqual(result.returncode, 0)
        self.assertIn(expected, result.stdout)

    def test_normal_temperature(self):
        self.check_temperature(25, "STATUS: NORMAL")

    def test_warning_temperature(self):
        self.check_temperature(36, "STATUS: WARNING")

    def test_critical_temperature(self):
        self.check_temperature(46, "STATUS: CRITICAL")

    def test_invalid_temperature(self):
        result = subprocess.run(
            [str(APP), "abc"],
            capture_output=True,
            text=True
        )

        self.assertEqual(result.returncode, 2)
        self.assertIn("ERROR", result.stderr)


if __name__ == "__main__":
    unittest.main(verbosity=2)
