import os ,json ,sys



def get_disk_usage():
    lis=[]
    try:
        input_directory = sys.argv[1]
    except Exception as e:
        print(e.__doc__)
        print("Oops!No argument||Please pass a directory name.")
    try:
        files = os.listdir(input_directory)
        for file_name in files:
            fullpath = input_directory + "/" + file_name
            if os.path.isfile(fullpath):
                file_size = os.path.getsize(fullpath)
                lis.append([fullpath,file_size])
        newdict = {'files':lis}
        print(json.dumps(newdict))
    except Exception as e:
        print(e.__doc__)
        print("Oops!Wrong path||Please enter a valid path.")


get_disk_usage()

