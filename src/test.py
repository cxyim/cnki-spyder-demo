import sys
sys.path.append(".")
import cnki_spyder_tool as cnki
import csv
from pprint import pprint as fprint


if __name__ == "__main__":
    
    input_file = open("../data/sub_userinfo.csv","r",encoding="utf-8")
    csv_reader = csv.reader(input_file,delimiter=",")
    
    author_set = set()
    for row in csv_reader:
        author_name = row[1]
        author_set.add(author_name)

    doc_url_set = set()
    for author_name in author_set:
        doc_url_file = open("../data/doc_url.txt","a",encoding="utf-8")
        tmp = cnki.get_doc_url_set(author_name)
        for url in tmp:
            if url not in doc_url_set:
                doc_url_set.add(url)
                doc_url_file.write(url+"\n")
        doc_url_file.close()
    
        


        
