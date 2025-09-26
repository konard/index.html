#!/usr/bin/env python3
"""
Test script to verify all navigation links work correctly
"""
import os
import re
from pathlib import Path

def extract_links(html_content):
    """Extract all href links from HTML content"""
    pattern = r'<a\s+href="([^"]+)"'
    return re.findall(pattern, html_content)

def test_navigation():
    """Test all navigation links in HTML files"""
    html_files = ['index.html', 'About.html', 'My_projects.html', 'Kontacts.html']
    base_path = Path('/tmp/gh-issue-solver-1758853808389')

    all_valid = True

    for html_file in html_files:
        file_path = base_path / html_file
        if not file_path.exists():
            print(f"❌ File {html_file} does not exist!")
            all_valid = False
            continue

        print(f"\n📄 Testing {html_file}:")

        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        links = extract_links(content)

        for link in links:
            # Skip external links and anchors
            if link.startswith('http') or link.startswith('#'):
                continue

            # Check if linked file exists
            linked_file = base_path / link
            if linked_file.exists():
                print(f"  ✅ Link to '{link}' is valid")
            else:
                print(f"  ❌ Link to '{link}' is broken (file not found)")
                all_valid = False

    print("\n" + "="*50)
    if all_valid:
        print("✅ All navigation links are working correctly!")
    else:
        print("❌ Some navigation links are broken!")

    return all_valid

if __name__ == "__main__":
    success = test_navigation()
    exit(0 if success else 1)