# test_walletbalanceapi.py
"""
Tests for WalletBalanceAPI module.
"""

import unittest
from walletbalanceapi import WalletBalanceAPI

class TestWalletBalanceAPI(unittest.TestCase):
    """Test cases for WalletBalanceAPI class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = WalletBalanceAPI()
        self.assertIsInstance(instance, WalletBalanceAPI)
        
    def test_run_method(self):
        """Test the run method."""
        instance = WalletBalanceAPI()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
