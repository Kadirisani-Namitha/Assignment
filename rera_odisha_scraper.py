import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_driver_path = r"C:\Users\kadir\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"
service = Service(executable_path=chrome_driver_path)
options = webdriver.ChromeOptions()
# options.add_argument("--headless")  # Uncomment if you want no browser UI

driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 15)

# List your project URLs here
project_urls = [
    "https://rera.odisha.gov.in/projects/project-details/VTJGc2RHVmtYMTlpTWZ3NlplSWhhRjFJOXU1enRkY2N5czd2c3dwcUtUVVZmK1hYMlRsdHdkSEI5NnlVQmpHT2lHTlhUOUtsSjVDdHhPd2s3MFNLK2hnMytWWVVMczhabTFhMmRlTW9PV289",
    # Add more URLs here
]

all_projects = []
fieldnames = set()  # To dynamically track all keys (columns)

try:
    for url in project_urls:
        driver.get(url)

        project_name_element = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "h3.card-title.project-title"))
        )
        project_name = project_name_element.text

        table_rows = driver.find_elements(By.CSS_SELECTOR, "table.table-bordered tbody tr")

        details = {"Project Name": project_name}
        for row in table_rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            if len(cells) == 2:
                key = cells[0].text.strip().replace(":", "")
                value = cells[1].text.strip()
                details[key] = value

        all_projects.append(details)
        fieldnames.update(details.keys())

    # Write all projects to CSV
    with open("rera_multiple_projects.csv", "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=list(fieldnames))
        writer.writeheader()
        writer.writerows(all_projects)

    print(f"Scraped {len(all_projects)} projects. Saved to rera_multiple_projects.csv")

except Exception as e:
    print("Error:", e)

finally:
    driver.quit()
