#python 2.7.12

import os
import string

def fetch_dir_list(root_dir):
    if len(root_dir) <= 0: 
        raise Exception('Invalid input directory name: {}'.format(root_dir))

    files = os.listdir(root_dir)
    #file_list = []
    file_list = [file for file in files if os.path.isfile(os.path.join(root_dir,file))] 
    
    # for file in files:
    #     if os.path.isdir(os.path.join(root_dir, file)):
    #         file_list.append(file)
    #     else:
    #         print '{0} is not a directory..'.format(file)
    print file_list

def fetch_file_list(root_dir):
    file_list = []
    if os.path.isfile(root_dir):
        file_list.append(root_dir)
        return file_list

    files = os.listdir(root_dir)
    for file in files:
        file_list.extend(fetch_file_list(os.path.join(root_dir, file)))

    return file_list

def copy_dir(source_dir, dest_dir):
    if(len(source_dir) <= 0 or len(dest_dir) <= 0):
        raise Exception('Invalid source or destination directory..')

    os.mkdir(dest_dir)
    files = os.path.listdir(source_dir)

    for file in files:
        if os.path.isfile(source_dir):
            copy_file(source_dir, dest_dir)

def copy_file(source_file, dest_file):
    if(len(source_file) <= 0 or len(dest_file) <= 0):
        raise Exception('Invalid source or destination file..')

    try:
        src = open(source_file, "r")
        dest = open(dest_file, "w")

        contents = src.read()
        dest.write(contents)
        src.close()
        dest.close()
    except Exception as e:
        raise Exception('Failed to copy file {0}. Error: {1}'.format(source_file, e.message))

def remove_dir_recursive(root_dir):
    print os.listdir(root_dir)

    files = os.listdir(root_dir)
    for file in files:
        if os.path.isfile(file): return
        else:
            print 'Directory: ', file
            remove_dir_recursive(file)

        #else:
            #print 'Removing file: ', file
            #os.unlink(file)

        #os.rmdir(file)
        #print 'Removing directory: ', file
    return

def main():

    dest_dir = '/Users/vg2/samples1'
    remove_dir_recursive(dest_dir)

    # source_dir = '/Users/vg2/samples'
    # dest_dir  = '/Users/vg2/samples1'
    # file_list = fetch_file_list(source_dir)
    # mlist = []

    # for file_name in file_list:
    #     try:
    #         dest_file = string.replace(file_name, source_dir, dest_dir)
    #         if not os.path.exists(os.path.dirname(dest_file)):
    #             try:
    #                 os.makedirs(os.path.dirname(dest_file))
    #             except OSError as exc: # Guard against race condition
    #                 if exc.errno != errno.EEXIST:
    #                     raise

    #         copy_file(file_name, dest_file)
    #         mlist.append('Copy source: {0} destination: {1}  is successful.'.format(file_name, dest_file))

    #     except IOError:
    #         mlist.append('Failed to open file {0}'.format(file_name))
    #     except Exception as e:
    #         mlist.append(e.message)

    # for msg in mlist:
    #     print msg

if __name__ == '__main__':
    main()
