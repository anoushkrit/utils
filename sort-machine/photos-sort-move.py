import os
import pandas as pd
import shutil
import datetime


def get_file_details(list_values, name, year, month, date, source, size, current):
    data = {'Filename': name,
            'Year': year,
            'Month': month,
            'Date': date,
            'Size': size,
            'Source': source,
            'Current': current}
    list_values.append(data)
    return list_values


def move_file_type(source_path, dest_path):
    if not os.path.isdir(dest_path):
        os.mkdir(dest_path)
    else:
        pass
    for folderName, subFolders, fileNames in os.walk(source_path):
        for filename in fileNames:
            try:
                shutil.move(os.path.join(folderName, filename), dest_path)
            except:
                continue
            print(os.path.join(folderName, filename))


def image_date_sort(source_path, dest_path):
    list_values = list()
    if not os.path.isdir(dest_path):
        os.mkdir(dest_path)
    else:
        pass


    for folderName, subFolders, fnames in os.walk(source_path):
        for fname in fnames:
            if fname.endswith('.png') | fname.endswith('.jpg') | fname.endswith('.jpeg') | fname.endswith('.JPG') | fname.endswith('.bmp') | fname.endswith('.PNG'):  # | fname.endswith('.mp4'):

                fpath = os.path.join(folderName, fname)
                print(fpath)
                mdate = datetime.date.fromtimestamp(os.path.getmtime(fpath))
                year = str(mdate)[:4]
                month = str(mdate)[5:7]
                date = str(mdate)[-2:]
                size = os.path.getsize(fpath)
                current = year + "-" + month

                list_values = get_file_details(list_values=list_values, name=fname, year=year, month=month, date=date, size=size, source=folderName, current=current)
                if os.path.isdir(dest_path + "/" + year + "-" + month):

                    # Duplicate handling
                    if not os.path.exists(dest_path + "/" + year + "-" + month + "/" + fname):
                        shutil.move(os.path.join(folderName, fname), os.path.join(dest_path, year + "-" + month))
                    else:
                        try:
                            os.mkdir(dest_path + "/" + year + "-" + month + "/" + "__2__")
                        except:
                            try:
                                shutil.move(os.path.join(folderName, fname), dest_path + "/" + year + "-" + month + "/" + "__2__")
                            except:
                                pass
                else:
                    try:
                        os.mkdir(dest_path + "/" + year + "-" + month)
                        shutil.move(os.path.join(folderName, fname), dest_path + "/" + year + "-" + month)
                    except:
                        continue

            else:
                continue
    return list_values


# SOURCE_PATH = "E:/Cluttered-Photos"
# DEST_PATH = "E:/Photos"

SOURCE_PATH = "G:/Archives/GDrive_GPhotos/takeout"
DEST_PATH = "G:/Archives/GDrive_GPhotos/GPhotos"


def main():

    list_values = image_date_sort(source_path= SOURCE_PATH, dest_path= DEST_PATH)
    df2 = pd.DataFrame(list_values, columns=['Filename', 'Year', 'Month', 'Date', 'Size', 'Source', 'Current'])
    df2.to_csv(r'\images.csv', index=None, header=True)


    move_file_type(source_path=SOURCE_PATH, dest_path=DEST_PATH)


if __name__ == '__main__':
    main()