import random
#C������ �������
def passautomat()->str:
	"""������ ��������� �������
	"""	
	str0=".,:;!_*-+()/#�%&"
	str1 = '0123456789'
	str2 = 'qwertyuiopasdfghjklzxcvbnm'
	str3 = str2.upper() # 'QWERTYUIOPASDFGHJKLZXCVBNM'
	str4 = str0+str1+str2+str3
	ls = list(str4) # ������ [".",",",":"...]
	random.shuffle(ls) #����������
# ��������� �� ������ 12 ������������ ��������
	psword = ''.join([random.choice(ls) for x in range(12)])
# ������ �����
	return psword
