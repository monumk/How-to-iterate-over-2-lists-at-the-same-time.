'''How to iterate over 2+ lists at the same time
You can zip() lists and then iterate over the zip object. A zip object is an iterator of tuples.'''

l1=[1,2,3,4,5]
l2=[10,20,30,40,50]
l3=[100,200,300,400,500]
l4=zip(l1,l2,l3)

for l1,l2,l3 in l4:
    print(l1,l2,l3)
    
