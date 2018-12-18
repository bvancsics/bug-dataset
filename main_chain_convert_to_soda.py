import argparse
import json
import os
import subprocess as sp

# /work/pertest.js -t ./tests.json -r perTest_results.txt -c "istanbul cover --report json-summary node_modules/.bin/_mocha -- --reporter json -t 15000 test/*.test.js" -g "double.test.js should write double 100"

# python3 main_chain_convert_to_soda.py -f /data/Chain/framework/Hessian_1_traces/ -p /data/Chain/framework/Hessian_1_uj/hessian.js/lib -c /data/Chain/jerryscript-tools/callchain-filter.py -o /data/Chain/framework/Hessian_1_chains/0

def arg_parser():
    parser = argparse.ArgumentParser(description = '   ')
    parser.add_argument('-f', '--folder',   required = True, help = 'chains folder')
    parser.add_argument('-p', '--pattern',  required = True, help = 'pattern')
    parser.add_argument('-c', '--chain-filter',  required = True, help = 'chain-filter python script')
    parser.add_argument('-o', '--output',   required = True, help = 'output folder')

    param_dict = {}
    args = parser.parse_args()
    param_dict["folder"] = args.folder
    param_dict["pattern"] = args.pattern
    param_dict["chain-filter"] = args.chain_filter
    param_dict["output"] = args.output
    return param_dict


def get_chain_file_list(folder):
    chai_file_list = set()
    files = [f for f in os.listdir(folder) if os.path.isfile(folder+"/"+f)]

    for f in files:
        if f.count("test_")> 0 and f.count("_trace") > 0:
            chai_file_list.add(folder+"/"+f)
    return list(chai_file_list)



def cleaning(param_dict, chain_file):
    #cmd = "python3 /home/user/Asztal/JavaScriptChain/jerryscript-tools/callchain-filter.py "+chain_file+" + /data/Chain/framework/Hessian_1/hessian.js/lib > "+chain_file+"_cleand.txt"
    cmd = "python3 "+param_dict["chain-filter"]+" "+chain_file+" + "+param_dict["pattern"]+" > "+chain_file+"_cleand.txt"
    sp.call(cmd, shell=True)


def read_chain_txt(cleand_chain_file):
    id_label_map = {}
    with open(cleand_chain_file) as f:
        data = json.load(f)
        for node in data["nodes"]:
            id_label_map[node["id"]] = node["pos"]
    return id_label_map


def get_chains(cleand_chain_file, id_label_map):
    soda_chain_set = set()
    with open(cleand_chain_file) as f:
        data = json.load(f)
        for chain in data["call_chains"]:
            chain = str(chain).replace(",", "")
            chain = str(chain).replace("[", "")
            chain = str(chain).replace("]", "")
            soda_chain_set.add("---".join([id_label_map.get(n, id_label_map[int(n)]) for n in chain.split()]))
    return soda_chain_set


def soda_chains_dump(soda_chain_set, chain_path):
    soda_file = chain_path+"_soda_chain.txt"
    soda_chain_file = open(soda_file, "w")
    for elem in soda_chain_set:
        soda_chain_file.write(str(elem)+",x\n")
    soda_chain_file.close()


def create_output_folder(output, folder):
    if os.path.isdir(output):
        rm_cmd = "rm -R "+str(output)
        sp.call(rm_cmd, shell=True)
    os.makedirs(output)

    files = [f for f in os.listdir(folder) if os.path.isfile(folder+"/"+f)]
    for f in files:
        if f.count("test_")> 0 and f.count("_soda_chain.txt") > 0:
            uj_nev = f.split("_")[0]+"_"+f.split("_")[1]+".txt"
            sp.call("mv "+folder+"/"+f+" "+output+"/"+uj_nev, shell=True)


param_dict = arg_parser()
chai_file_list = get_chain_file_list(param_dict["folder"])


for chain_path in chai_file_list:
    # remove other nodes
    print(chain_path)
    cleaning(param_dict, chain_path)

    # get id-node map
    id_label_map = read_chain_txt(chain_path+"_cleand.txt")

    # get chain set with method names
    soda_chain_set = get_chains(chain_path+"_cleand.txt", id_label_map)

    # dump
    soda_chains_dump(soda_chain_set, chain_path)

create_output_folder(param_dict["output"], param_dict["folder"])