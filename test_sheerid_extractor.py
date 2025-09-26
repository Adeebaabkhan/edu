"""
Test suite for SheerID Extractor simplified functionality.
"""

import json
import os
import tempfile
import unittest
from sheerid_extractor import SheerIDExtractor


class TestSheerIDExtractor(unittest.TestCase):
    """Test cases for SheerID Extractor simplified output functionality."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.extractor = SheerIDExtractor()
        
        # Sample comprehensive data with all the fields that would normally be saved
        self.comprehensive_data = [
            {
                "id": 10000158,
                "name": "Galgotias University",
                "country": "IN",
                "city": "Greater Noida",
                "state": "Uttar Pradesh",
                "website": "https://galgotiasuniversity.edu.in",
                "domain": "galgotiasuniversity.edu.in",
                "address": "Plot No. 2, Sector 17-A",
                "extraction_date": "2024-01-15",
                "query_found": True,
                "phone": "+91-120-2323000",
                "email": "info@galgotiasuniversity.edu.in",
                "type": "University",
                "status": "Active",
                "founded": "2011",
                "programs": ["Engineering", "Management"]
            },
            {
                "id": 10000256,
                "name": "Stanford University", 
                "country": "US",
                "city": "Stanford",
                "state": "California",
                "website": "https://www.stanford.edu",
                "domain": "stanford.edu",
                "address": "450 Jane Stanford Way",
                "extraction_date": "2024-01-15",
                "query_found": True,
                "phone": "+1-650-723-2300",
                "email": "info@stanford.edu",
                "type": "University",
                "status": "Active",
                "founded": "1885",
                "programs": ["Engineering", "Business"]
            }
        ]
        
        # Expected simplified output
        self.expected_simplified = [
            {
                "id": 10000158,
                "name": "Galgotias University",
                "country": "IN"
            },
            {
                "id": 10000256,
                "name": "Stanford University",
                "country": "US"
            }
        ]
    
    def test_process_institutions_returns_only_essential_fields(self):
        """Test that process_institutions returns only id, name, and country fields."""
        result = self.extractor.process_institutions(self.comprehensive_data)
        
        # Verify we get the expected number of records
        self.assertEqual(len(result), 2)
        
        # Verify each record has only the three essential fields
        for record in result:
            self.assertEqual(set(record.keys()), {"id", "name", "country"})
        
        # Verify the exact content matches expected output
        self.assertEqual(result, self.expected_simplified)
    
    def test_process_institutions_filters_incomplete_records(self):
        """Test that records missing essential fields are filtered out."""
        incomplete_data = [
            {"id": 1, "name": "Complete University", "country": "US"},  # Complete
            {"id": 2, "name": "Missing Country University"},  # Missing country
            {"name": "Missing ID University", "country": "CA"},  # Missing id
            {"id": 3, "country": "GB"},  # Missing name
        ]
        
        result = self.extractor.process_institutions(incomplete_data)
        
        # Only the complete record should be included
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], {"id": 1, "name": "Complete University", "country": "US"})
    
    def test_file_size_reduction(self):
        """Test that the simplified output significantly reduces file size."""
        self.extractor.process_institutions(self.comprehensive_data)
        
        original_size = len(json.dumps(self.comprehensive_data))
        simplified_size = len(json.dumps(self.extractor.output_data))
        
        # Verify significant size reduction (should be more than 50%)
        reduction_percent = ((original_size - simplified_size) / original_size) * 100
        self.assertGreater(reduction_percent, 50)
    
    def test_save_to_file(self):
        """Test that save_to_file creates correct output file."""
        self.extractor.process_institutions(self.comprehensive_data)
        
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as tmp_file:
            temp_filename = tmp_file.name
        
        try:
            self.extractor.save_to_file(temp_filename)
            
            # Verify file exists and contains expected data
            self.assertTrue(os.path.exists(temp_filename))
            
            with open(temp_filename, 'r', encoding='utf-8') as f:
                saved_data = json.load(f)
            
            self.assertEqual(saved_data, self.expected_simplified)
            
        finally:
            # Clean up
            if os.path.exists(temp_filename):
                os.unlink(temp_filename)
    
    def test_get_stats(self):
        """Test that get_stats returns correct processing statistics."""
        self.extractor.process_institutions(self.comprehensive_data)
        stats = self.extractor.get_stats()
        
        expected_stats = {
            "processed_count": 2,
            "output_records": 2,
            "fields_per_record": 3,
            "essential_fields": ["id", "name", "country"]
        }
        
        self.assertEqual(stats, expected_stats)
    
    def test_example_output_format_matches_requirements(self):
        """Test that output matches the exact format specified in requirements."""
        # Create data that matches the example in the problem statement
        example_data = [{
            "id": 10000158,
            "name": "Galgotias University",
            "country": "IN",
            # ... many other fields that should be filtered out
            "city": "Greater Noida",
            "state": "Uttar Pradesh",
            "website": "https://galgotiasuniversity.edu.in",
            "domain": "galgotiasuniversity.edu.in",
            "address": "Plot No. 2, Sector 17-A",
            "extraction_date": "2024-01-15",
            "query_found": True,
        }]
        
        result = self.extractor.process_institutions(example_data)
        
        expected = {
            "id": 10000158,
            "name": "Galgotias University",
            "country": "IN"
        }
        
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], expected)


if __name__ == '__main__':
    unittest.main()