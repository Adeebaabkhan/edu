# Educational Repository

This repository contains educational tools and utilities.

## SheerID Extractor

The `SheerIDExtractor` class provides simplified processing of educational institution data from SheerID, focusing on extracting only essential fields to reduce file size and complexity.

### Features

- **Simplified Output**: Extracts only 3 essential fields per institution:
  - `id` - Institution identifier  
  - `name` - Institution name
  - `country` - Country code

- **Size Reduction**: Significantly reduces output file size (typically 80%+ reduction) by removing unnecessary metadata

- **Data Validation**: Filters out incomplete records missing required fields

### Usage

```python
from sheerid_extractor import SheerIDExtractor

# Initialize extractor
extractor = SheerIDExtractor()

# Process institution data (with comprehensive fields)
comprehensive_data = [
    {
        "id": 10000158,
        "name": "Galgotias University",
        "country": "IN",
        "city": "Greater Noida",
        "state": "Uttar Pradesh",
        "website": "https://galgotiasuniversity.edu.in",
        # ... many other fields
    }
]

# Get simplified output
simplified_data = extractor.process_institutions(comprehensive_data)

# Result will be:
# [{"id": 10000158, "name": "Galgotias University", "country": "IN"}]

# Save to file
extractor.save_to_file("institutions_simplified.json")
```

### Testing

Run the test suite to validate functionality:

```bash
python test_sheerid_extractor.py
```

### Example Output

The extractor transforms comprehensive institution records into minimal ones:

**Before** (comprehensive record):
```json
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
  "query_found": true,
  "phone": "+91-120-2323000",
  "email": "info@galgotiasuniversity.edu.in",
  "type": "University",
  "status": "Active",
  "founded": "2011"
}
```

**After** (simplified record):
```json
{
  "id": 10000158,
  "name": "Galgotias University",
  "country": "IN"
}
```

This represents an ~86% reduction in file size while maintaining essential identification data.