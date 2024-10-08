import datetime
def store_non_primes(use):
    f=open("Non_Primes.txt", "a")
    f.write("%s " % use)
    f.close
def store_non_primes_new_line():
    f=open("Non_Primes.txt", "a")
    f.write("\n")
    f.close
def store_primes(use):
    f=open("New_Primes.txt", "a")
    f.write("%s " % use)
    f.close
def new_limit(use, primes):
    j=0
    squared=use**(1./2)
    while primes[j]<squared:
        j +=1
    j +=1
    return j
def time_check(Time):
    return(datetime.datetime.now()-Time)
def known_non_primes(use,non_primes,limit, indicate):
    if indicate==True:
        opposites=[limit[0]-nons for nons in non_primes]
        non_primes=opposites
    else:
        non_primes.append(use)
def non_factor(use, primes, limit):
    i=0
    Boo=False
    while (Boo==False) and (i<limit[1]):
        if use%primes[i]!=0:
            i +=1
        else:
            Boo=True
    return i
def is_it_prime(use, primes, limit):
    i=0
    Boo=True
    while (Boo==True) and (i<limit):
        if use%primes[i]!=0:
            i +=1
        else:
            Boo=False
    return Boo
def prime_factors(use, primes, limit):
    user=use+0
    i=0
    factors=[]
    while (i<limit) and (user!=1):
        if use%primes[i]==0:
            factors.append(primes[i])
            while user%primes[i]==0:
                user /=primes[i]
        i +=1
    if user==1:
        return factors
    else:
        return use
def list_update(use, primes, limit, count_list, reset_list, non_primes, indicate, time):
    if use>limit[0]:
        print(time_check(time))
        print("New Milestone")
        limit[2]=limit[0]*1
        limit[0] *=primes[limit[1]]
        count_list.append(0)
        reset_list.append(primes[limit[1]]-1)
        non_primes.clear()
        non_primes.append(primes[limit[1]])
        limit[1] +=1
        indicate=False
    return indicate
def counter(count_list, reset_list):
    i=0
    Boo=False
    while i<len(count_list) and (Boo==False):
        if count_list[i]==0:
            i +=1
        else:
            Boo=True
    if Boo==False:
        count_list[-1]=reset_list[-1]
        return i
    else:
        count_list[i-1]=reset_list[i-1]
        count_list[i] -=1
        return i
def massprimeduction(limitations):
    using=11
    Time=datetime.datetime.now()
    massprimeduction.Primes=[2,3,5,7,11]
    for i in massprimeduction.Primes:
        store_primes(i)
    Limit=[30,3,6]
    Count_list=[0,1]
    Reset_list=[0,1]
    Opposite_non_primes=[2]
    indicator=False
    while using<limitations:
        indicator=list_update(using, massprimeduction.Primes, Limit, Count_list, Reset_list, Opposite_non_primes, indicator, Time)
        add=massprimeduction.Primes[counter(Count_list, Reset_list)]
        using +=add-1
        if using>(Limit[0]/2) and indicator==False:
            Opposite_non_primes=Opposite_non_primes[-1::-1]
            indicator=True
        if indicator==True:
            if len(Opposite_non_primes)!=0:
                if using%massprimeduction.Primes[Opposite_non_primes[0]]!=0:
                    if is_it_prime(using, massprimeduction.Primes, new_limit(using, massprimeduction.Primes))==True:
                        massprimeduction.Primes.append(using)
                        store_primes(using)
                else:
                    Opposite_non_primes.remove(Opposite_non_primes[0])
            else:
                if is_it_prime(using, massprimeduction.Primes, new_limit(using, massprimeduction.Primes))==True:
                        massprimeduction.Primes.append(using)
                        store_primes(using)
        else:
            if is_it_prime(using, massprimeduction.Primes, new_limit(using, massprimeduction.Primes))==True:
                    massprimeduction.Primes.append(using)
            else:
                Opposite_non_primes.append(non_factor(using, massprimeduction.Primes, Limit))
    print("Primes ")
    #for prime in massprimeduction.Primes:
        #print(prime, end=" ")
        #store_primes(prime)
    print(time_check(Time))
if __name__ == "__main__":
    Input=input("What is the Limit?\n")
    Input=int(Input)
    massprimeduction(Input)