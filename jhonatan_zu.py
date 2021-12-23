import json
import requests
import time, itertools


input=input('\nEnter int target: ')
input= int(input)

def search():
    res=requests.get('https://mach-eight.uc.r.appspot.com/')
    json_To_py=json.loads(res.text)
    val=json_To_py['values']
    return val

def extract(): 
    h_in=[]
    summary=[]
    for i in search():
        h_in.append(i['h_in'])
    for i in search():
        summary.append(
            {'name':i['first_name']+' '+i['last_name'],'height':int(i['h_in'])}
        )
    return h_in,summary #(raw_input,li)

def algorit(raw_list):
    global input
    s=[int(item) for item in raw_list]
    s=list(set(s))
    s.sort()
    found=False
    #input=139
    zero,hi=0,len(s)-1
    output=[]
    print('\nOperation:')
    while zero<=hi:
        total=int(s[zero])+int(s[hi])
        if total==input:
            found=True
            print(s[zero],'----',s[hi],'=', input)
            output.append([s[zero],s[hi]])
            if zero==hi: break  
            hi-=1
        
        elif total<input:
            zero+=1
        else:
            hi-=1
        #time.sleep(1) #<<
    if found==False:
        #print('\n>>>> Match not found <<<<')
        return False
    print ('\noutput:')
    for i in output:
        print(i)
    return output #res


def match(res,li):
    # change list of dicts into matrix
    new_li=[]
    id = 0
    for i in li:  
        new_li.append([
            i['height'],i['name'],id
        ])
    iter = itertools.product(new_li, repeat=2)
    iter= list(iter)
    count = 0
    i=0
    cut=0
    memory={} #dict with memory for the unique string of match
    print('\nTry Match-->\n') 
    while 1:
        if count >= len(res):
            count = 0   
        if i == len(iter):
            i=0
        if [res[count][0],res[count][1]] == [iter[i][0][0], iter[i][1][0]]:
            memory[str(iter[i][0][1])+' '+str(iter[i][0][0])+ ' --- ' +str(iter[i][1][1])+' '+str(iter[i][1][0])]=count
            #print('#', end='')
        count+=1
        i+=1
        if cut == len(new_li)**2*5: #Threshold based on list size
            break
        cut +=1
        #time.sleep(2)
    
    print('\n--------------------------------------------> Debug match\n\nRESULT:\n')

    for i in memory:
        print (i)

if __name__=="__main__":
    res=algorit(extract()[0])
    if res==False:
        print('\n>>>>>> MATCH NOT FOUND <<<<<<')
    else:
        li=extract()[1]
        match(res,li)
    

    