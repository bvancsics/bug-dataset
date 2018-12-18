import before
import subprocess as sp
import test_results
import trace_actions
import data_copy
import os

"""
!!!!!! PATH ----> /data/Chain/node/out/Release:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
export PATH=/data/Chain/node/out/Release:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
"""

"""
os.chdir("/work/")
sp.call("npm i --save glob", shell=True)
os.chdir("/data/Chain/framework")
"""

filter_script = "/data/Chain/jerryscript-tools/callchain-filter.py"

cwd = os.getcwd()
before.settings()
os.chdir(cwd)

for x in range(2, 11):

    project = "Hessian.js"
    buggy_folder = "./Hessian_"+str(x)+"_buggy"
    fixed_o_t_folder = "./Hessian_"+str(x)+"_fixed-only-test-change"
    trace_folder = "./Hessian_" + str(x) + "_traces"
    chain_folder = "./Hessian_" + str(x) + "_chains"
    new_data_folder = "./Hessian_" + str(x) + "_data"


    sp.call("python3 main_bugsjs.py -p "+project+" -b "+str(x)+" -t per-test -v buggy -o "+buggy_folder, shell=True)
    os.chdir(cwd)
    sp.call("python3 main_bugsjs.py -p "+project+" -b "+str(x)+" -t per-test -v fixed-only-test-change -o "+fixed_o_t_folder, shell=True)
    os.chdir(cwd)
    sp.call("python3 main_bugsjs.py -p "+project+" -b "+str(x)+" -t per-chain -v fixed-only-test-change -o "+fixed_o_t_folder, shell=True)
    os.chdir(cwd)



    buggy_testMap = buggy_folder+"/hessian.js/testMap.csv"
    buggy_perTest = buggy_folder+"/hessian.js/perTest_results.txt"
    fixed_o_t_testMap = fixed_o_t_folder+"/hessian.js/testMap.csv"
    fixed_o_t_perTest = fixed_o_t_folder+"/hessian.js/perTest_results.txt"
    test_results.get_skipped_tests(buggy_testMap, buggy_perTest, fixed_o_t_testMap, fixed_o_t_perTest)


    pattern = str(os.path.abspath(fixed_o_t_folder+"/hessian.js/")+"/lib")
    trace_actions.trace_copy(fixed_o_t_folder+"/hessian.js/", trace_folder)
    trace_actions.trace_convert_to_soda(trace_folder, pattern, filter_script, chain_folder)


    data_copy.create_data_folders(new_data_folder)
    data_copy.test_coverage_copy(fixed_o_t_folder+"/hessian.js", new_data_folder)
    data_copy.chain_coverage_copy(chain_folder, new_data_folder)
    data_copy.result_copy(fixed_o_t_folder+"/hessian.js", new_data_folder)
    data_copy.dummy_copy(cwd, new_data_folder)



