"""Initialize the test suite for the advanced AI-driven security application."""

import unittest

# Import test modules
from tests.test_network_analysis import TestNetworkAnalysis
from tests.test_forensics import TestForensics
from tests.test_steganography import TestSteganography
from tests.test_reverse_engineering import TestReverseEngineering
from tests.test_crypto import TestCrypto
from tests.test_osint import TestOSINT
from tests.test_exploit_development import TestExploitDevelopment
from tests.test_dynamic_code_exec import TestDynamicCodeExec
from tests.test_polymorphic_code_gen import TestPolymorphicCodeGen
from tests.test_incident_response import TestIncidentResponse
from tests.test_threat_modeling import TestThreatModeling
from tests.test_risk_analysis import TestRiskAnalysis
from tests.test_ctf_simulation import TestCTFSimulation
from tests.test_red_team_tools import TestRedTeamTools
from tests.test_api_interaction import TestAPIInteraction
from tests.test_user_interface import TestUserInterface
from tests.test_external_tools import TestExternalTools
from tests.test_utils import TestUtils

# Initialize a test suite
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestNetworkAnalysis))
    suite.addTest(unittest.makeSuite(TestForensics))
    suite.addTest(unittest.makeSuite(TestSteganography))
    suite.addTest(unittest.makeSuite(TestReverseEngineering))
    suite.addTest(unittest.makeSuite(TestCrypto))
    suite.addTest(unittest.makeSuite(TestOSINT))
    suite.addTest(unittest.makeSuite(TestExploitDevelopment))
    suite.addTest(unittest.makeSuite(TestDynamicCodeExec))
    suite.addTest(unittest.makeSuite(TestPolymorphicCodeGen))
    suite.addTest(unittest.makeSuite(TestIncidentResponse))
    suite.addTest(unittest.makeSuite(TestThreatModeling))
    suite.addTest(unittest.makeSuite(TestRiskAnalysis))
    suite.addTest(unittest.makeSuite(TestCTFSimulation))
    suite.addTest(unittest.makeSuite(TestRedTeamTools))
    suite.addTest(unittest.makeSuite(TestAPIInteraction))
    suite.addTest(unittest.makeSuite(TestUserInterface))
    suite.addTest(unittest.makeSuite(TestExternalTools))
    suite.addTest(unittest.makeSuite(TestUtils))
    return suite

# Run the test suite
if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    test_suite = suite()
    runner.run(test_suite)