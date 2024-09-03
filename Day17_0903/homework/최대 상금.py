def max_price(cnt):
    global max_v
    if cnt == int(change):
        answer = int(''.join(map(str,m_list)))
        if max_v < answer:
            max_v = answer
        return
    N = max(m_list)
    for i in range(len(m_list)-1):
        for j in range(i+1,len(m_list)):
            if m_list[i]>=m_list[j]: continue
            else:
                m_list[i],m_list[j] = m_list[j],m_list[i]
                max_price(cnt+1)
                m_list[j],m_list[i] = m_list[i],m_list[j]
T = int(input())
for tc in range(1,T+1):
    money,change = input().split()
    m_list=[]
    for i in money:
        m_list.append(int(i))
    max_v = 0
    max_price(0)
    print(max_v)