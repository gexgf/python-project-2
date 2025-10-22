logi = (
    ('2020-12-10 09:07:55.075064', 'ERROR'),
    ('2020-12-10 09:07:58.075064', 'WARNING'),
    ('2020-12-10 09:07:58.075061', 'WARNING'),
    ('2020-12-10 09:07:55.075064', 'ERROR'),
    ('2020-12-10 09:07:58.075064', 'ERROR'),
    ('2020-12-10 09:07:58.075064', 'WARNING'),
    ('2020-12-10 09:07:58.075064', 'INFO'),
    ('2020-12-10 09:07:58.075064', 'ERROR'),
    ('2020-12-10 09:07:58.075060', 'WARNING'),
    ('2020-12-10 09:07:57.075064', 'WARNING'),
    ('2020-12-10 09:07:55.075064', 'ERROR'),
    ('2020-12-10 09:07:58.075064', 'INFO'),
    ('2020-12-10 09:07:52.075064', 'ERROR'),
    ('2020-12-10 09:07:52.075064', 'ERROR'),
    ('2020-12-10 09:07:58.075064', 'INFO'),
    ('2020-12-10 09:07:58.075066', 'INFO'),
    ('2020-12-10 09:07:58.075066', 'INFO'),
    ('2020-12-10 09:07:58.075064', 'INFO'),
    ('2020-12-10 09:07:58.075064', 'ERROR'),
    ('2020-12-10 09:07:58.075064', 'WARNING'),
)

logi_check = (
    ('2020-12-10 09:07:58.075064', 'INFO'),
    ('2020-12-10 09:07:58.075060', 'WARNING'),
)

clean = []
# print(type(clean))

for a in logi:
    if a not in clean:
        clean.append(a)

def check_if (dane, logi_check):
    for a in logi_check:
        if a not in dane:
            return False
    return True



print(check_if(clean, logi_check))




def check_if2 (dane, logi_check):
    return dane.issuperset(logi_check)

clean_set = set(logi)

# print(len(clean_set))

print(check_if2(clean_set, logi_check))





