import sys
import time
import string

from extenderr import *
def er_msg():
    mes = "incorrect command line!\n" \
          "  Waited:\n" \
          "\tcommand -f infile outfile01 outfile02\n" \
          "  Or:\n" \
          "\tcommand -n number outfile01 outfile02\n"
    print(mes)
def er_msg1():
    mes = "incorrect file!\n"
    print(mes)
#----------------------------------------------
if __name__ == '__main__':
    if len(sys.argv) != 5:
       er_msg()
       exit()

    print('==> Start')
    startTime = time.time()
    if sys.argv[1] == "-f":
        inputFileName = sys.argv[2]
        outputFileName = sys.argv[3]
        sortedOutputFileName = sys.argv[4]

        # Чтение исходного файла, содержащего данные, разделенные пробелами и переводами строки

        ifile = open(inputFileName)
        str = ifile.read()
        ifile.close()
        # Формирование массива строк, содержащего чистые данные в виде массива строк символов.
        strArray = str.replace("\n", " ").split(" ")
        container = Container()
        figNum = container.file_in(strArray)
        if(figNum==0):
            er_msg1()
            exit()
    elif sys.argv[1] == "-n":
        outputFileName = sys.argv[3]
        sortedOutputFileName = sys.argv[4]
        container = Container()
        container.random_in(int(sys.argv[2]))

    ofile = open(outputFileName, 'w')
    container.Write(ofile)
    ofile.close()

    container.Sort();
    sofile = open(sortedOutputFileName, 'w')
    sofile.write("Sorted container\n")
    container.Write(sofile)
    sofile.close()

    print('==> Finish')
    print(round(time.time() - startTime, 7), " seconds")
