
"""# imports"""

import random
import time
import os
import requests
import time
import csv
from bs4 import BeautifulSoup
import re
import pandas as pd
import gdown

list_agents=[
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 OPR/101.0.0.0',
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.31',
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.76',
 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
 "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.61",
 "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"]

"""# Grap the input data and handle it"""

# link to your Google Drive file
google_drive_link = 'https://drive.google.com/drive/folders/1ltdsXAS_zaZ3hI-q9eze_QCzHciyYAJY'
gdown.download_folder(google_drive_link, quiet=True, use_cookies=False)

# path of your Excel file
excel_file_path = '20211030 Test Assignment/Input.xlsx'

# desired name for the CSV file
csv_file_path = 'output.csv'

# Read Excel file into a pandas DataFrame
df = pd.read_excel(excel_file_path)

# Save DataFrame to a CSV file
df.to_csv(csv_file_path, index=False)

print(f'Conversion completed: {excel_file_path} -> {csv_file_path}')

# path of your Excel file
excel_file_path = '20211030 Test Assignment/Output Data Structure.xlsx'

# desired name for the CSV file
csv_file_path = 'structure.csv'

# Read Excel file into a pandas DataFrame
df = pd.read_excel(excel_file_path)

# Save DataFrame to a CSV file
df.to_csv(csv_file_path, index=False)

print(f'Conversion completed: {excel_file_path} -> {csv_file_path}')

directory = '20211030 Test Assignment/StopWords'

# Specify the output file name
output_file = 'Stopwordsall.txt'

def process_file(file_path):
    with open(file_path, 'r', encoding='latin-1') as file:
        lines = file.readlines()
        return [line.split('|')[0].strip() for line in lines]

def combine_files(input_directory, output_file_name):
    result_lines = []
    for filename in os.listdir(input_directory):
        if filename.endswith('.txt'):
            file_path = os.path.join(input_directory, filename)
            result_lines.extend(process_file(file_path))

    with open(output_file_name, 'w', encoding='utf-8') as output_file:
        output_file.write('\n'.join(result_lines))

# Call the function to combine files
combine_files(directory, output_file)

print(f'Files combined and saved to: {output_file}')

"""#web scrap the data"""

def clean_text(input_text, allowed_chars= ['-', "'", ' ']):
    # Define a regex pattern to match any character not in the allowed list
    pattern = f'[^a-zA-Z0-9 {" ".join(re.escape(char) for char in allowed_chars)}]'

    # Use re.sub to replace the matched characters with an empty string
    cleaned_text = re.sub(pattern, '', input_text)

    # Replace consecutive spaces with a single space
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text)

    # Remove non-alphanumeric characters and extra whitespaces
    cleaned_text = re.sub(r'[^a-zA-Z0-9\s]', '', cleaned_text)

    return cleaned_text.strip()

# Example usage:
text_to_clean = "This is a text's with!@# $ special characters and spaces."


cleaned_result = clean_text(text_to_clean)

print(cleaned_result)

class init_url():
  def __init__(self, title,text):
      self.title = title
      self.text = text

class urls_csv_info():

  def __init__(self, csv,file_name):
      self.csv = csv
      #self.wd=wd
      self.file_=file_name
      self.tables = []
      self.url_links = []
      self.init_urls=[]
      self.fail_list=[]
  def url_one_link(self,link):
    user_agent= random.choice(list_agents)
    headers = {
        "authority": "insights.blackcoffer.com",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "en-GB,en;q=0.9,en-US;q=0.8",
        "cache-control": "max-age=0",
        "sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="120", "Microsoft Edge";v="120"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "cross-site",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent":  user_agent
    }
    response = requests.get(link, headers=headers)
    if response.status_code==200:
      self.tables.append(response.content.decode())
      self.url_links.append(link)
    else:
      print("fail",link)
      if response.status_code==404:
        print("we skiped 404")
        self.fail_list.append(link)
      else:
        print("try again")
        self.url_one_link(link)

  def articals_link(self):

    csv_file_path = self.csv
    # Read CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file_path)
    # Loop through the rows of the DataFrame
    counter=0
    for index, row in df.iterrows():
        url = row['URL']
        self.url_one_link(url)
        time.sleep(random.choice([0.1,0.3,0.5,0.7]))
        if counter%20==0:
          print("counter",counter)
        counter+=1
      #self.url_one_link(self.link+"&page="+str(i+1))



  def get_print_articals(self):
    for ind in ob.tables:

      soup = BeautifulSoup(ind, 'html.parser')
      title_element = soup.select('h1[class="entry-title"]')
      if len(title_element)==0:
        title_element = soup.select('h1[class="tdb-title-text"]')
      title_text = title_element[0].get_text(strip=True)
      #print("found titel ",title_text)

      eligible_divs = soup.select('div:has(> p), div:has(> ul)')

      # Find the div with the maximum text size
      max_size_div = None
      max_text_size = 0

      for div in eligible_divs:
          text_size = len(div.get_text(strip=True))
          if text_size > max_text_size:
              max_text_size = text_size
              max_size_div = div
              #tdb-block-inner td-fix-index

      # Extract and print the combined text content of all children
      combined_text = ' '.join(
              child.get_text(strip=True)
              for child in max_size_div.find_all(recursive=False)
              if child.name != 'pre')

      self.init_urls.append(init_url(title_text,combined_text))

  def li_ob_csv(self,name):
    path=""
    csv_file = path+name+".csv"
    # Define the CSV column headers
    fields = ["url","title", "text"]
    # Open the CSV file in write mode and write the header
    with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(fields)
        counter=0
        # Write the data for each product
        for artical in self.init_urls:
            writer.writerow([self.url_links[counter],clean_text(artical.title), clean_text(artical.text)])
            counter+=1
    print(f"CSV file '{csv_file}' created successfully.")


  def get_init_urls_csv(self):
    self.articals_link()
    self.get_print_articals()
    self.li_ob_csv(self.file_)

ob=urls_csv_info("/content/output.csv","data_all")
ob.get_init_urls_csv()

print("list of 404 fails",ob.fail_list)

ob.init_urls[0].text

"""#NLP ANALYSIS"""

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk import sent_tokenize, word_tokenize
from nltk.corpus import cmudict  # For syllable count
from textblob import TextBlob

file_path = 'Stopwordsall.txt'
# Read the contents of the file and split lines into a list
with open(file_path, 'r') as file:
    stopwords_list = [line.strip().lower() for line in file]
# Print the resulting list
print(stopwords_list)

file_path = '20211030 Test Assignment/MasterDictionary/negative-words.txt'
# Read the contents of the file and split lines into a list
with open(file_path, 'r',encoding='ISO-8859-1') as file:
    negative_list = [line.strip().lower() for line in file]
# Print the resulting list
print(negative_list)

file_path = '20211030 Test Assignment/MasterDictionary/positive-words.txt'
# Read the contents of the file and split lines into a list
with open(file_path, 'r') as file:
    positive_list = [line.strip().lower() for line in file]
# Print the resulting list
print(positive_list)

# for stopwords
nltk.download('stopwords')
#for Tokenization
nltk.download('punkt')
nltk.download('cmudict')

#test
print("test")
cmudict_dict=cmudict.dict()
def tokenize_text(text):
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text)
    filtered_tokens = [word.lower() for word in words if word.lower() not in stop_words]
    return  [word for word in filtered_tokens if word.lower() not in stopwords_list]

def positive_score_(text):
  filtered_tokens=tokenize_text(text)
  positive_score = sum(1 for token in filtered_tokens if token in positive_list)
  return positive_score

def negative_score_(text):
  filtered_tokens=tokenize_text(text)
  negative_score = sum(1 for token in filtered_tokens if token in negative_list)
  return negative_score

def polarity_subjectivity(text):
    sentiment=TextBlob(text).sentiment
    #      polarity     subjectivity
    return sentiment[0],sentiment[1]

def avg_sentence_length(text):
    sentences = sent_tokenize(text)
    return sum(len(tokenize_text(sentence)) for sentence in sentences) / len(sentences)

def percentage_of_complex_words(text):
    words = tokenize_text(text)
    complex_words = [word for word in words if syllable_count(word) >= 3]  # Assuming 3 or more syllables is complex
    return (len(complex_words) / len(words)) * 100 if len(words) > 0 else 0

def fog_index(average_sentence_length, percentage_of_complex_words):
    return 0.4 * (average_sentence_length + percentage_of_complex_words)

def avg_words_per_sentence(text):
    sentences = sent_tokenize(text)
    return len(tokenize_text(text)) / len(sentences) if len(sentences) > 0 else 0

def complex_word_count(text):
    words = tokenize_text(text)
    return len([word for word in words if syllable_count(word) >= 3])  # Assuming 3 or more syllables is complex

def word_count(text):
    words = tokenize_text(text)
    return len(words)

def syllable_count(word):
    d = cmudict_dict
    return max([len(list(y for y in x if y[-1].isdigit())) for x in d[word.lower()]]) if word.lower() in d else 0

def personal_pronouns(text):
    words = tokenize_text(text)
    pronouns = [word.lower() for word in words if word.lower() in ['i', 'me', 'my', 'mine', 'myself', 'we', 'us', 'our', 'ours', 'ourselves']]
    return len(pronouns)

def avg_word_length(text):
    words = tokenize_text(text)
    return sum(len(word) for word in words) / len(words) if len(words) > 0 else 0

# Sample text
text = ob.init_urls[0].text
print(text)

# Calculate linguistic features
positive_score=positive_score_(text)
negative_score=negative_score_(text)
polarity,subjectivity=polarity_subjectivity(text)
avg_sentence_len = avg_sentence_length(text)
percentage_complex_words = percentage_of_complex_words(text)
fog_idx = fog_index(avg_sentence_len, percentage_complex_words)
avg_words_per_sent = avg_words_per_sentence(text)
complex_word_cnt = complex_word_count(text)
total_word_cnt = word_count(text)
syllables_per_word = sum(syllable_count(word) for word in tokenize_text(text)) / total_word_cnt if total_word_cnt > 0 else 0
pronoun_count = personal_pronouns(text)
avg_word_len = avg_word_length(text)

# Print the results
print(f'positive score: {positive_score}')
print(f'negative score: {negative_score}')
print(f'polarity score: {polarity}')
print(f'subjectivity score: {subjectivity}')
print(f'Average Sentence Length: {avg_sentence_len}')
print(f'Percentage of Complex Words: {percentage_complex_words}%')
print(f'FOG Index: {fog_idx}')
print(f'Average Words per Sentence: {avg_words_per_sent}')
print(f'Complex Word Count: {complex_word_cnt}')
print(f'Total Word Count: {total_word_cnt}')
print(f'Syllables per Word: {syllables_per_word}')
print(f'Personal Pronoun Count: {pronoun_count}')
print(f'Average Word Length: {avg_word_len}')

file_path = 'data_all.csv'
# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Iterate over the DataFrame rows
for index, row in df.iterrows():
  #text
  text = row["title"]+" "+row["text"]
  #factors
  print("-----------------------")
  print(row["title"])
  positive_score=positive_score_(text)
  negative_score=negative_score_(text)
  polarity,subjectivity=polarity_subjectivity(text)
  avg_sentence_len = avg_sentence_length(text)
  percentage_complex_words = percentage_of_complex_words(text)
  fog_idx = fog_index(avg_sentence_len, percentage_complex_words)
  avg_words_per_sent = avg_words_per_sentence(text)
  complex_word_cnt = complex_word_count(text)
  total_word_cnt = word_count(text)
  syllables_per_word = sum(syllable_count(word) for word in tokenize_text(text)) / total_word_cnt if total_word_cnt > 0 else 0
  pronoun_count = personal_pronouns(text)
  avg_word_len = avg_word_length(text)
  print(total_word_cnt)
  print("-----------------------")
  features = {
    'Positive Score': positive_score,
    'Negative Score': negative_score,
    'Polarity Score': polarity,
    'Subjectivity Score': subjectivity,
    'Average Sentence Length':avg_sentence_len,
    'Percentage of Complex Words': percentage_complex_words,
    'FOG Index': fog_idx,
    'Average Words per Sentence': avg_words_per_sent,
    'Complex Word Count': complex_word_cnt,
    'Total Word Count': total_word_cnt,
    'Syllables per Word': syllables_per_word,
    'Personal Pronoun Count': pronoun_count,
    'Average Word Length': avg_word_len}
    # Update each column based on the calculated features
  for feature, value in features.items():
    df.at[index, feature] = value

# Display the updated DataFrame
print(df)

df.columns

file_path = 'output.csv'
# read the CSV file into a DataFrame
df_main = pd.read_csv(file_path)
df_main.columns

file_path = 'structure.csv'
# read the CSV file into a DataFrame
structure = pd.read_csv(file_path)
structure.columns

merged_df = pd.merge(df_main, df, left_on='URL', right_on='url', how='left')
# if the website did not exist then it fall under 404 requests , and we fell all records by 404
merged_df.fillna("404", inplace=True)

# drop the redundant 'url' column
merged_df.drop('url', axis=1, inplace=True)
merged_df.drop('title', axis=1, inplace=True)
merged_df.drop('text', axis=1, inplace=True)
merged_df.columns=structure.columns
merged_df.to_csv("output_results.csv", index=False)
merged_df
