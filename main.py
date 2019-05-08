import subprocess as sp
import test_results
import data_copy
import os



cwd = os.getcwd()
os.chdir(cwd)


for x in range(1, 2):
    project = "Eslint"
    subfolder = "eslint"

    changes = "./"+str(project)+"_"+str(x)+"_changes"
    buggy_folder = "./"+str(project)+"_"+str(x)+"_buggy"
    #fixed_folder = "./"+str(project)+"_"+str(x)+"_fixed"
    fixed_o_t_folder = "./"+str(project)+"_"+str(x)+"_fixed-only-test-change"
    new_data_folder = "./"+str(project)+"_" + str(x) + "_data"



    sp.call("python3 main_bugsjs.py -p "+project+" -b "+str(x)+" -t test -v buggy -o "+changes, shell=True)
    os.chdir(cwd)

    #sp.call("python3 main_bugsjs.py -p "+project+" -b "+str(x)+" -t test -v fixed -o "+fixed_folder, shell=True)
    #os.chdir(cwd)
    sp.call("python3 main_bugsjs.py -p "+project+" -b "+str(x)+" -t per-test -v buggy -o "+buggy_folder, shell=True)
    os.chdir(cwd)
    sp.call("python3 main_bugsjs.py -p "+project+" -b "+str(x)+" -t per-test -v fixed-only-test-change -o "+fixed_o_t_folder, shell=True)
    os.chdir(cwd)



    try:
        buggy_testMap = buggy_folder+"/"+str(subfolder)+"/testMap.csv"
        buggy_perTest = buggy_folder+"/"+str(subfolder)+"/perTest_results.txt"
        fixed_o_t_testMap = fixed_o_t_folder+"/"+str(subfolder)+"/testMap.csv"
        fixed_o_t_perTest = fixed_o_t_folder+"/"+str(subfolder)+"/perTest_results.txt"
        
        test_results.get_skipped_tests(buggy_testMap, buggy_perTest, fixed_o_t_testMap, fixed_o_t_perTest)


        data_copy.create_data_folders(new_data_folder)
        data_copy.test_coverage_copy(fixed_o_t_folder+"/"+str(subfolder), new_data_folder)
        data_copy.result_copy(fixed_o_t_folder+"/"+str(subfolder), new_data_folder)
    except:
        pass



    # ./rawDataReader -t coverage -m istanbul-js -p /home/user/Asztal/JavaScriptChain/Hessian_1_data/pertest_coverage/ -c /data/Chain/framework-refact/Hessian_1_fixed-only-test-change/hessian.js -o /home/user/Asztal/JavaScriptChain/Hessian_1_data/Hessian_1_pertest.method.cov.SoDA
    # ./rawDataReader -t coverage -m one-test-per-file -p /home/user/Asztal/JavaScriptChain/Hessian_1_data/perchain_coverage/0 -c /data/Chain/framework-refact/Hessian_1_fixed-only-test-change/hessian.js -o /home/user/Asztal/JavaScriptChain/Hessian_1_data/Hessian_1_perchain.method.cov.SoDA
    # ./rawDataReader -t results -m dejagnu-one-revision-per-file -p /home/user/Asztal/JavaScriptChain/Hessian_1_data/result/ -c /data/Chain/framework-refact/Hessian_1_fixed-only-test-change/hessian.js -o /home/user/Asztal/JavaScriptChain/Hessian_1_data/Hessian_1.res.SoDA

    # ./binaryFilter -c /home/user/Asztal/JavaScriptChain/Hessian_1_data/Hessian_1_pertest.method.cov.SoDA --save-coverage /home/user/Asztal/JavaScriptChain/Hessian_1_data/Hessian_1_pertest.filtered.method.cov.SoDA --filter-tests /home/user/Asztal/JavaScriptChain/Hessian_1_data/perTest_results.txt_skipped.txt
    # ./binaryFilter -c /home/user/Asztal/JavaScriptChain/Hessian_1_data/Hessian_1_perchain.method.cov.SoDA --save-coverage /home/user/Asztal/JavaScriptChain/Hessian_1_data/Hessian_1_perchain.filtered.method.cov.SoDA --filter-tests /home/user/Asztal/JavaScriptChain/Hessian_1_data/perTest_results.txt_skipped.txt
    # ./binaryFilter -r /home/user/Asztal/JavaScriptChain/Hessian_1_data/Hessian_1.res.SoDA --save-results /home/user/Asztal/JavaScriptChain/Hessian_1_data/Hessian_1_filtered.res.SoDA --filter-tests /home/user/Asztal/JavaScriptChain/Hessian_1_data/perTest_results.txt_skipped.txt

    # ./fl-score -c /home/user/Asztal/JavaScriptChain/Hessian_1_data/Hessian_1_pertest.method.cov.SoDA -r /home/user/Asztal/JavaScriptChain/Hessian_1_data/Hessian_1.res.SoDA -d /home/user/Asztal/JavaScriptChain/Hessian_1_data/dummy.chg.SoDA -o /home/user/Asztal/JavaScriptChain/Hessian_1_data/fl-method
    # ./fl-score -c /home/user/Asztal/JavaScriptChain/Hessian_1_data/Hessian_1_pertest.filtered.method.cov.SoDA -r /home/user/Asztal/JavaScriptChain/Hessian_1_data/Hessian_1_filtered.res.SoDA -d /home/user/Asztal/JavaScriptChain/Hessian_1_data/dummy.chg.SoDA -o /home/user/Asztal/JavaScriptChain/Hessian_1_data/fl-method-filtered
    # ./fl-score -c /home/user/Asztal/JavaScriptChain/Hessian_1_data/Hessian_1_perchain.method.cov.SoDA -r /home/user/Asztal/JavaScriptChain/Hessian_1_data/Hessian_1.res.SoDA -d /home/user/Asztal/JavaScriptChain/Hessian_1_data/dummy.chg.SoDA -o /home/user/Asztal/JavaScriptChain/Hessian_1_data/fl-chain
    # ./fl-score -c /home/user/Asztal/JavaScriptChain/Hessian_1_data/Hessian_1_perchain.filtered.method.cov.SoDA -r /home/user/Asztal/JavaScriptChain/Hessian_1_data/Hessian_1_filtered.res.SoDA -d /home/user/Asztal/JavaScriptChain/Hessian_1_data/dummy.chg.SoDA -o /home/user/Asztal/JavaScriptChain/Hessian_1_data/fl-chain-filtered
