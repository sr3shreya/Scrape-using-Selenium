############################################################
############################################################
import json
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Scrape:
    def __init__(self, driver):
        self.driver = driver
        # self.link=[]
    def my_scrape(self):
        links = []
        self.driver.maximize_window()
        self.driver.get("https://www.hcltech.com/careers/Careers-in-india")
        headings = []
        output_data = []
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, 'table')))
        for heading in self.driver.find_element_by_tag_name('table').find_element_by_tag_name("thead").find_elements_by_tag_name("th"):
            headings.append(heading.text.strip())
        headings.append("LINK")
        for row in self.driver.find_element_by_tag_name('table').find_element_by_tag_name("tbody").find_elements_by_tag_name("tr"):
            designation = ''
            job_link = ''
            date = ''
            location = ''
            exp = ''
            for data in row.find_elements_by_tag_name("td"):
                if 'designation' in data.get_attribute("class"):
                    designation = data.text
                    job_link = data.find_element_by_tag_name("a").get_attribute("href")
                    links.append(job_link)
                if 'date' in data.get_attribute("class"):
                    date = data.text
                if 'location' in data.get_attribute("class"):
                    location = data.text
                if 'experience' in data.get_attribute("class"):
                    exp = data.text
            output_data.append([designation, date, location, exp, job_link])
        df = pd.DataFrame(output_data, columns=headings)
        mydata = json.loads(df.to_json())
        result = json.dumps(mydata, indent=4)
        print(result)
        return links

    def link_scrape(self, links):
        output_data_1 = []
        for i in links:
            driver.get(i)
            headings_1 = ['jobs-location','jobs-designation', 'jobs-qualification', 'jobs-skills', 'jobs-experience', 'jobs-positions']
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'container')))
            jobs_location = ''
            jobs_designation = ''
            job_qualification = ''
            job_skills = ''
            job_experience = ''
            job_positions = ''
            for data in self.driver.find_elements_by_xpath('//*[@id="training-hiring-programs"]/div[2]/div/div'):
                if 'jobs-location' in data.get_attribute("class"):
                    jobs_location = data.text.replace("LOCATION:","").replace("\n","")
                if 'jobs-designation' in data.get_attribute("class"):
                    jobs_designation = data.text.replace("DESIGNATION:","").replace("\n","")
                if 'jobs-qualification' in data.get_attribute("class"):
                    job_qualification = data.text.replace("QUALIFICATION:","").replace("\n","")
                if 'jobs-skills' in data.get_attribute("class"):
                    job_skills = data.text.replace("SKILLS:","").replace("\n","")
                    #print(job_skills)
                if 'jobs-experience' in data.get_attribute("class"):
                    job_experience = data.text.replace("EXPERIENCE:","").replace("\n","")
                if 'jobs-positions' in data.get_attribute("class"):
                    job_positions = data.text.replace("NO. OF POSITIONS:","").replace("\n","")
            output_data_1.append([jobs_location,jobs_designation, job_qualification, job_skills, job_experience, job_positions])
        df1 = pd.DataFrame(output_data_1, columns=headings_1)
        mydata1 = json.loads(df1.to_json())
        result1 = json.dumps(mydata1, indent=4)
        print(result1)
        #df1.to_csv('output.csv', index=False)
        return df1


driver_path = 'C:/Users/shreya_s/bin/chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)
S1 = Scrape(driver)
links = S1.my_scrape()
df = S1.link_scrape(links)
