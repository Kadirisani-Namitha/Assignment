# RERA Odisha Project Scraper

This Python project scrapes the first 6 projects listed under the **Projects Registered** section from the [RERA Odisha website](https://rera.odisha.gov.in/projects/project-list). For each project, it extracts the following details from the project's detail page:

- Rera Registration Number
- Project Name
- Promoter Name (Company Name under Promoter Details tab)
- Address of the Promoter (Registered Office Address under Promoter Details tab)
- GST Number

## Requirements

- Python 3.x
- Selenium
- ChromeDriver (compatible with your installed Chrome browser version)

You can install the Python dependencies with:

```bash
pip install selenium
