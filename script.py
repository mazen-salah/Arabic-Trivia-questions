import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import json

start = 3
end = 1865
selector = "#post-body-5532701192554214020 > div:nth-child(1) > div:nth-child({}) > span"
options = uc.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = uc.Chrome(options=options)
driver.get('http://samihamadallah.blogspot.com/2013/02/blog-post_5814.html')

data_list = []

for i in range(start, end+1):
    try:
        text = driver.find_element(By.CSS_SELECTOR, selector.format(i)).text
        question = text.split("؟")[0] + "؟"
        answer = text.split("؟")[1]
        print(question)
        data_dict = {"question": question, "answer": answer}
        data_list.append(data_dict)
    except:
        pass

# Save the data as a JSON file
with open('data.json', 'w', encoding='utf-8') as json_file:
    json.dump(data_list, json_file, ensure_ascii=False, indent=4)

# Close the WebDriver
driver.quit()
