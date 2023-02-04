
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from datetime import datetime
import sqlite3



def save_data(youtube,twitter,instagram):
    
    record ={
        'date': datetime.now(),
        'youtube' : youtube,
        'twitter' : twitter,
        'instagram' : instagram
    }
    
    # Connect to the Database
    con = sqlite3.connect('followers.db')
    cur = con.cursor()

    cur.execute('''
                  CREATE TABLE IF NOT EXISTS monthly_stats (
                  date INTEGER, youtube TEXT, twitter TEXT, instagram TEXT
                  )
                ''')

    insert = cur.execute(
                'INSERT INTO monthly_stats VALUES ("%s", "%s", "%s", "%s")' % (
                record['date'], record['youtube'], record['twitter'], record['instagram']
                        )
    )

    con.commit()
    con.close()


    



#setup webdriver
options=Options()
options.add_argument('--headless')
driver=webdriver.Firefox(executable_path='./geckodriver.exe', options=options)
driver.implicitly_wait(10)

#Youtube
driver.get('https://www.youtube.com/@TheHarshBeniwal')
youtube_count = driver.find_element(By.ID, 'subscriber-count').text.split(' ')[0]



#Twitter
driver.get('https://twitter.com/iamharshbeniwal')
twitter_count = driver.find_element(By.CSS_SELECTOR, 'a[href="/iamharshbeniwal/followers"] > span > span').text


#Instagram
driver.get('https://www.picuki.com/profile/harshbeniwal')
instagram_count = driver.find_element(By.CSS_SELECTOR, '.followed_by').text


#Close Webdriver
driver.close()

# Save the data
save_data(youtube_count,twitter_count,instagram_count)

