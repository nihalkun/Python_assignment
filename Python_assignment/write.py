def main() :
    outfile = open('myfile.txt','w')

    fname = input("Enter your first name: ")
    lname = input("Enter your last name: ")

    outfile.write(fname + '\n')
    outfile.write(lname + '\n')

    outfile.close()


def read() :
    outfile = open('myfile.txt','r')
    
    for l in outfile:
        print(l)
    outfile.close()

    

def append() :
    outfile = open('myfile.txt','a+')
  
    names = input("Enter your first name: ")
    
    outfile.write(names + '\n')
    for l in outfile:
        print(l)
    outfile.close()


append()   
read() 