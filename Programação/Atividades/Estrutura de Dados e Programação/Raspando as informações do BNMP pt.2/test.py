import requests
import concurrent.futures
from fake_useragent import UserAgent
from utils.utils import *

ua = UserAgent()
cookie = "portalbnmp=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJndWVzdF9wb3J0YWxibm1wIiwiYXV0aCI6IlJPTEVfQU5PTllNT1VTIiwiZXhwIjoxNjI5NDY1MDg5fQ.W01fTPR-SrywQagtq694UT3oq_91NCLVRFVNyoeIOvw9SVTw-DkDIa-0Oqfe4pQ0SPXc3fYT4uAYrVTai77COw"
headers = {
    'authority': 'portalbnmp.cnj.jus.br',
    'accept': 'application/json',
    'user-agent': ua.random,
    'content-type': 'application/json;charset=UTF-8',
    'origin': 'https://portalbnmp.cnj.jus.br',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://portalbnmp.cnj.jus.br/',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': cookie,
}


def post_obter_data(id_estado: int, id_municipio: int = "", id_orgao: int = "") -> str:
    """Tem como parâmetros os ids em questão.
    Retorna a variável data necessário para
    fazer uma requisição do tipo POST."""
    if not id_municipio and not id_orgao:
        # Só tem estado!
        print(f"Acessando estado {id_estado}/27")
        return '{"buscaOrgaoRecursivo":false,"orgaoExpeditor":{},"idEstado":' + str(id_estado) + '}'
    elif not id_orgao:
        # Tem estado e id_municipio!
        print(f"Acessando MUNICÍPIO({id_municipio})")
        return '{"buscaOrgaoRecursivo":false,"orgaoExpeditor":{},"idEstado":' + str(
            id_estado) + ',"idMunicipio":' + str(id_municipio) + '}'
    else:
        # Tem estado, municipio e orgao!
        print(f"Acessando ÓRGÃO({id_orgao})")
        return '{"buscaOrgaoRecursivo":false,"orgaoExpeditor":{"id":' + str(id_orgao) + '},"idEstado":' + str(
            id_estado) + ',"idMunicipio":' + str(id_municipio) + '}'


def obter_post_pag1(id_estado: int, id_municipio: int = 0, id_orgao: int = 0) -> tuple[dict, int]:
    """Faz um POST request da primeira página para
    obter até 2.000 elementos. Retorna uma lista de
    mandados e um int com o total de mandados daquele id."""
    params = (
        ('page', '0'),
        ('size', '2000'),
        ('sort', 'dataExpedicao,ASC'),
    )

    data = post_obter_data(id_estado, id_municipio, id_orgao)

    raw_data = obter_post(params, data)
    total_pages = raw_data['totalPages']
    return raw_data, total_pages


def obter_post(params, data):
    """Faz uma requisição do tipo POST e retorna
    um JSON se ela for bem sucedida e um NoneType
    caso contrário"""
    response = requests.post(
        url='https://portalbnmp.cnj.jus.br/bnmpportal/api/pesquisa-pecas/filter',
        headers=headers,
        params=params,
        data=data
    )
    if response.ok:
        return response.json()
    else:
        print("Deu Ruim!")


def obter_post_expandido(raw_data: dict, id_estado: int, id_municipio: int = 0, id_orgao: int = 0) -> list:
    """Aproveita-se da ordenação para extrapolar o
    limite de 10.000 linhas e alcaçar até o dobro disso.
    Retorna uma lista de dicts"""
    data = post_obter_data(id_estado, id_municipio, id_orgao)
    all_mandados = list()
    all_mandados.extend(raw_data['content'])
    total_pages = raw_data['totalPages']
    total_elements = raw_data['numberOfElements']
    params = tuple((('page', str(x)), ('size', '2000'), ('sort', 'dataExpedicao,ASC')) for x in range(1, 5))
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        novos_mandados = executor.map(obter_post, params, tuple(data for _ in range(len(params))))
    for e in [x['content'] for x in novos_mandados]:
        all_mandados.extend(e)
    paginas_restantes = (total_elements - 10000) // 2000
    if paginas_restantes > 1:
        params = tuple(
            (('page', str(x)), ('size', '2000'), ('sort', 'dataExpedicao,DESC')) for x in range(0, paginas_restantes))
        with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
            novos_mandados = executor.map(obter_post, params, tuple(data for _ in range(len(params))))
        for e in [x['content'] for x in novos_mandados]:
            all_mandados.extend(e)
    params = (('page', str(paginas_restantes + 1)), ('size', '2000'), ('sort', 'dataExpedicao,DESC'))
    ultima_pag = obter_post(params, data)
    all_mandados.extend([x for x in ultima_pag['content'] if x not in all_mandados])
    return all_mandados


def obter_post_forcabruta(id_estado: int, id_municipio: int, id_orgao: int) -> list:
    data = '{"buscaOrgaoRecursivo":false,"orgaoExpeditor":{"id":' + str(id_orgao) + '},"idEstado":' + str(
            id_estado) + ',"idMunicipio":' + str(id_municipio) + '}'
    data = [data for _ in range(len(params))]

    all_mandados = list()

    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        novos_mandados = executor.map(obter_post, params, data)
    for lista_mandados in [x['content'] for x in novos_mandados if x]:
        all_mandados.extend([mandado for mandado in lista_mandados if mandado not in all_mandados])
    return all_mandados



# Sorting Params ('sort', 'numeroPeca,ASC')  ('sort', 'numeroPeca,DESC')  ('sort', 'nomePessoa,ASC')  ('sort', 'nomePessoa,DESC')  ('sort', 'descricaoStatus,ASC')  ('sort', 'descricaoStatus,DESC')  ('sort', 'dataExpedicao,ASC')  ('sort', 'dataExpedicao,DESC')  ('sort', 'descricaoPeca,ASC')  ('sort', 'descricaoPeca,DESC')
# params = (
#     ('page', '0'),
#     ('size', '2000'),
#     ('sort', 'dataExpedicao,ASC'),
# )

# data = '{"buscaOrgaoRecursivo":false,"orgaoExp editor":{},"idEstado":14}'
#
# response = requests.post('https://portalbnmp.cnj.jus.br/bnmpportal/api/pesquisa-pecas/filter', headers=headers,
#                          params=params, data=data)
#
# raw_data = response.json()
# NB. Original query string below. It seems impossible to parse and
# reproduce query strings 100% accurately so the one below is given
# in case the reproduced version is not "correct".
# response = requests.post('https://portalbnmp.cnj.jus.br/bnmpportal/api/pesquisa-pecas/filter?page=0&size=10&sort=dataExpedicao,ASC', headers=headers, data=data)
raw_data_expandido, total_pages = obter_post_pag1(26, 9422, 33)
post_expandido = obter_post_expandido(raw_data_expandido, 26, 9422, 33)
with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
    executor.map(pega_conteudo_completo, post_expandido)
print("Terminei o POST expandido! :)")
raw_data_forca_bruta, tot_pages = obter_post_pag1(19, 6861, 26)
mandados_forca_bruta = obter_post_forcabruta(19, 6861, 26)
with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
    executor.map(pega_conteudo_completo, mandados_forca_bruta)

print("Terminei TUDO e SEM ERROS! Ps.: caralho Lucas você é FODAA!!!")