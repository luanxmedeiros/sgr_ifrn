from lib2to3.pgen2.tokenize import group

from appsgr.models import *


#Grupos
professores=Grupo(name="Professores")
professores.save()
coordenadores=Grupo(name="Coordenadores")
coordenadores.save()
diretores=Grupo(name="Diretores")
diretores.save()
tecadm=Grupo(name="Técnicos Administrativo")
tecadm.save()
alunos=Grupo(name="Alunos")
alunos.save()



# Pessoas
pes1=Pessoa(is_staff=True,first_name='Givanaldo', last_name="Rocha", cpf='33344455560',email='givanaldo@gmail.com',data_nascimento="1973-05-30", telefone='8499253259' ,username='20122148000001')
pes1.set_password('123456')
pes1.save()
professores.user_set.add(pes1)
coordenadores.user_set.add(pes1)
pes2=Pessoa(first_name='Alvaro', last_name="Hermano", cpf='33344455561',email='alvaro@gmail.com',data_nascimento="1976-03-22",username='20122148000002',  telefone='84955556661')
pes2.set_password('123456')
pes2.save()
professores.user_set.add(pes2)
coordenadores.user_set.add(pes2)
pes3=Pessoa(first_name='Luiz', last_name="Ricardo", cpf='33344955562',email='luiz@gmail.com',data_nascimento="1975-08-12",username='20122148000003', telefone='84955556662')
pes3.set_password('123456')
pes3.save()
professores.user_set.add(pes3)
pes4=Pessoa(first_name='Bruno Gomes', last_name="Gurgel", cpf='33344455563',email='bruno@gmail.com',data_nascimento="1973-05-30",username='20122148000004',  telefone='84955556663')
pes4.set_password('123456')
pes4.save()
professores.user_set.add(pes4)
coordenadores.user_set.add(pes4)
pes5=Pessoa(first_name='Diogenes Henrique', last_name="Silva", cpf='33344455564',email='diogenes@gmail.com',data_nascimento="1976-03-22",username='20122148000005', telefone='84955556664')
pes5.set_password('123456')
pes5.save()
professores.user_set.add(pes5)
pes6=Pessoa(first_name='Bartolomeu Silva', last_name="Borges", cpf='33344455565',email='bartolomeu@gmail.com',data_nascimento="1975-03-19",username='20122148000006',telefone='84955556665')
pes6.set_password('123456')
pes6.save()
professores.user_set.add(pes6)
pes7=Pessoa(first_name='Silvia Araújo', last_name="de Lima", cpf='33344455566',email='silvia@gmail.com',data_nascimento="1973-05-30",username='20122148000007', telefone='84955556666')
pes7.set_password('123456')
pes7.save()
professores.user_set.add(pes7)
pes8=Pessoa(first_name='Renata Cavalcanti', last_name="Pereira", cpf='33344455567',email='renata@gmail.com',data_nascimento="1976-03-22",username='20122148000008', telefone='84955556667')
pes8.set_password('123456')
pes8.save()
professores.user_set.add(pes8)
pes9=Pessoa(first_name='Hugo Limeira', last_name="da Silva", cpf='33344455568',email='hugo@gmail.com',data_nascimento="1975-08-12",username='20122148000009',  telefone='84955556668')
pes9.set_password('123456')
pes9.save()
professores.user_set.add(pes9)
pes10=Pessoa(first_name='Fernando Barcelar', last_name="Gomes", cpf='33344455569',email='fernando@gmail.com',data_nascimento="1978-05-30",username='20122148000010', telefone='84955556669')
pes10.set_password('123456')
pes10.save()
professores.user_set.add(pes10)
pes11=Pessoa(first_name='Isaú Lopes', last_name="Sousa", cpf='33344455570',email='isau@gmail.com',data_nascimento="1976-03-22",username='20122148000011', telefone='84955556670')
pes11.set_password('123456')
pes11.save()
professores.user_set.add(pes11)
pes12=Pessoa(first_name='Otávio Moreira', last_name="Cardoso", cpf='33344455571',email='otavio@gmail.com',data_nascimento="1975-08-12",username='20122148000012', telefone='84955556671')
pes12.set_password('123456')
pes12.save()
professores.user_set.add(pes12)
pes13=Pessoa(first_name='Júlio Hermano', last_name="Pires", cpf='33344455572',email='julio@gmail.com',data_nascimento="1970-09-12",username='20122148000013',  telefone='84955556672')
pes13.set_password('123456')
pes13.save()
professores.user_set.add(pes13)
pes14=Pessoa(first_name='Claudio Pereira', last_name="Vasconcelos", cpf='33344455573',email='claudio@gmail.com',data_nascimento="1975-04-30",username='20122148000014', telefone='84955556673')
pes14.set_password('123456')
pes14.save()
professores.user_set.add(pes14)
pes15=Pessoa(first_name='Tadeu Viera', last_name="de Sousa", cpf='33344455574',email='tadeu@gmail.com',data_nascimento="1973-07-18",username='20122148000015', telefone='84955556674')
pes15.set_password('123456')
pes15.save()
professores.user_set.add(pes15)
pes16=Pessoa(first_name='João Maria', last_name="de Lima", cpf='33344455575',email='joaogmail.com',data_nascimento="1973-07-21",username='20122148000016', telefone='84952956674')
pes16.set_password('123456')
pes16.save()
professores.user_set.add(pes16)
pes17=Pessoa(first_name='Valdemiro', last_name="Júnior", cpf='33344455576',email='valdemirogmail.com',data_nascimento="1970-09-14",username='20122148000017', telefone='84962956874')
pes17.set_password('123456')
pes17.save()
professores.user_set.add(pes17)
pes18 = Pessoa(first_name='Felipe', last_name="Quintaes", cpf='22259844456',email='felipe@gmail.com',data_nascimento="1979-02-20",username='20112148000018', telefone='84977776666')
pes18.set_password('123456')
pes18.save()
diretores.user_set.add(pes18)

#Diretor
dir1=Diretor(pessoa=pes18)
dir1.save()

cam1 = Campus(nome='Parnamirim', telefone='40054108', cidade='Parnamirim', endereco='Rua Boa Esperança', bairro='Nova Esperança', numero=75)
cam1.save()
cam1.diretores.add(dir1)

#Tecnico administrativo
pes19=Pessoa(first_name='Eduardo', last_name="Chavez", cpf='55566633301',email='eduardo@gmail.com',data_nascimento="1989-05-15",username='20112133010219',  telefone='84955196660')
pes19.set_password('123456')
pes19.save()
tecadm.user_set.add(pes19)
pes20=Pessoa(first_name='Ana Paula', last_name="", cpf='55566633302',email='ana@gmail.com',data_nascimento="1986-09-22",username='2011213301020', telefone='84956286660')
pes20.set_password('123456')
pes20.save()
tecadm.user_set.add(pes20)




#Coordenadores
cor1=Coordenador(pessoa=pes1)
cor1.save()
cor2=Coordenador(pessoa=pes2)
cor2.save()
cor3=Coordenador(pessoa=pes3)
cor3.save()
cor4=Coordenador(pessoa=pes4)
cor4.save()
cor5=Coordenador(pessoa=pes5)
cor5.save()
cor6=Coordenador(pessoa=pes6)
cor6.save()
cor7=Coordenador(pessoa=pes7)
cor7.save()
cor8=Coordenador(pessoa=pes8)
cor8.save()
cor9=Coordenador(pessoa=pes9)
cor9.save()
cor10=Coordenador(pessoa=pes10)
cor10.save()
cor11=Coordenador(pessoa=pes11)
cor11.save()
cor12=Coordenador(pessoa=pes12)
cor12.save()
cor13=Coordenador(pessoa=pes13)
cor13.save()
cor14=Coordenador(pessoa=pes14)
cor14.save()
cor15=Coordenador(pessoa=pes15)
cor15.save()





mod1 =  ModalidadeCurso(nivel='Superior', nome='Superior')
mod1.save()
mod2 =  ModalidadeCurso(nivel='Subsequente', nome='Médio')
mod2.save()
mod3 =  ModalidadeCurso(nivel='Integrado', nome='Médio')
mod3.save()

turn1 = Turno(nome='Matutino')
turn2 = Turno(nome='Verpertino')
turn3 = Turno(nome='Noturno')
turn1.save()
turn2.save()
turn3.save()

#Professores
prof1 = Professor(pessoa=pes1,  campus_atuante=cam1) #Givanaldo
prof1.save()
prof2 = Professor(pessoa=pes2,  campus_atuante=cam1) #Alvaro
prof2.save()
prof3 = Professor(pessoa=pes4,  campus_atuante=cam1) #Bruno
prof3.save()
prof4 = Professor(pessoa=pes5,  campus_atuante=cam1)
prof4.save()
prof5 = Professor(pessoa=pes6,  campus_atuante=cam1)
prof5.save()
prof6 = Professor(pessoa=pes7,  campus_atuante=cam1)
prof6.save()
prof7 = Professor(pessoa=pes15,  campus_atuante=cam1)
prof7.save()
prof8 = Professor(pessoa=pes9,  campus_atuante=cam1)
prof8.save()
prof9 = Professor(pessoa=pes16,  campus_atuante=cam1)
prof9.save()
prof10 = Professor(pessoa=pes17,  campus_atuante=cam1)
prof10.save()

#Disciplinas
disciplina1 = Disciplina(nome="Estrutura de Dados")
disciplina1.save()
disciplina1.professores.add(prof1,prof8)


disciplina2 = Disciplina(nome="Programação Orientada a Objetos")
disciplina2.save()
disciplina2.professores.add(prof1,prof3)

disciplina3 = Disciplina(nome="Engenharia de Software")
disciplina3.save()
disciplina3.professores.add(prof2)

disciplina4 = Disciplina(nome="Cálculo")
disciplina4.save()
disciplina4.professores.add(prof10)

disciplina5 = Disciplina(nome="Análise de Projeto Orientada a Objetos")
disciplina5.save()
disciplina5.professores.add(prof9)


#Cursos superiores
cur1=Curso(nome='Sistemas Para Internet', coordenador=cor1, ativo=True, campus=cam1, anos=3, modalidade=mod1, periodos=6)
cur1.save()
cur1.disciplinas.add(disciplina1,disciplina2,disciplina3,disciplina4,disciplina5)
cur1.turnos.add(turn1, turn2, turn3)

cur2=Curso(nome='Redes de Computadores', coordenador=cor4, ativo=True, campus=cam1, anos=3, modalidade=mod1, periodos=6)
cur2.save()
cur2.turnos.add(turn1, turn2)

cur3=Curso(nome='Física', coordenador=cor14, ativo=True, campus=cam1, anos=3, modalidade=mod1, periodos=6)
cur3.save()
cur3.turnos.add(turn2, turn3)

cur4=Curso(nome='Matemática', coordenador=cor13, ativo=True, campus=cam1, anos=3, modalidade=mod1, periodos=6)
cur4.save()
cur4.turnos.add(turn1, turn3)

cur5=Curso(nome='TADS', coordenador=cor12, ativo=True, campus=cam1, anos=3, modalidade=mod1, periodos=6)
cur5.save()
cur5.turnos.add(turn1, turn2, turn3)

cur18=Curso(nome='Matemática', coordenador=cor1, ativo=True, campus=cam1, anos=3, modalidade=mod1, periodos=6)
cur18.save()
cur18.turnos.add(turn2, turn3)

cur19=Curso(nome='Redes de Computadores', coordenador=cor4, ativo=True, campus=cam1, anos=3, modalidade=mod1, periodos=6)
cur19.save()
cur19.turnos.add(turn1, turn2, turn3)


#Subsequente
cur6=Curso(nome='Redes de Computadores', coordenador=cor4, ativo=True, campus=cam1, anos=2, modalidade=mod2, periodos=4)
cur6.save()
cur6.turnos.add(turn1, turn2, turn3)

cur7=Curso(nome='Mecatronica', coordenador=cor3, ativo=True, campus=cam1, anos=2, modalidade=mod2, periodos=4)
cur7.save()
cur7.turnos.add(turn1, turn2, turn3)

cur8=Curso(nome='Edificações', coordenador=cor9, ativo=True, campus=cam1, anos=2, modalidade=mod2, periodos=4)
cur8.save()
cur8.turnos.add(turn1, turn2, turn3)

cur9=Curso(nome='Energias Renováveis', coordenador=cor8, ativo=True, campus=cam1, anos=2, modalidade=mod2, periodos=4)
cur9.save()
cur9.turnos.add(turn1, turn2, turn3)

cur10=Curso(nome='Petróleo e Gás', coordenador=cor7, ativo=True, campus=cam1, anos=2, modalidade=mod2, periodos=4)
cur10.save()
cur10.turnos.add(turn1, turn2, turn3)

#Integrado
cur11=Curso(nome='Informática', coordenador=cor2, ativo=True, campus=cam1, anos=4, modalidade=mod3, periodos=0)
cur11.save()
cur11.turnos.add(turn1, turn2)

cur12=Curso(nome='Mecânica', coordenador=cor4, ativo=True, campus=cam1, anos=4, modalidade=mod3, periodos=0)
cur12.save()
cur12.turnos.add(turn1, turn2)

cur13=Curso(nome='Mecatrônica', coordenador=cor3, ativo=True, campus=cam1, anos=4, modalidade=mod3, periodos=0)
cur13.save()
cur13.turnos.add(turn1, turn2)

cur14=Curso(nome='Edificações', coordenador=cor5, ativo=True, campus=cam1, anos=4, modalidade=mod3, periodos=0)
cur14.save()
cur14.turnos.add(turn1, turn2)

cur15=Curso(nome='Mineração', coordenador=cor6, ativo=True, campus=cam1, anos=4, modalidade=mod3, periodos=0)
cur15.save()
cur15.turnos.add(turn1, turn2)

cur16=Curso(nome='Informática', coordenador=cor2, ativo=True, campus=cam1, anos=4, modalidade=mod3, periodos=0)
cur16.save()
cur16.turnos.add(turn1, turn2)

cur17=Curso(nome='Mecatrônica', coordenador=cor3, ativo=True, campus=cam1, anos=4, modalidade=mod3, periodos=0)
cur17.save()
cur17.turnos.add(turn1, turn2)

#Técnicos
tec1=Tecnico_Administrativo(pessoa=pes19, campus_atuante=cam1)
tec1.save()
tec2=Tecnico_Administrativo(pessoa=pes20, campus_atuante=cam1)
tec2.save()

#Criando turmas de sistemas para internet
turma1= Turma(nome="2014.2",curso=cur1, turno=turn1)
turma1.save()


turma2 = Turma(nome="2015.1", curso=cur1, turno=turn1)
turma2.save()

#Alunos
al1=Aluno(first_name='Luan Medeiros',last_name="Macena", cpf='77788818001',email='luan@gmail.com',data_nascimento="1992-02-22",username='20142144060201',telefone='84955186660', curso=cur1, turma=turma1)
al1.set_password('123456')
al1.save()
alunos.user_set.add(al1)
al2=Aluno(first_name='Carlos Henrique', last_name="Pires", cpf='77788818002',email='carlos@gmail.com',data_nascimento="1990-05-30",username='20142144060202',telefone='84954956660', curso=cur1, turma=turma1)
al2.set_password('123456')
al2.save()
alunos.user_set.add(al2)
al3=Aluno(first_name='Juliana Soares', last_name="dos Anjos", cpf='77788818003',email='juliana@gmail.com',data_nascimento="1995-04-08",username='20142144060203',telefone='84955266660', curso=cur1, turma=turma1)
al3.set_password('123456')
al3.save()
alunos.user_set.add(al3)
al4=Aluno(first_name='Matheus Barbosa', last_name="de Farias", cpf='77788818004',email='matheus@gmail.com',data_nascimento="1994-06-14",username='20142144060204',telefone='84955557160', curso=cur1, turma=turma2)
al4.set_password('123456')
al4.save()
alunos.user_set.add(al4)
al5=Aluno(first_name='Hallesandro', last_name="Dvilla", cpf='77788818005',email='hallesandro@gmail.com',data_nascimento="1995-03-30",username='20142144060205',telefone='84955166660', curso=cur1, turma=turma2)
al5.set_password('123456')
al5.save()
alunos.user_set.add(al5)
al6=Aluno(first_name='Ednilson', last_name="Palhares", cpf='77788818006',email='ednilson@gmail.com',data_nascimento="1992-09-21",username='20142144060206',telefone='84905556660', curso=cur1, turma=turma2)
al6.set_password('123456')
al6.save()
alunos.user_set.add(al6)
al7=Aluno(first_name='Wellignton', last_name="Ferreira", cpf='77788818007',email='wellignton@gmail.com',data_nascimento="1994-04-13",username='20142144060207',telefone='84959556660', curso=cur1, turma=turma1)
al7.set_password('123456')
al7.save()
alunos.user_set.add(al7)
al8=Aluno(first_name='Monic Laura', last_name="", cpf='77788818008',email='monic@gmail.com',data_nascimento="1993-06-30",username='20142144060208',telefone='84955555660', curso=cur1, turma=turma1)
al8.set_password('123456')
al8.save()
alunos.user_set.add(al8)



#Tipos de requerimentos
tip_req1 = Tipo_Requerimento(nome="ADEQUAÇÃO DE HORÁRIOS")
tip_req1.save()
tip_req2 = Tipo_Requerimento(nome="APROVEITAMENTO DE ESTUDOS")
tip_req2.save()
tip_req3 = Tipo_Requerimento(nome="ATENDIMENTO DOMICILIAR")
tip_req3.save()
tip_req4 = Tipo_Requerimento(nome="CANCELAMENTO DE MATRÍCULA")
tip_req4.save()
tip_req5 = Tipo_Requerimento(nome="CERTIFICAÇÃO DE CONHECIMENTOS")
tip_req5.save()
tip_req6 = Tipo_Requerimento(nome="DISPENSA DE ATIVIDADES")
tip_req6.save()
tip_req7 = Tipo_Requerimento(nome="ESTUDO INDIVIDUALIZADO")
tip_req7.save()
tip_req8 = Tipo_Requerimento(nome="INCLUSÃO DE DISCIPLINAS")
tip_req8.save()
tip_req9 = Tipo_Requerimento(nome="JUSTIFICATIVA DE FALTA - DIA ESPECÍFICO")
tip_req9.save()
tip_req10= Tipo_Requerimento(nome="JUSTIFICATIVA DE FALTA POR PERÍODO")
tip_req10.save()
tip_req11= Tipo_Requerimento(nome="JUSTIFICATIVA DE FALTAS (DIAS EM ANEXO)")
tip_req11.save()
tip_req12 = Tipo_Requerimento(nome="LANÇAMENTO OU REVISÃO DE FALTAS/NOTAS/SITUAÇÃO")
tip_req12.save()
tip_req13 = Tipo_Requerimento(nome="MUDANÇA DE CURSO")
tip_req13.save()
tip_req14 = Tipo_Requerimento(nome="MUDANÇA DE TURMA")
tip_req14.save()
tip_req15 = Tipo_Requerimento(nome="MUDANÇA DE TURNO")
tip_req15.save()
tip_req16 = Tipo_Requerimento(nome="OUTROS")
tip_req16.save()
tip_req17 = Tipo_Requerimento(nome="REABERTURA MATRÍCULA")
tip_req17.save()
tip_req18 = Tipo_Requerimento(nome="REMOÇÃO DE DISCIPLINAS")
tip_req18.save()
tip_req19 = Tipo_Requerimento(nome="RENOVAÇÃO MATRÍCULA")
tip_req19.save()
tip_req20 = Tipo_Requerimento(nome="REPOSIÇÃO DE ATIVIDADES")
tip_req20.save()
tip_req21 = Tipo_Requerimento(nome="TRANCAMENTO DE MATRÍCULA - COMPULSÓRIO")
tip_req21.save()
tip_req22 = Tipo_Requerimento(nome="TRANCAMENTO DE MATRÍCULA - PERÍODO")
tip_req22.save()
tip_req23 = Tipo_Requerimento(nome="TRANSFERÊNCIA")
tip_req23.save()


#Documentos
doc1 = Documento(nome="Atestado médico")
doc1.save()
doc2 = Documento(nome="Certidão de nascimento")
doc2.save()
doc3 = Documento(nome="CPF")
doc3.save()
doc4 = Documento(nome="Intimição Judicial")
doc4.save()
doc5 = Documento(nome="Outro")
doc5.save()
doc6 = Documento(nome="RG")
doc6.save()



#Criando requerimentos de Luan
req1=Requerimento(aluno=al1, tipo_requerimento=tip_req1,observacoes="Estou tomando medição e preciso faltas em dias alternados")
req1.save()
req1.documentos_apresentados.add(doc1,doc3,doc6)

req2=Requerimento(aluno=al1, tipo_requerimento=tip_req2, disciplina_cursada="Programação Diferenciada", disciplina_curso_atual=disciplina2)
req2.save()

req3=Requerimento(aluno=al1, tipo_requerimento=tip_req3, observacoes="Estou sem movimento nas pernas")
req3.save()
req3.documentos_apresentados.add(doc1)

req4=Requerimento(aluno=al1, tipo_requerimento=tip_req4, observacoes="Surgiu uma oportunidade de emprego e estou necessitando")
req4.save()

req5=Requerimento(aluno=al1, tipo_requerimento=tip_req5, disciplina_certificacao=disciplina1, observacoes="Não estou conseguindo entender o professor")
req5.save()

req6=Requerimento(aluno=al1, tipo_requerimento=tip_req6, observacoes="Estou com febre")
req6.save()
req6.documentos_apresentados.add(doc1)

req7=Requerimento(aluno=al1, tipo_requerimento=tip_req7, observacoes="Não consigo entender com o barulho da turma, carlos bagunça muito")
req7.save()

req8=Requerimento(aluno=al1, tipo_requerimento=tip_req8, observacoes="Poderia haver a inclusãod e gestão empresarial no curso")
req8.save()

#Criando requerimentos de Carlos
req9=Requerimento(aluno=al2, tipo_requerimento=tip_req9, observacoes="Adoeci", data_falta_dia='2016-07-16')
req9.save()
req9.documentos_apresentados.add(doc1)

req10=Requerimento(aluno=al2, tipo_requerimento=tip_req10, observacoes="Estive em um evento em João Pessoa", data_faltas_de='2016-08-25', data_faltas_ate='2016-08-26')
req10.save()
req10.documentos_apresentados.add(doc5)

req11=Requerimento(aluno=al2, tipo_requerimento=tip_req11, observacoes="Meu pai proibiu de sair de casa por conta dos protestos")
req11.save()
req11.documentos_apresentados.add(doc5)

req12=Requerimento(aluno=al2, tipo_requerimento=tip_req12, observacoes="Os professores estão atrasando o lançamento das notas do bimestre")
req12.save()

req13=Requerimento(aluno=al2, tipo_requerimento=tip_req13, observacoes="Não me dei com o curso atual", curso_origem=cur1, curso_destino=cur5)
req13.save()

req14=Requerimento(aluno=al2, tipo_requerimento=tip_req14, turma_destino=turma2, observacoes="Turma Bagunceira")
req14.save()