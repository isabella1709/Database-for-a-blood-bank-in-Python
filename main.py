from utils.create_db import create_db # importando a função "create_db" do módulo "utils.create_db"
from sqlalchemy import create_engine, select, func
from services.database import engine
from sqlalchemy.orm import Session
from urllib.parse import quote
from models import pessoa, doador, funcionario, paciente, requisitos, hospital, coleta, doacao, compatibilidade, sangue

if __name__ == "__main__": # verificando se este script está sendo executado como um programa principal
    create_db()  # chamando a função "create_db" para criar as tabelas no banco de dados

engine = create_engine(f"mysql+pymysql://root:{quote('@1234')}@localhost:3306/sangue")

# inserts na tabela pessoa

with Session(engine) as session:
    ana = pessoa(
        cpf="11111111111", nome="Ana Flávia", data_nasc="2004-03-20",
        end_pais="Brasil", end_estado="PR", end_cidade="Curitiba", end_rua="Rua Teste",
        end_bairro="Santa Felicidade", end_complemento="a"
    )

    isa = pessoa(
        cpf="22222222222", nome="Isabella", data_nasc="2004-09-17",
        end_pais="Brasil", end_estado="PR", end_cidade="Curitiba", end_rua="Rua Teste 2",
        end_bairro="Batel", end_complemento="b"
    )

    vitor = pessoa(
        cpf="33333333333", nome="Vitor", data_nasc="2004-10-27",
        end_pais="Brasil", end_estado="PR", end_cidade="Curitiba", end_rua="Rua Teste 3",
        end_bairro="Prado Velho", end_complemento="c"
    )

    vinicius = pessoa(
        cpf="44444444444", nome="Vinicius", data_nasc="2004-09-14",
        end_pais="Brasil", end_estado="PR", end_cidade="Curitiba", end_rua="Rua Teste 4",
        end_bairro="Centro", end_complemento="c"
    )

    mohamed = pessoa(
        cpf="55555555555", nome="Mohamed", data_nasc="2004-05-07",
        end_pais="Brasil", end_estado="PR", end_cidade="Curitiba", end_rua="Rua Teste 5",
        end_bairro="Ecoville", end_complemento="d"
    )

    gabriel = pessoa(
        cpf="66666666666", nome="Gabriel", data_nasc="2004-07-07",
        end_pais="Brasil", end_estado="PR", end_cidade="Curitiba", end_rua="Rua Teste 6",
        end_bairro="Boqueirão", end_complemento="e"
    )

    michele = pessoa(
        cpf="77777777777", nome="Michele", data_nasc="2004-10-17",
        end_pais="Brasil", end_estado="PR", end_cidade="Curitiba", end_rua="Rua Teste 7",
        end_bairro="Butiatuvinha", end_complemento="f"
    )

    yejin = pessoa(
        cpf="88888888888", nome="Yejin", data_nasc="2004-09-13",
        end_pais="Brasil", end_estado="PR", end_cidade="Curitiba", end_rua="Rua Teste 8",
        end_bairro="Cabral", end_complemento="g"
    )

    clara = pessoa(
        cpf="99999999999", nome= "Clara", data_nasc="2004-08-19",
        end_pais="Brasil", end_estado="PR", end_cidade="Curitiba", end_rua="Rua Teste 9",
        end_bairro="Orleans", end_complemento="h" 
    )

    claudio = pessoa(
        cpf="01010101010", nome= "Claudio", data_nasc="1997-02-20",
        end_pais="Brasil", end_estado="PR", end_cidade="Curitiba", end_rua="Rua Teste 10",
        end_bairro="CIC", end_complemento="i" 
    )

    maria = pessoa(
        cpf="12121212121", nome= "Maria", data_nasc="2000-12-21",
        end_pais="Brasil", end_estado="PR", end_cidade="Curitiba", end_rua="Rua Teste 11",
        end_bairro="Campina do Siqueira", end_complemento="j" 
    )

    joao = pessoa(
        cpf="23232323232", nome= "João", data_nasc="1990-07-06",
        end_pais="Brasil", end_estado="PR", end_cidade="Curitiba", end_rua="Rua Teste 12",
        end_bairro="Ecoville", end_complemento="k" 
    )

    julia = pessoa(
        cpf="34343434343", nome= "Julia", data_nasc="2006-05-09",
        end_pais="Brasil", end_estado="PR", end_cidade="Curitiba", end_rua="Rua Teste 13",
        end_bairro="Agua Verde", end_complemento="l" 
    )

    luisa = pessoa(
        cpf="45454545454", nome= "Luísa", data_nasc="2010-10-10",
        end_pais="Brasil", end_estado="PR", end_cidade="Curitiba", end_rua="Rua Teste 14",
        end_bairro="Campo Comprido", end_complemento="m" 
    )

    carlos = pessoa(
        cpf="56565656565", nome= "Carlos", data_nasc="1982-11-15",
        end_pais="Brasil", end_estado="PR", end_cidade="Curitiba", end_rua="Rua Teste 15",
        end_bairro="Prado Velho", end_complemento="n" 
    )

    cleiton = pessoa(
        cpf="19191919191", nome="Cleiton", data_nasc="1985-06-08", 
        end_pais="Brasil", end_estado="PR", end_cidade="Curitiba", end_rua="Rua Teste 16",
        end_bairro="Batel", end_complemento="n" 
    )

    legolas = pessoa(
        cpf="15151515151", nome="Legolas", data_nasc="1980-06-08", 
        end_pais="Brasil", end_estado="PR", end_cidade="Curitiba", end_rua="Rua Teste 18",
        end_bairro="Bigorrilho", end_complemento="n" 
    )

    session.add_all([ana, isa, vitor, vinicius, mohamed, gabriel, michele,
                    yejin, clara, claudio, maria, joao, julia, luisa, carlos, cleiton, legolas])
    session.commit()

#inserts na tabela doador 

with Session(engine) as session:
    ana_doador = doador(
        cpf_doador = "11111111111", genero="F", apto=False,
        tipo_sanguineo_doador="O-", peso="49.0"
    )

    isa_doador = doador(
        cpf_doador="22222222222", genero="F", apto=True,
        tipo_sanguineo_doador="O-", peso="50.0"
    )

    michele_doador = doador(
        cpf_doador="77777777777", genero="F", apto=True,
        tipo_sanguineo_doador="AB+", peso="50.0"
    )

    yejin_doador = doador(
        cpf_doador="88888888888", genero="F", apto=True,
        tipo_sanguineo_doador="AB+", peso="50.0"
    )

    clara_doador = doador(
        cpf_doador="99999999999", genero="F", apto=True,
        tipo_sanguineo_doador="O-", peso="50.0"
    )

    maria_doador = doador(
        cpf_doador="12121212121", genero="F", apto=False,
        tipo_sanguineo_doador="AB-", peso="47.0"
    )

    cleiton_doador = doador(
        cpf_doador="19191919191", genero="M", apto=True,
        tipo_sanguineo_doador="A+", peso="75.0"
    )

    legolas_doador = doador(
        cpf_doador="15151515151", genero="M", apto=True,
        tipo_sanguineo_doador="A+", peso="78.0"
    )

    session.add_all([ana_doador, isa_doador, michele_doador, yejin_doador, clara_doador, maria_doador, cleiton_doador, legolas_doador])
    session.commit()

# insert na tabela requisitos

with Session (engine) as session:
    requisitos_ana = requisitos(
        cpf_doador="11111111111", saudavel=True, alimentacao=True,
        descanso=False, peso_minimo=False, idade_minima=True, idade_maxima=True
    )

    requisitos_isa = requisitos(
        cpf_doador="22222222222", saudavel=True, alimentacao=True,
        descanso=True, peso_minimo=True, idade_minima=True, idade_maxima=True
    )

    requisitos_michele = requisitos(
        cpf_doador="77777777777", saudavel=True, alimentacao=True,
        descanso=True, peso_minimo=True, idade_minima=True, idade_maxima=True
    )

    requisitos_yejin = requisitos(
        cpf_doador="88888888888", saudavel=True, alimentacao=True,
        descanso=True, peso_minimo=True, idade_minima=True, idade_maxima=True
    )

    requisitos_clara = requisitos(
        cpf_doador="99999999999", saudavel=True, alimentacao=True,
        descanso=True, peso_minimo=True, idade_minima=True, idade_maxima=True
    )

    requisitos_maria = requisitos(
        cpf_doador="99999999999", saudavel=False, alimentacao=True,
        descanso=True, peso_minimo=False, idade_minima=True, idade_maxima=True
    )

    requisitos_cleiton = requisitos(
        id_requisitos="7", cpf_doador="19191919191", saudavel=True, alimentacao=True,
        descanso=True, peso_minimo=True, idade_minima=True, idade_maxima=True
    )

    requisitos_legolas = requisitos(
        cpf_doador="15151515151", saudavel=True, alimentacao=True,
        descanso=True, peso_minimo=True, idade_minima=True, idade_maxima=True
    )

    session.add_all([requisitos_ana, requisitos_isa, requisitos_michele, requisitos_yejin,
                    requisitos_clara, requisitos_maria])
    session.commit()

# insert na tabela funcionario

with Session (engine) as session:
    ana_func = funcionario(
        cpf_funcionario="11111111111", data_contratacao="2022-10-13", cargo="enfermeiro"
    )

    isa_func = funcionario(
        cpf_funcionario="22222222222", data_contratacao="2022-10-12", cargo="enfermeiro"
    )

    vitor_func = funcionario(
        cpf_funcionario="33333333333", data_contratacao="2022-10-14", cargo="enfermeiro"
    )

    vinicius_func = funcionario(
        cpf_funcionario="44444444444", data_contratacao="2022-10-15", cargo="enfermeiro"
    )

    mohamed_func = funcionario(
        cpf_funcionario="55555555555", data_contratacao="2022-10-16", cargo="enfermeiro"
    )

    gabriel_func = funcionario(
        cpf_funcionario="66666666666", data_contratacao="2022-10-17", cargo="enfermeiro"
    )

    session.add_all([ana_func, isa_func, vitor_func, vinicius_func, mohamed_func, gabriel_func])
    session.commit()

# insert na tabela paciente

with Session (engine) as session:
    claudio_pac = paciente(
        cpf_paciente="01010101010", genero="M", tipo_sanguineo_paciente="O-", peso="70.0"
    )

    joao_pac = paciente(
        cpf_paciente="23232323232", genero="M", tipo_sanguineo_paciente="AB+", peso="70.0"
    )

    carlos_pac = paciente(
        cpf_paciente="56565656565", genero="M", tipo_sanguineo_paciente="O+", peso="70.0"
    )

    julia_pac = paciente(
        cpf_paciente="34343434343", genero="F", tipo_sanguineo_paciente="AB-", peso="60.0"
    )

    luisa_pac = paciente(
        cpf_paciente="45454545454", genero="F", tipo_sanguineo_paciente="A+", peso="54.0"
    )

    gabriel_pac = paciente(
        cpf_paciente="66666666666", genero="M", tipo_sanguineo_paciente="B+", peso="60.0"
    )

    session.add_all([claudio_pac, joao_pac, carlos_pac, julia_pac, luisa_pac, gabriel_pac])
    session.commit()

# insert na tabela hospital

with Session (engine) as session:
    santa_cruz = hospital(
        nome_hospital="Hospital Santa Cruz", end_pais="Brasil", end_estado="PR",
        end_cidade="Curitiba", end_rua="Rua Teste 1", end_bairro="Santa Felicidade", end_complemento="a"
    )

    pequeno_principe = hospital(
        nome_hospital="Hospital Pequeno Principe", end_pais="Brasil", end_estado="PR",
        end_cidade="Curitiba", end_rua="Rua Teste 2", end_bairro="Ecoville", end_complemento="b"
    )

    cruz_vermelha = hospital(
        nome_hospital="Hospital Cruz Vermelha", end_pais="Brasil", end_estado="PR",
        end_cidade="Curitiba", end_rua="Rua Teste 3", end_bairro="Prado Velho", end_complemento="c"
    )

    santa_casa = hospital(
        nome_hospital="Hospital Santa Casa", end_pais="Brasil", end_estado="PR",
        end_cidade="Curitiba", end_rua="Rua Teste 4", end_bairro="Agua Verde", end_complemento="d"
    )

    sao_marcelino = hospital(
        nome_hospital="Hospital São Marcelino", end_pais="Brasil", end_estado="PR",
        end_cidade="Curitiba", end_rua="Rua Teste 5", end_bairro="Boqueirão", end_complemento="e"
    )

    evangelico = hospital(
        nome_hospital="Hospital Evangélico", end_pais="Brasil", end_estado="PR",
        end_cidade="Curitiba", end_rua="Rua Teste 6", end_bairro="Bigorrilho", end_complemento="f"
    )

    session.add_all([santa_cruz, pequeno_principe, cruz_vermelha, santa_casa, sao_marcelino, evangelico])
    session.commit()

# insert na tabela coleta
    
with Session (engine) as session:
    coleta_isa = coleta(
        data_coleta = "2023-09-17", cpf_doador = "22222222222", cpf_funcionario = "44444444444", 
        id_hospital = "1"
    )

    coleta_michele = coleta(
        data_coleta = "2023-09-17", cpf_doador = "77777777777", cpf_funcionario = "11111111111", 
        id_hospital = "2"
    )

    coleta_yejin = coleta(
        data_coleta = "2023-09-17", cpf_doador = "88888888888", cpf_funcionario = "22222222222", 
        id_hospital = "3"
    )

    coleta_clara = coleta(
        data_coleta = "2023-09-17", cpf_doador = "99999999999", cpf_funcionario = "55555555555", 
        id_hospital = "4"
    )

    coleta_cleiton = coleta(
        data_coleta = "2023-09-17", cpf_doador = "19191919191", cpf_funcionario = "66666666666", 
        id_hospital = "5"
    )
    
    coleta_legolas = coleta(
        data_coleta = "2023-09-17", cpf_doador = "15151515151", cpf_funcionario = "33333333333", 
        id_hospital = "6"
    )
    session.add_all([coleta_isa, coleta_michele, coleta_yejin, coleta_clara, coleta_cleiton, coleta_legolas])
    session.commit()

# insert na tabela doacao

with Session (engine) as session:
    doacao_claudio = doacao(
        data_doacao="2023-09-18", cpf_paciente="01010101010",
        cpf_funcionario="11111111111", id_hospital="5"
    )

    doacao_joao = doacao(
        data_doacao="2023-09-18", cpf_paciente="23232323232", 
        cpf_funcionario="33333333333", id_hospital="3"
    )

    doacao_carlos = doacao(
        data_doacao="2023-09-18", cpf_paciente="56565656565", 
        cpf_funcionario="44444444444", id_hospital="1"
    )

    doacao_julia = doacao(
        data_doacao="2023-09-18", cpf_paciente="34343434343", 
        cpf_funcionario="22222222222", id_hospital="4"
    )

    doacao_luisa = doacao(
        data_doacao="2023-09-18", cpf_paciente="45454545454", 
        cpf_funcionario="11111111111", id_hospital="2"
    )

    doacao_gabriel = doacao(
        data_doacao="2023-09-18", cpf_paciente="66666666666", 
        cpf_funcionario="22222222222", id_hospital="6"
    )

    session.add_all([doacao_claudio, doacao_joao, doacao_carlos, doacao_julia, doacao_luisa, doacao_gabriel])
    session.commit()
    
# insert na tabela compatibilidade

with Session (engine) as session:
    comp_isa_claudio = compatibilidade(
        compativel=True, 
        id_coleta="1", cpf_doador="22222222222", coleta_cpf_funcionario="44444444444", coleta_id_hospital="1",
        id_doacao="1", cpf_paciente="01010101010", doacao_cpf_funcionario="11111111111", doacao_id_hospital="5"
    )   

    comp_michele_joao = compatibilidade(
        compativel=True, 
        id_coleta="2", cpf_doador="77777777777", coleta_cpf_funcionario="11111111111", coleta_id_hospital="2",
        id_doacao="2", cpf_paciente="23232323232", doacao_cpf_funcionario="33333333333", doacao_id_hospital="3"
    )
    
    comp_yejin_carlos = compatibilidade(
        compativel=False, 
        id_coleta="3", cpf_doador="88888888888", coleta_cpf_funcionario="22222222222", coleta_id_hospital="3",
        id_doacao="3", cpf_paciente="56565656565", doacao_cpf_funcionario="44444444444", doacao_id_hospital="1"
    )

    comp_clara_julia = compatibilidade(
        compativel=True, 
        id_coleta="4", cpf_doador="99999999999", coleta_cpf_funcionario="55555555555", coleta_id_hospital="4",
        id_doacao="4", cpf_paciente="34343434343", doacao_cpf_funcionario="22222222222", doacao_id_hospital="4"
    )

    comp_cleiton_luisa = compatibilidade(
        compativel=True, 
        id_coleta="5", cpf_doador="19191919191", coleta_cpf_funcionario="66666666666", coleta_id_hospital="5",
        id_doacao="5", cpf_paciente="45454545454", doacao_cpf_funcionario="11111111111", doacao_id_hospital="2"
    )

    comp_legolas_gabriel = compatibilidade(
        compativel=False, 
        id_coleta="6", cpf_doador="15151515151", coleta_cpf_funcionario="33333333333", coleta_id_hospital="6",
        id_doacao="6", cpf_paciente="66666666666", doacao_cpf_funcionario="22222222222", doacao_id_hospital="6"
    )

    session.add_all([comp_isa_claudio, comp_michele_joao, comp_yejin_carlos, 
                    comp_clara_julia, comp_cleiton_luisa, comp_legolas_gabriel])
    session.commit()

# insert na tabela sangue

with Session (engine) as session:
    sangue_isa_claudio = sangue(
        id_sangue = "1", quantidade = "2",
        id_hospital = "1", 
        id_coleta = "1", cpf_doador = "22222222222", coleta_cpf_funcionario = "44444444444",
        id_doacao = "1", cpf_paciente = "23232323232", doacao_cpf_funcionario = "11111111111"
    )

    sangue_michele_joao = sangue(
        id_sangue = "2", quantidade = "1", 
        id_hospital = "2", 
        id_coleta = "2", cpf_doador = "77777777777", coleta_cpf_funcionario = "11111111111",
        id_doacao = "2", cpf_paciente = "01010101010", doacao_cpf_funcionario = "33333333333"
    )

    sangue_yejin_carlos = sangue(
        id_sangue = "3", quantidade = "3", 
        id_hospital = "3", 
        id_coleta = "3", cpf_doador = "88888888888", coleta_cpf_funcionario = "22222222222",
        id_doacao = "3", cpf_paciente = "56565656565", doacao_cpf_funcionario = "44444444444"
    )

    sangue_clara_julia = sangue(
        id_sangue = "4", quantidade = "2", 
        id_hospital = "4", 
        id_coleta = "4", cpf_doador = "99999999999", coleta_cpf_funcionario = "55555555555",
        id_doacao = "4", cpf_paciente = "34343434343", doacao_cpf_funcionario = "22222222222"
    )
    
    sangue_cleiton_luisa = sangue(
        id_sangue = "5", quantidade = "1", 
        id_hospital = "5", 
        id_coleta = "5", cpf_doador = "19191919191", coleta_cpf_funcionario = "66666666666",
        id_doacao = "5", cpf_paciente = "45454545454", doacao_cpf_funcionario = "11111111111"
    )

    sangue_legolas_gabriel = sangue(
        id_sangue = "6", quantidade = "3", 
        id_hospital = "6", 
        id_coleta = "6", cpf_doador = "15151515151", coleta_cpf_funcionario = "33333333333",
        id_doacao = "6", cpf_paciente = "66666666666", doacao_cpf_funcionario = "22222222222"
    )

    session.add_all([sangue_isa_claudio, sangue_michele_joao, sangue_yejin_carlos,
                    sangue_clara_julia, sangue_cleiton_luisa, sangue_legolas_gabriel])
    session.commit()

# atualizando 5 registros

stmt = select(pessoa).where(pessoa.nome == "Mohamed")
mohamed = session.scalars(stmt).one()

mohamed.end_pais = "Líbano"

session.commit()

stmt = select(pessoa).where(pessoa.nome == "Isabella")
isa = session.scalars(stmt).one()

isa.end_pais = "Alemanha"

session.commit()

stmt = select(pessoa).where(pessoa.nome == "Vinicius")
vinicius = session.scalars(stmt).one()

vinicius.end_pais = "Japão"

session.commit()

stmt = select(pessoa).where(pessoa.nome == "Gabriel")
gabriel = session.scalars(stmt).one()

gabriel.end_pais = "Austrália"

session.commit()

stmt = select(pessoa).where(pessoa.nome == "Ana Flávia")
ana = session.scalars(stmt).one()

ana.end_pais = "Canadá"

session.commit()

# instruções de exclusão na tabela pessoa

session.delete(ana)

session.delete(isa_doador)

session.delete(requisitos_michele)

session.delete(vinicius_func)

session.delete(claudio_pac)

# session.commit()

# Consultas

# 1 - Quantidade de sangue armazenada

with Session(engine) as conn:
    total_sangue = conn.execute(
        select(func.sum(sangue.quantidade).label("Total de bolsas de sangue"))
    ).scalar()


    print(f"Total de bolsas sangue: {total_sangue}\n")

# 2 - Número de doações

with Session(engine) as conn:
    total_doacoes = conn.execute(
        select(func.count(doacao.id_doacao).label("Total de doações"))
    ).scalar()


    print(f"Total de doações: {total_doacoes}\n")

# 3 - Compatibilidade entre doador e paciente

with Session(engine) as conn:
    compatibilidade_sangue = conn.execute(
        select(compatibilidade.id_compatibilidade, compatibilidade.cpf_doador, compatibilidade.cpf_paciente)
        .where(compatibilidade.compativel == 1)
    )

    queries = compatibilidade_sangue.fetchall()

    for query in queries:
        print(f"Compatibilidade: {query}\n")

# 4 - Quantidade de pessoas aptas a doar
        
with Session(engine) as conn:
    quantidade_pessoas = conn.execute(
        select(func.count(requisitos.id_requisitos)).where(requisitos.saudavel == 1 
        and requisitos.alimentacao == 1 and requisitos.descanso == 1 
        and requisitos.peso_minimo == 1 and requisitos.idade_minima == 1 and requisitos.idade_maxima == 1)
    ).scalar()


    print(f"Quantidade de pessoas aptas a doar: {quantidade_pessoas}\n")

# 5 - Relatório do processo de cada doação

with Session(engine) as conn:

    relatorio_doacao = conn.execute(select(doacao.id_doacao, doacao.data_doacao, doacao.cpf_paciente,
        doacao.cpf_funcionario, doacao.id_hospital))

    queries = relatorio_doacao.fetchall()

    for query in queries:
        print(f"Doação: {query}\n")

# 6 - Tipo sanguíneo mais armazenado

with Session(engine) as conn:
    tipo_sangue_max = conn.execute(
        select(doador.tipo_sanguineo_doador, func.sum(sangue.quantidade))
        .join(sangue, doador.cpf_doador == sangue.cpf_doador)
        .group_by(doador.tipo_sanguineo_doador)
        .order_by(func.sum(sangue.quantidade).desc())
    )

    queries = tipo_sangue_max.fetchall()

    print(f"Tipo sanguíne mais armazenado: {queries[0]}\n")


# 7 - Tipo sanguíneo menos armazenado

with Session(engine) as conn:
    tipo_sangue_max = conn.execute(
        select(doador.tipo_sanguineo_doador, func.sum(sangue.quantidade))
        .join(sangue, doador.cpf_doador == sangue.cpf_doador)
        .group_by(doador.tipo_sanguineo_doador)
        .order_by(func.sum(sangue.quantidade))
    )

    queries = tipo_sangue_max.fetchall()

    print(f"Tipo sanguíneo menos armazenado: {queries[0]}\n")

# 8 - Tipo sanguíneo mais requisitado

with Session(engine) as conn:
    tipo_sangue_req = conn.execute(
        select(doador.tipo_sanguineo_doador, func.sum(sangue.quantidade))
        .join(sangue, doador.cpf_doador == sangue.cpf_doador)
        .where(doador.tipo_sanguineo_doador == "O-")
    )

    queries = tipo_sangue_req.fetchall()

    print(f"Tipo sanguíneo mais requisitado: {queries[0]}\n")

# 9 - Tipo sanguíneo menos requisitado

with Session(engine) as conn:
    tipo_sangue_req = conn.execute(
        select(doador.tipo_sanguineo_doador, func.sum(sangue.quantidade))
        .join(sangue, doador.cpf_doador == sangue.cpf_doador)
        .where(doador.tipo_sanguineo_doador == "AB+")
    )

    queries = tipo_sangue_req.fetchall()

    print(f"Tipo sanguíneo menos requisitado: {queries[0]}\n")

# 10 - Hospital mais próximo ao doador

with Session(engine) as conn:
    hospital_proximo = conn.execute(
        select(pessoa.cpf, hospital.nome_hospital, hospital.end_rua)
        .join(hospital, pessoa.end_rua == hospital.end_rua)
    )

    queries = hospital_proximo.fetchall()
    
    for query in queries:
        print(f"Hospital próximo ao doador: {query}\n")

# 11- Hospital mais utilizado para doações

with Session(engine) as conn:
    hospital_max = conn.execute(
        select(hospital.nome_hospital, func.count(doacao.id_doacao))
        .join(doacao, hospital.id_hospital == doacao.id_hospital)
        .group_by(hospital.nome_hospital)
        .order_by(func.count(doacao.id_doacao).desc())
    )

    queries = hospital_max.fetchall()

    print(f"Hospital mais utilizado: {queries[0]}\n")

# 12- Hospital menos utilizado para doações

with Session(engine) as conn:
    hospital_max = conn.execute(
        select(hospital.nome_hospital, func.count(doacao.id_doacao))
        .join(doacao, hospital.id_hospital == doacao.id_hospital)
        .group_by(hospital.nome_hospital)
        .order_by(func.count(doacao.id_doacao))
    )

    queries = hospital_max.fetchall()

    print(f"Hospital menos utilizado: {queries[0]}\n")

# 13- Funcionários cadastrados no processo de doação

with Session(engine) as conn:
    funcionarios_cadastrados = conn.execute(
        select(pessoa.cpf, pessoa.nome, funcionario.cpf_funcionario, funcionario.cargo, funcionario.data_contratacao)
        .where(pessoa.cpf == funcionario.cpf_funcionario)
    )

    queries = funcionarios_cadastrados.fetchall()
    
    for query in queries:
        print(f"Funcionário cadastrado: {query}\n")


# 14- Quantidade de funcionários

with Session(engine) as conn:
    funcionarios_cadastrados = conn.execute(select(func.count(funcionario.cpf_funcionario)) ).scalar()

    print(f"Número de funcionários: {funcionarios_cadastrados}\n")

# 15- Número anual de doações

with Session(engine) as conn:
    numero_doacoes = conn.execute(select(func.count(doacao.id_doacao)) ).scalar()

    print(f"Número de doações anual: {numero_doacoes}\n")


# 16- Grau de necessidade de um paciente

with Session(engine) as conn:
    paciente_max = conn.execute(
        select(paciente.cpf_paciente, pessoa.nome, func.count(doacao.id_doacao))
        .join(pessoa, paciente.cpf_paciente == pessoa.cpf)
        .join(doacao, paciente.cpf_paciente == doacao.cpf_paciente)
        .group_by(paciente.cpf_paciente)
        .order_by(func.count(doacao.id_doacao).desc())
    )

    queries = paciente_max.fetchall()

    for query in queries:
        print(f"Grau de necessidade dos pacientes em ordem decrescente: {query}\n")

# 17- Doador mais recorrente

with Session(engine) as conn:
    doador_max = conn.execute(select(doador.cpf_doador, pessoa.nome,
    func.count(coleta.id_coleta)) 
        .join(pessoa, doador.cpf_doador == pessoa.cpf)
        .join(coleta, doador.cpf_doador == coleta.cpf_doador)
        .group_by(doador.cpf_doador)
        .order_by(func.count(coleta.id_coleta).desc())

    )

    queries = doador_max.fetchall()

    print(f"Doador mais recorrente: {queries[0]}\n")

# 18- Funcionário mais recorrente

with Session(engine) as conn:
    funcionario_max = conn.execute(select(funcionario.cpf_funcionario, pessoa.nome,
    func.count(coleta.id_coleta)) 
        .join(pessoa, funcionario.cpf_funcionario == pessoa.cpf)
        .join(coleta, funcionario.cpf_funcionario == coleta.cpf_funcionario)
        .group_by(funcionario.cpf_funcionario)
        .order_by(func.count(coleta.id_coleta).desc())

    )

    queries = funcionario_max.fetchall()

    print(f"Funcionário mais recorrente: {queries[0]}\n")

# 19- Número de doações de um doador

with Session(engine) as conn:
    numero_doacoes_doador = conn.execute(select(coleta.cpf_doador, func.count(coleta.id_coleta))
        .group_by(coleta.cpf_doador) )
    
    queries = numero_doacoes_doador.fetchall()

    for query in queries:
        print(f"Número de doações de cada doador: {query}\n")

# 20 - Faixa etária de cada doador

with Session(engine) as conn:
    idade = conn.execute(select(pessoa.nome, pessoa.data_nasc, 
        func.extract('year', func.current_date()) - func.extract('year', pessoa.data_nasc).label('idade'))
        .group_by(pessoa.cpf) )
    
    queries = idade.fetchall()

    for query in queries:
        print(f"Faixa etária de cada doador: {query}\n")
