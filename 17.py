import inflect
p = inflect.engine()

tot = 0

for i in range(1,1001):
    words = p.number_to_words(i, wantlist=True)
    for j in words:
        st = j.replace('-','')
        st = st.replace(' ','')
        print st
        tot += len(st)

print tot