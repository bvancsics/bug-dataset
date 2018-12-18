import subprocess as sp
import os



def get_test_results(testMap, perTest_result):
    results = {}
    with open(perTest_result, "r") as infile:
        for line in infile:
            if line.count("result;id") == 0:
                if line.count(": ") > 0:
                    line = line.split("\n")[0]
                    results[line.split(": ")[1]] = line.split(": ")[0]
                if line.count(";") > 0:
                    line = line.split("\n")[0]
                    results[line.split(";")[1]] = line.split(";")[0]

    test_map = {}
    with open(testMap, "r", encoding='utf-8') as infile:
        for line in infile:
            line = line.split("\n")[0]
            if line.count("id@@@test_name"):
                pass
            else:
                test_map[line.split("@@@")[0]] = line.split("@@@")[1]

    testname_results = {}
    for test, result in results.items():
        testname_results[test_map[test]] = result
    return testname_results


def tests_comapre(buggy, fixed):
    skipped_test_names = set()
    for test, result in fixed.items():
        if test in buggy.keys():
            if str(result).upper() == "FAIL" and str(buggy[test]).upper() == "FAIL":
                print(test)
                skipped_test_names.add(test)
            elif str(result).upper() == "FAIL" and str(buggy[test]).upper() == "PASS":
                print("fixed:FAIL;buggy:PASS;" + str(test))
            elif str(result).upper() == "PASS" and str(buggy[test]).upper() == "FAIL":
                print("fixed:PASS;buggy:FAIL;" + str(test))
        else:
            print("uj teszt a fixed-ben;" + str(test))
    return skipped_test_names


def write_skipped_list(skipped_test_names, testMap, output_file):
    test_map = {}
    with open(testMap, "r", encoding='utf-8') as infile:
        for line in infile:
            line = line.split("\n")[0]
            if line.count("id@@@test_name"):
                pass
            else:
                test_map[line.split("@@@")[1]] = line.split("@@@")[0]

    skipped_file = open(output_file, "w")
    for skipped in skipped_test_names:
        skipped_file.write(test_map[skipped] + "\n")
    skipped_file.close()


def get_skipped_tests(buggy_testMap, buggy_perTest, fixed_o_t_testMap, fixed_o_t_perTest):
    buggy_testname_results = get_test_results(buggy_testMap, buggy_perTest)
    fixed_testname_results = get_test_results(fixed_o_t_testMap, fixed_o_t_perTest)
    skipped_test_names = tests_comapre(buggy_testname_results, fixed_testname_results)
    write_skipped_list(skipped_test_names, fixed_o_t_testMap, fixed_o_t_perTest+"_skipped.txt")