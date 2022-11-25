import os

#check if the directory exists
if not os.path.exists("./CIFAR10/DataSplit"):
    os.makedirs("./CIFAR10/DataSplit")
if not os.path.exists("./CIFAR10/ConvexPolytopePoisons"):    
    os.mkdir("./CIFAR10/ConvexPolytopePoisons")
if not os.path.exists("./CIFAR10/Features"):
    os.mkdir("./CIFAR10/Features")
if not os.path.exists("./CIFAR10/TestSplit"):
    os.mkdir("./CIFAR10/TestSplit")
if not os.path.exists("./CIFAR10/TrainSplit"):
    os.mkdir("./CIFAR10/TrainSplit")
if not os.path.exists("Logs"):
    os.mkdir("Logs")

#concatenate all the modelCheckpointPartitions into one tar file
os.system("cat modelCheckPointPartition00 modelCheckPointPartition01 modelCheckPointPartition02 modelCheckPointPartition03 modelCheckPointPartition04 modelCheckPointPartition05 modelCheckPointPartition06 modelCheckPointPartition07 > modelCheckPoints.tar.gz")
    
#extract the tar file
os.system("tar -xvf modelCheckpoints.tar.gz")

  



print("Extracting CIFAR10")
os.system("python ./CIFAR_Download/parseCIFAR.py")

print("Parsing Convex Polytope Poisons")
os.system("python ./CIFAR_Download/parsePoison.py")

print("Creating Data Partitions")
os.system("python ./CIFAR_Download/createDataSplit.py")

print("Extracting Features from Pre-trained Models")
os.system("python extractFeatures.py")
