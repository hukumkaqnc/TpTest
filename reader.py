from main import*
user = 'Кравченко'
alpha = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'
alpha = alpha.split()
doc1_id = "1QVGSGIqZxLSCrtwD8WsT3Thar_X7mcgcPv3NQr_aRq0"
doc2_id = "1uavinxCLtNEXu3O1z5dlabq0yPK8xWvZK8Hs8coBk9Y"
doc_dict = {doc1_id: ['09.03.03 Прикладная информатика - ведомости лето 2022-2023', groups_list], doc2_id: ['09.03.04 Программная инженерия - ведомости лето 2022-2023', groups_list1] }
teachers = list()
stud_dict = dict()
stud_list = list()
cred = Creds()
print(doc_dict[doc1_id][1])

print(cred.get(doc1_id, "D11"))
firstL = alpha.index('D')
firstN = 11
subjects_dict = {doc1_id: [], doc2_id: []}
subjects_list = list()
for d in doc_dict:
    print('\t'+d)
    for gr in doc_dict[d][1]:
        print(gr)
        for elem in cred.get(d, gr+'!'+"D11:V11")['values']:
            for el in elem:
                # print(el+'\n')
                if el.find(user)>=0:
                    print('match')
                    letter = alpha[firstL+elem.index(el)]
                    number = str(firstN-2)
                    subject = cred.get(d, gr+'!'+alpha[firstL+elem.index(el)]+str(
                    firstN-2  
                    ))['values'][0][0]
                    typeS = cred.get(d, gr+'!'+alpha[firstL+elem.index(el)]+str(
                    firstN+2  
                    ))['values'][0][0]
                    lst = [gr, subject, typeS, letter, number]
                    subjects_dict[d].append(lst)
                    if not (subject in subjects_list):
                        subjects_list.append(subject)
                teachers.append(el)
sub = subjects_list[0]

for d in subjects_dict:
    print(d)
    for elem in subjects_dict[d]:
        print(elem)
for d in subjects_dict:
    for elem in subjects_dict[d]:

        if elem[1] == sub:
            arr = cred.batch(d, elem[0]+'!'+"B14:C100",'COLUMNS')['valueRanges'][0]['values']
            
            for it in range(len(arr[0])):
                
                stud_dict[arr[1][it]] = [d, arr[0][it], elem[0], elem[1], elem[2], elem[3], elem[4]]
print(stud_dict)             
    
for st in stud_dict:
    mark = '5' #input(stud_dict[st][1]+' '+stud_dict[st][2]+' - ')
    stud_dict[st]=[stud_dict[st][0],stud_dict[st][1],stud_dict[st][2],stud_dict[st][3],stud_dict[st][4],stud_dict[st][5],stud_dict[st][6], mark]
print(stud_dict)
count = 0
group = doc_dict[doc1_id][1][0]
mark_arr =[[''] for i in range(len(stud_dict))]
for st in stud_dict:
    if group != stud_dict[st][2]:
        print(group)
        group = stud_dict[st][2]
        cred.update(doc_id, gr_n+'!'+let+'14:'+let+str(14+len(mark_arr)-1), 'RAW', mark_arr)
        count = 0
    let = stud_dict[st][5]
    doc_id = stud_dict[st][0]
    gr_n = stud_dict[st][2]
    mark_arr[count][0]=stud_dict[st][7]
    count+=1
for i in range(count,len(mark_arr)-1):
    mark_arr[i][0] = ''
cred.update(doc_id, gr_n+'!'+let+'14:'+let+str(14+len(mark_arr)-1), 'RAW', mark_arr)
    
    



