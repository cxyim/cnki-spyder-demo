import sys
sys.path.append(".")
import cnki_spyder_tool as cnki
from pprint import pprint as fprint

if __name__ == "__main__":

    input_file = open("../data/doc_url/2_copy.txt","r",encoding="utf-8")
    
    while True:  
        res_file = open("../data/res_csv/2_res.csv","a",encoding="utf-8")
        line = input_file.readline()
        if not line:
            break
        cnki.get_doc_bibilo(line.strip(),res_file)    
        res_file.close()
