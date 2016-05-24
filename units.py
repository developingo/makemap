import testutils
import re

def inch_to_mm (inch):
    return inch * 25.4

def mm_to_inch (mm):
    return mm / 25.4

def mm_to_pt (mm):
    return mm / 25.4 * 72.0

def pt_to_mm (pt):
    return pt / 72.0 * 25.4

mm_re = re.compile ("^([-+]?\d*\.?\d+)\s*mm$")

def parse_units_str (str):
    m = mm_re.match (str)
    if m == None:
        return None

    mm = m.group (1)
    return float (mm)

########## tests ##########

class TestUnitConversions (testutils.TestCaseHelper):
    def mm_inch_roundtrip (self, x):
        self.assertFloatEquals (inch_to_mm (mm_to_inch (x)), x)
        self.assertFloatEquals (mm_to_inch (inch_to_mm (x)), x)

    def test_mm_to_inch_conversion_roundtrips (self):
        self.mm_inch_roundtrip (0)
        self.mm_inch_roundtrip (1)
        self.mm_inch_roundtrip (10)
        self.mm_inch_roundtrip (-1)
        self.mm_inch_roundtrip (-10)

    def mm_pt_roundtrip (self, x):
        self.assertFloatEquals (mm_to_pt (pt_to_mm (x)), x)
        self.assertFloatEquals (pt_to_mm (mm_to_pt (x)), x)

    def test_mm_to_pt_conversion_roundtrips (self):
        self.mm_pt_roundtrip (0)
        self.mm_pt_roundtrip (1)
        self.mm_pt_roundtrip (10)
        self.mm_pt_roundtrip (-1)
        self.mm_pt_roundtrip (-10)

    def test_can_parse_mm (self):
        self.assertFloatEquals (11.0, parse_units_str ("11mm"))

    def test_can_parse_mm_with_space (self):
        self.assertFloatEquals (11.0, parse_units_str ("11 mm"))
