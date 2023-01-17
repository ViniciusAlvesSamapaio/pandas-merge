import pandas as pd 

#dados que serão utilizados no merge
cadastro = {'ID': ['HH328', 'TE234', 'LK342', 'PP097', 'QU821', 'UW123'],
            'Nome': ['maria', 'roger', 'marcos', 'vinicius', 'marcio','mario' ],
            'Idade': [24, 34, 54, 23, 18, 19],
            'CEP': ['83294-234','23484-324','38423-943','38420-324','89324-743', '12839-312']
        }
cadastro = pd.DataFrame(cadastro, columns = ['ID', 'Nome', 'Idade', 'CEP'])

cadastro1 = {'ID': ['JA821', 'LO128', 'YU389', 'PK839', 'YE892', 'QU821'],
            'Nome': ['monica', 'rogeria', 'momo', 'vanessa', 'maria', 'marcio'  ],
            'Idade': [23, 64, 31, 17, 34, 18],
            'CEP': ['37824-234','78903-234','42343-467','43893-384','47823-637', '89324-743']
        }

cadastro1 = pd.DataFrame(cadastro1, columns = ['ID', 'Nome', 'Idade', 'CEP'])

compras = { 'ID': ['JA821', 'LO128', 'YU389', 'PK839', 'YE892', 'PP097', 'QU821'],
            'Data': ['2021-08-12', '2022-09-23', '2022-03-30', '2023-12-10', '2022-11-09','2021-02-10','2022-07-14' ],
            'Valor': [923, 3123, 93, 10, 23, 90, 100]
        }

compras = pd.DataFrame(compras, columns = ['ID', 'Data', 'Valor'])


# usando a função Merge inner

#b = pd.merge(cadastro, cadastro1, on=["ID"], how="inner")

b = pd.merge(cadastro, cadastro1[['ID', 'Idade', 'CEP']], on=["ID"], how="inner")
print(b)

# usando a função Merge Full

lojas = pd.concat([cadastro, cadastro1], ignore_index=True)
lojas = lojas.drop_duplicates(subset="ID")
print(lojas)

# usando a função Merge Left Join

c = pd.merge(cadastro, compras, on=["ID"], how="left")
print(c)
