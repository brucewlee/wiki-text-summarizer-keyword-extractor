# Wikipedia summarizer
import bs4 as bs  
import urllib.request  
import re
from gensim.summarization import summarize as su_gs
from gensim.summarization import keywords
from gensim.summarization import mz_keywords
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
from sys import argv
import os

def print_usage():
    # Display the parameters and what they mean.
    print('''
    Usage:
        summarize.py <wiki-url> <summary length>

    Explanation:
        Parameter 1: Wikipedia URL to pull
        Parameter 2: the number of words for the summary to contain
    ''')

def summarize(url_topull, num_of_words):
    # Obtain text
    scraped_data = urllib.request.urlopen(url_topull)  
    article = scraped_data.read()
    parsed_article = bs.BeautifulSoup(article,'lxml')
    paragraphs = parsed_article.find_all('p')
    article_text = ""
    for p in paragraphs:  
        article_text += p.text

    # Extract keywords
    stop_words = set(stopwords.words('english')) 
    keywords = mz_keywords(article_text,scores=True,threshold=0.003)
    keywords_names = []
    for tuples in keywords:
        if tuples[0] not in stop_words: 
            if len(tuples[0]) > 2:
                keywords_names.append(tuples[0])

    # Create summary
    pre_summary = su_gs(article_text,word_count=num_of_words)
    summary = re.sub("[\(\[].*?[\)\]]", "", pre_summary)

    # Print
    print_pretty (summary,keywords_names)

def print_pretty (summary, keywords_names):
    columns = os.get_terminal_size().columns
    print ("=" * columns)
    print ("wiki-summarizer-----written-by-@brucewlee(github)".center(columns))
    print ("-" * columns)
    printable = summary
    print (printable.center(columns))
    print ("-" * columns)
    str_keywords_names = str(keywords_names).strip('[]')
    printable2 = str_keywords_names
    print (printable2.center(columns))
    print ("=" * columns)

if __name__ == '__main__':
    if len(argv) != 3:
        print_usage()
    elif not str(argv[2]).isdigit():
        print_usage()
    else:
        summarize(argv[1], int(argv[2]))