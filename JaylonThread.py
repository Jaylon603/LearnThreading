#Calculates Staff's yearly salary and see if combined meet the goal of $500,000
# With multi threading we can seemingly find salary and subtract from goal total
import threading
import sys

#define variables
ManagerSalary = 0.0
OwnerSalary = 0.0
global sumIncome
sumIncome = 500000

def calcManager(hr):
    #function to calculate Manager yearly
    global sumIncome
    print("Manager Salery: {}" .format(hr * 40 * 52))
    sumIncome -= hr* 40 *52

def calcOwner(hr):
    #function to calculate Owner yearly
    global sumIncome
    print("Owner Salery: {}" .format(hr * 40 * 52))
    sumIncome -= hr* 40 *52

if __name__ =="__main__":
     # creating thread
    x = threading.Thread(target=calcManager, args=(40,))
    y = threading.Thread(target=calcOwner, args=(90,))
 
    # starting thread 1
    x.start()
    # starting thread 2
    y.start()
 
    # wait until thread 1 is completely executed
    x.join()
    # wait until thread 2 is completely executed
    y.join()
 
    # both threads completely executed
    if sumIncome <=0:
        print("Sum goal reached!")
    print("Done!")