import unittest
import minotaurx_hash
from binascii import hexlify, unhexlify


class TestMinotaurX(unittest.TestCase):
    """Test suite for MinotaurX hash module"""

    # Test vector: block header and expected hash
    TEST_INPUT = "700000005d385ba114d079970b29a9418fd0549e7d68a95c7f168621a314201000000000578586d149fd07b22f3a8a347c516de7052f034d2b76ff68e0d6ecff9b77a45489e3fd511732011df0731000"
    EXPECTED_OUTPUT = (
        b"43ea5f3eaaac756aaa2711a18c234e13038dd3b1462aae1aa710bb158f4acca9"
    )

    def test_known_hash(self):
        """Test with known hash vector"""
        test_input = unhexlify(self.TEST_INPUT)
        result = minotaurx_hash.getPoWHash(test_input)
        result_hex = hexlify(result)

        self.assertEqual(
            result_hex,
            self.EXPECTED_OUTPUT,
            f"Expected {self.EXPECTED_OUTPUT}, got {result_hex}",
        )

    def test_output_length(self):
        """Test that output is always 32 bytes"""
        test_input = unhexlify(self.TEST_INPUT)
        result = minotaurx_hash.getPoWHash(test_input)

        self.assertEqual(
            len(result), 32, f"Expected 32-byte output, got {len(result)} bytes"
        )

    def test_output_type(self):
        """Test that output is bytes"""
        test_input = unhexlify(self.TEST_INPUT)
        result = minotaurx_hash.getPoWHash(test_input)

        self.assertIsInstance(
            result, bytes, f"Expected bytes output, got {type(result)}"
        )

    def test_invalid_input_length(self):
        """Test that function rejects wrong input size"""
        # Input should be exactly 80 bytes
        invalid_inputs = [
            b"",  # Empty
            b"short",  # Too short
            b"x" * 79,  # One byte short
            b"x" * 81,  # One byte too long
            b"x" * 160,  # Double size
        ]

        for invalid_input in invalid_inputs:
            with self.subTest(input_length=len(invalid_input)):
                # This should either raise an exception or handle gracefully
                try:
                    result = minotaurx_hash.getPoWHash(invalid_input)
                    # If no exception, result should still be 32 bytes
                    self.assertEqual(len(result), 32)
                except (TypeError, ValueError) as e:
                    # It's acceptable to raise an error for invalid input
                    self.assertIn(
                        "80",
                        str(e),
                        "Error message should indicate 80-byte requirement",
                    )

    def test_deterministic(self):
        """Test that same input always produces same output"""
        test_input = unhexlify(self.TEST_INPUT)
        result1 = minotaurx_hash.getPoWHash(test_input)
        result2 = minotaurx_hash.getPoWHash(test_input)

        self.assertEqual(
            result1, result2, "Same input should always produce same output"
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
