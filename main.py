
import subprocess as sp
import test_results
import data_copy
import os



cwd = os.getcwd()
os.chdir(cwd)


for x in range(1, 5):
    project = "Shields"  # <--- itt megadod a projekt nevet (azt ami a Projects.cs-ben van)
    subfolder = "shields" # <--- itt megadod a github-os projekt nevet

    # ezekbe a mappakba lesznek gyujtve a meresek
    buggy_folder = "./"+str(project)+"_"+str(x)+"_buggy"
    changes_folder = "./"+str(project)+"_"+str(x)+"_changes"
    fixed_folder = "./"+str(project)+"_"+str(x)+"_fixed"
    fixed_o_t_folder = "./"+str(project)+"_"+str(x)+"_fixed-only-test-change"
    new_data_folder = "./"+str(project)+"_" + str(x) + "_data"


    # ezek a 'netto meresek'
    sp.call("python3 main_bugsjs.py -p "+project+" -b "+str(x)+" -t test -v buggy -o "+changes_folder, shell=True)
    os.chdir(cwd)
    sp.call("python3 main_bugsjs.py -p "+project+" -b "+str(x)+" -t test -v fixed -o "+fixed_folder, shell=True)
    os.chdir(cwd)
    sp.call("python3 main_bugsjs.py -p "+project+" -b "+str(x)+" -t per-test -v buggy -o "+buggy_folder, shell=True)
    os.chdir(cwd)
    sp.call("python3 main_bugsjs.py -p "+project+" -b "+str(x)+" -t per-test -v fixed-only-test-change -o "+fixed_o_t_folder, shell=True)
    os.chdir(cwd)


    try:
        # elkeszitunk egy listat azokrol a metodusokrol, amelyek a hibas es a fixalt verzioban is buknak
        # ezek a bug szempontjabol irrelevans buko tesztek
        buggy_testMap = buggy_folder+"/"+str(subfolder)+"/testMap.csv"
        buggy_perTest = buggy_folder+"/"+str(subfolder)+"/perTest_results.txt"
        fixed_o_t_testMap = fixed_o_t_folder+"/"+str(subfolder)+"/testMap.csv"
        fixed_o_t_perTest = fixed_o_t_folder+"/"+str(subfolder)+"/perTest_results.txt"
        test_results.get_skipped_tests(buggy_testMap, buggy_perTest, fixed_o_t_testMap, fixed_o_t_perTest)

        # osszegyujtjuk az adatokat a _data mappaba, hogy kesobb konnyebb legyen azokat felhasznalni/feldolgozni
        data_copy.create_data_folders(new_data_folder)
        data_copy.test_coverage_copy(fixed_o_t_folder+"/"+str(subfolder), new_data_folder)
        data_copy.result_copy(fixed_o_t_folder+"/"+str(subfolder), new_data_folder)
    except:
        pass



