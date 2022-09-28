from validate_docbr import CPF, CNPJ

# Class Factory
class Documento:

    @staticmethod
    def cria_documento(documento):
        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) == 14:
            return DocCnpj(documento)
        else:
            raise ValueError("Quantidade de dígitos incorreta")

class DocCpf:
    def __init__(self, documento):
        if self.valida(documento):
            self.cpf = documento
        else:
            raise ValueError("Cpf inválido!")
    
    def __str__(self):
        return self.format()
    
    def valida(self, cpf):
        validador = CPF()
        return validador.validate(cpf)
    
    def format(self):
        # fatia_um = self.cpf[:3]
        # fatia_dois = self.cpf[3:6]
        # fatia_tres = self.cpf[6:9]
        # fatia_quatro = self.cpf[9:]
        # return "{}.{}.{}-{}".format(fatia_um, fatia_dois, fatia_tres, fatia_quatro)
        mascara = CPF()
        return mascara.mask(self.cpf)

class DocCnpj:
    def __init__(self, documento):
        if self.valida(documento):
            self.cnpj = documento
        else:
            raise ValueError("Cnpj inválido!!")

    def __str__(self):
        return self.format()
    
    def valida(self, cnpj):
        validador = CNPJ()
        return validador.validate(cnpj)
    
    def format(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)



# Primeira classe

# class CpfCnpj:
#     def __init__(self, doc, tipo_doc):
#         self.tipo_doc = tipo_doc
#         doc = str(doc)
#         if tipo_doc == "cpf":
#             if self.cpf_valido(doc):
#                 self.cpf = doc
#             else:
#                 raise ValueError("Cpf inválido!")
#         elif tipo_doc == "cnpj":
#             if self.cnpj_valido(doc):
#                 self.cnpj = doc
#             else:
#                 raise ValueError("Cnpj inválido!!")
#         else:
#             raise ValueError("Documento inválido")

#     def __str__(self):
#         if(self.tipo_doc == "cpf"):
#             return self.formata_cpf()
#         elif(self.tipo_doc == "cnpj"):
#             return self.formata_cnpj()
#         else:
#             raise ValueError("Documento inválido")

#     def cpf_valido(self, cpf):
#         if len(cpf) == 11:
#             validador = CPF()
#             return validador.validate(cpf)
#         else:
#             raise ValueError("Quantidade de dígitos é inválida!")
    
#     def cnpj_valido(self, cnpj):
#         if len(cnpj) == 14:
#             validador = CNPJ()
#             return validador.validate(cnpj)
#         else:
#             raise ValueError("Quantidade de dígitos inválido")
    
#     def formata_cpf(self):
#         mascara = CPF()
#         return mascara.mask(self.cpf)

#     def formata_cnpj(self):
#         mascara = CNPJ()
#         return mascara.mask(self.cnpj)