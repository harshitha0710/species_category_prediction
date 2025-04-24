import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open the IUCN Red List search page
driver.get("https://www.iucnredlist.org/search/grid?taxonLevel=Amazing&searchType=species")
time.sleep(2)

# Perform the initial search
driver.find_element(By.XPATH, "//input[@class='search search--site']").send_keys("animals")
driver.find_element(By.XPATH, "//button[@class='search--site__button search-formbutton']").click()
time.sleep(3)

# Select the initial filters
driver.find_element(By.XPATH, "//label[@for='taxonLevel-Amazing']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//li[14]//h3").click()

# Select population trend filters
for trend_id in ["populationTrend-2", "populationTrend-1", "populationTrend-0"]:
    element = driver.find_element(By.XPATH, f"//input[@id='{trend_id}']")
    driver.execute_script("arguments[0].click();", element)

# Apply the marine regions filters
marine_regions_section = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//li//h3[contains(text(), 'Marine Regions')]"))
)
marine_regions_section.click()

marine_filters = [
    "marineRegions-18",  # Arctic
    "marineRegions-31",  # Atlantic
    "marineRegions-58",  # Indian Ocean
    "marineRegions-88",  # Pacific (Asian)
    "marineRegions-67"   # Pacific (North)
]

for marine_filter in marine_filters:
    element = driver.find_element(By.XPATH, f"//input[@id='{marine_filter}']")
    driver.execute_script("arguments[0].click();", element)
    time.sleep(2)

# Click "Show More" until all results are loaded
while True:
    try:
        show_more = driver.find_element(By.XPATH, "//a[@class='section__link-out']")
        driver.execute_script("arguments[0].click();", show_more)
        time.sleep(3)
    except NoSuchElementException:
        break

# Extract species links
list1 = driver.find_elements(By.XPATH, "//a[@class='link--faux']")

# Extract generation lengths
lengths = []
for link in list1:
    link_url = link.get_attribute("href")
    driver.execute_script("window.open(arguments[0],'_blank');", link_url)
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(3)

    try:
        len1 = driver.find_element(By.XPATH, "(//article[@id='habitatecology']//div//div[@class='layout-card--split__minor'])[2]/p[1]")
        years = len1.text.split(" ")[0]
        if "-" in years:
            x, y = map(float, years.split("-")[0:2])
            lengths.append((x + y) / 2)
        else:
            lengths.append(float(years))
    except NoSuchElementException:
        lengths.append("N/A")

    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(2)

# Save generation lengths to CSV
with open('red_genlen.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    for data in lengths:
        writer.writerow([data])

# Extract threats
threats = []
for link in list1:
    link_url = link.get_attribute("href")
    driver.execute_script("window.open(arguments[0],'_blank');", link_url)
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(3)

    try:
        threat_elements = driver.find_elements(By.XPATH, "//article[@id='threats']/div/div/h3")
        threats.append(len(threat_elements))
    except NoSuchElementException:
        threats.append("N/A")

    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(2)

# Save threats to CSV
with open('marine_threats.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    for data in threats:
        writer.writerow([data])

# Extract categories
categories = []
category_elements = driver.find_elements(By.XPATH, "//header[@class='card__header']/span")
for element in category_elements:
    categories.append(element.text.split("-")[1].split("\n")[0])

# Save categories to CSV
with open('marine_category.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    for data in categories:
        writer.writerow([data])

# Extract habitats
habitats = []
for link in list1:
    link_url = link.get_attribute("href")
    driver.execute_script("window.open(arguments[0],'_blank');", link_url)
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(3)

    try:
        habitat = driver.find_element(By.XPATH, "(//p[@class='panel__data panel__data--key'])[2]")
        habitats.append(habitat.text.split(",")[0])
    except NoSuchElementException:
        habitats.append("N/A")

    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(2)

# Save habitats to CSV
with open('marine_habitats1.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    for data in habitats:
        writer.writerow([data])

time.sleep(20)
driver.quit()
