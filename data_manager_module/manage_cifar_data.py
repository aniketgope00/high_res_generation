import os

def view_files()->None:
    files = os.listdir('./data')
    print("Files in ./data")
    for file in files:
        print(file)

    print(end = "\n")

    print(f"Files in ./data/{files[0]}")
    batch_files = os.listdir('./data/'+files[0])
    for file in batch_files:
        print(file)

    print(end = "\n")

def delete_files()->None:
    files = os.listdir('./data')
    batch_files = os.listdir('./data/'+files[0])
    for file in batch_files:
        os.remove('./data/'+files[0]+'/'+file)
    for file in files:
        os.remove('./data/'+file)
    os.rmdir('./data')


if __name__ == "__main__":
    view_files()
    delete_files()