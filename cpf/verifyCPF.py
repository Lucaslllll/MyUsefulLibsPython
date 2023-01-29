def validate_cpf(self, data):
        try:
            see_is_str = int(data)
        except ValueError:
            raise serializers.ValidationError("CPF is Invalid, only numbers")
        
        if len(data) == 11:
            if self.step1CPF(data):
                return data 
            else:
                raise serializers.ValidationError("CPF is Invalid")
        else:
            raise serializers.ValidationError("CPF is Invalid, length wrong")


def step1CPF(self, cpf:str):
    soma = 0; multiplication = 11
    for i in range(11):
        if i == 10:
            continue
        else:
            soma += (int(cpf[i])*multiplication)
            multiplication -= 1
        
    
    soma *= 10
    if soma % 11 == int(cpf[10]):
        if self.step2CPF(cpf): 
            return True
        else:
            return False
        
    else:
        return False

def step2CPF(self, cpf:str):
    dic = ['00000000000','11111111111', '22222222222', '33333333333', '44444444444',
            '55555555555','66666666666', '77777777777', '88888888888', '99999999999']
    soma = 0; multiplication = 10;
    for i in range(11):
        if i == 10 or i == 9:
            continue
        else:
            soma += (int(cpf[i])*multiplication)
            multiplication -= 1

    soma *= 10
    if soma % 11 == int(cpf[9]):
        for i in range(10):
            if cpf == dic[i]:
                return False

        
        return True
    else:
        return False


