
from sqlalchemy import Column, String, Integer, CHAR, Float, ForeignKey, CLOB, Date, TIMESTAMP
from app.models.database import Base
from datetime import datetime

class Usuario(Base):
    __tablename__ = "USUARIOS"

    id_usuario = Column("ID_USUARIO", Integer, primary_key=True, index=True)
    nome = Column("NOME", String(100), nullable=False)
    email = Column("EMAIL", String(150), unique=True, nullable=False)
    senha_hash = Column("SENHA_HASH", String(255), nullable=False)
    email_verificado = Column("EMAIL_VERIFICADO", CHAR(1), default="N")
    perfil = Column("PERFIL", String(50), default="PADRAO")

from sqlalchemy import Column, String, Integer, ForeignKey, CHAR
from app.models.database import Base

class ConfigEmpresa(Base):
    __tablename__ = "CONFIG_EMPRESA"

    id_config = Column("ID_CONFIG", Integer, primary_key=True)
    id_usuario = Column("ID_USUARIO", Integer, ForeignKey("USUARIOS.ID_USUARIO"))
    nome_empresa = Column("NOME_EMPRESA", String(150))
    setor = Column("SETOR", String(150))
    tamanho_empresa = Column("TAMANHO_EMPRESA", String(50))
    notificacoes_sistema = Column("NOTIFICACOES_SISTEMA", CHAR(1), default='S')
    atualizacoes_novidades = Column("ATUALIZACOES_NOVIDADES", CHAR(1), default='S')


class OrgaoRegulador(Base):
    __tablename__ = 'ORGAOS_REGULADORES'
    id_orgao = Column('ID_ORGAO', Integer, primary_key=True)
    nome_orgao = Column('NOME_ORGAO', String(200), nullable=False)
    id_tipo = Column('ID_TIPO', Integer, ForeignKey('TIPO_ORGAO.ID_TIPO'))


class TipoOrgao(Base):
    __tablename__ = 'TIPO_ORGAO'
    id_tipo = Column('ID_TIPO', Integer, primary_key=True)
    nome_tipo = Column('NOME_TIPO', String(100), unique=True, nullable=False)


class ResumoDou(Base):
    __tablename__ = 'RESUMOS_DOU'
    id_resumo = Column('ID_RESUMO', Integer, primary_key=True)
    orgao = Column('ORGAO', String(255), nullable=False)
    data_publicacao = Column('DATA_PUBLICACAO', Date, nullable=False)
    titulo = Column('TITULO', String(500), nullable=False)
    titulo_resumido = Column('TITULO_RESUMIDO', String(300))
    conteudo = Column('CONTEUDO', CLOB)
    descricao_breve = Column('DESCRICAO_BREVE', String(1000))
    resumo_simplificado = Column('RESUMO_SIMPLIFICADO', CLOB)
    orgao_resumido = Column('ORGAO_RESUMIDO', String(255))
    data_norma = Column('DATA_NORMA', Date)
    id_tipo_orgao = Column('ID_TIPO_ORGAO', Integer, ForeignKey('TIPO_ORGAO.ID_TIPO'))
    id_usuario = Column('ID_USUARIO', Integer, ForeignKey('USUARIOS.ID_USUARIO'))


class CanalAlerta(Base):
    __tablename__ = 'CANAIS_ALERTA'
    id_canal = Column('ID_CANAL', Integer, primary_key=True)
    nome_canal = Column('NOME_CANAL', String(100), unique=True)


class UsuarioCanalAlerta(Base):
    __tablename__ = 'USUARIO_CANAL_ALERTA'
    id_usuario = Column('ID_USUARIO', Integer, ForeignKey('USUARIOS.ID_USUARIO'), primary_key=True)
    id_canal = Column('ID_CANAL', Integer, ForeignKey('CANAIS_ALERTA.ID_CANAL'), primary_key=True)


class UsuarioOrgao(Base):
    __tablename__ = 'USUARIO_ORGAO'
    id_usuario = Column('ID_USUARIO', Integer, ForeignKey('USUARIOS.ID_USUARIO'), primary_key=True)
    id_orgao = Column('ID_ORGAO', Integer, ForeignKey('ORGAOS_REGULADORES.ID_ORGAO'), primary_key=True)


class LogProcessamento(Base):
    __tablename__ = 'LOG_PROCESSAMENTO'
    id_log = Column('ID_LOG', Integer, primary_key=True)
    nome_arquivo = Column('NOME_ARQUIVO', String(255))
    data_processamento = Column('DATA_PROCESSAMENTO', TIMESTAMP, default=datetime.utcnow)
    status = Column('STATUS', String(50))
    mensagem_erro = Column('MENSAGEM_ERRO', String(1000))
    
class Assinatura(Base):
    __tablename__ = "ASSINATURA"

    id_assinatura = Column("ID_ASSINATURA", Integer, primary_key=True)
    id_usuario = Column("ID_USUARIO", Integer, ForeignKey("USUARIOS.ID_USUARIO"))
    plano = Column("PLANO", String(100), nullable=False)
    valor = Column("VALOR", Float, nullable=False)


class MetodoPagamento(Base):
    __tablename__ = "METODO_PAGAMENTO"

    id_pagamento = Column("ID_PAGAMENTO", Integer, primary_key=True)
    id_usuario = Column("ID_USUARIO", Integer, ForeignKey("USUARIOS.ID_USUARIO"))
    tipo_cartao = Column("TIPO_CARTAO", String(50), nullable=False)
    validade = Column("VALIDADE", String(7), nullable=False)  # Exemplo: 08/2026

class Fatura(Base):
    __tablename__ = "FATURAS"

    id_fatura = Column("ID_FATURA", Integer, primary_key=True)
    id_usuario = Column("ID_USUARIO", Integer, ForeignKey("USUARIOS.ID_USUARIO"))
    mes_referencia = Column("MES_REFERENCIA", String(7), nullable=False)  # Exemplo: 04/2025
    valor = Column("VALOR", Float, nullable=False)
    status = Column("STATUS", String(50), nullable=False)  # Exemplo: PAGO, PENDENTE
