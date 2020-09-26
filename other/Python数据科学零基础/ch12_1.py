class Banks():
    '''定义银行'''
    bankname = 'MinSheng Bank'

    def motto(self):
        return "以客为尊"


userbank = Banks()
print("目前服务银行是", userbank.bankname)
print("银行服务理念是", userbank.motto())
