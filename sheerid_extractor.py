"""
SheerID Extractor - Simplified version that outputs only essential institution fields.

This module provides functionality to extract and process educational institution data
from SheerID with minimal output containing only id, name, and country.
"""

import json
from datetime import datetime
from typing import List, Dict, Any


class SheerIDExtractor:
    """
    SheerID Extractor class for processing educational institution data.
    
    This class focuses on extracting only the essential fields:
    - id: Institution identifier
    - name: Institution name
    - country: Country code
    """
    
    def __init__(self):
        """Initialize the SheerID Extractor."""
        self.processed_count = 0
        self.output_data = []
    
    def process_institutions(self, institutions_data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Process institution data and return simplified records.
        
        This method takes comprehensive institution data and extracts only
        the three essential fields: id, name, and country.
        
        Args:
            institutions_data: List of institution dictionaries with comprehensive data
        
        Returns:
            List of simplified institution dictionaries with only id, name, and country
        
        Example:
            Input institution record might contain:
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
                "programs": ["Engineering", "Management", "Science"]
            }
            
            Output will be:
            {
                "id": 10000158,
                "name": "Galgotias University",
                "country": "IN"
            }
        """
        simplified_institutions = []
        
        for institution in institutions_data:
            # Extract only the three essential fields
            simplified_record = {
                "id": institution.get("id"),
                "name": institution.get("name"),
                "country": institution.get("country")
            }
            
            # Only add records that have all required fields
            if all(value is not None for value in simplified_record.values()):
                simplified_institutions.append(simplified_record)
                self.processed_count += 1
        
        self.output_data = simplified_institutions
        return simplified_institutions
    
    def save_to_file(self, filename: str = "institutions_simplified.json") -> None:
        """
        Save the processed institutions to a JSON file.
        
        Args:
            filename: Output filename for the simplified data
        """
        if not self.output_data:
            raise ValueError("No data to save. Run process_institutions first.")
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.output_data, f, indent=2, ensure_ascii=False)
        
        print(f"Saved {len(self.output_data)} simplified institution records to {filename}")
    
    def get_stats(self) -> Dict[str, Any]:
        """
        Get processing statistics.
        
        Returns:
            Dictionary with processing statistics
        """
        return {
            "processed_count": self.processed_count,
            "output_records": len(self.output_data),
            "fields_per_record": 3,  # id, name, country
            "essential_fields": ["id", "name", "country"]
        }


# Example usage and demonstration
if __name__ == "__main__":
    # Sample comprehensive institution data (simulating what might come from SheerID API)
    sample_comprehensive_data = [
        {
            "id": 10000158,
            "name": "Galgotias University",
            "country": "IN",
            "city": "Greater Noida",
            "state": "Uttar Pradesh", 
            "website": "https://galgotiasuniversity.edu.in",
            "domain": "galgotiasuniversity.edu.in",
            "address": "Plot No. 2, Sector 17-A, Yamuna Expressway",
            "extraction_date": "2024-01-15",
            "query_found": True,
            "phone": "+91-120-2323000",
            "email": "info@galgotiasuniversity.edu.in",
            "type": "University",
            "status": "Active",
            "founded": "2011",
            "programs": ["Engineering", "Management", "Science", "Law", "Pharmacy"]
        },
        {
            "id": 10000256,
            "name": "Stanford University",
            "country": "US",
            "city": "Stanford",
            "state": "California",
            "website": "https://www.stanford.edu",
            "domain": "stanford.edu",
            "address": "450 Jane Stanford Way, Stanford, CA 94305",
            "extraction_date": "2024-01-15",
            "query_found": True,
            "phone": "+1-650-723-2300",
            "email": "info@stanford.edu",
            "type": "University",
            "status": "Active",
            "founded": "1885",
            "programs": ["Engineering", "Business", "Medicine", "Law", "Education"]
        },
        {
            "id": 10000387,
            "name": "University of Oxford",
            "country": "GB",
            "city": "Oxford",
            "state": "Oxfordshire",
            "website": "https://www.ox.ac.uk",
            "domain": "ox.ac.uk",
            "address": "University Offices, Wellington Square, Oxford OX1 2JD",
            "extraction_date": "2024-01-15",
            "query_found": True,
            "phone": "+44-1865-270000",
            "email": "enquiries@admin.ox.ac.uk",
            "type": "University",
            "status": "Active",
            "founded": "1096",
            "programs": ["Liberal Arts", "Sciences", "Medicine", "Law", "Engineering"]
        }
    ]
    
    # Demonstrate the extractor
    extractor = SheerIDExtractor()
    
    print("SheerID Extractor - Simplified Output Demo")
    print("=" * 50)
    
    # Process the institutions
    simplified_data = extractor.process_institutions(sample_comprehensive_data)
    
    print("\nOriginal comprehensive record example:")
    print(json.dumps(sample_comprehensive_data[0], indent=2))
    
    print("\nSimplified output:")
    for record in simplified_data:
        print(json.dumps(record, indent=2))
    
    print(f"\nProcessing Statistics:")
    stats = extractor.get_stats()
    for key, value in stats.items():
        print(f"  {key}: {value}")
    
    # Save to file
    extractor.save_to_file("institutions_simplified.json")
    
    print(f"\nFile size reduction:")
    original_size = len(json.dumps(sample_comprehensive_data))
    simplified_size = len(json.dumps(simplified_data))
    reduction_percent = ((original_size - simplified_size) / original_size) * 100
    print(f"  Original size: {original_size} bytes")
    print(f"  Simplified size: {simplified_size} bytes")
    print(f"  Reduction: {reduction_percent:.1f}%")