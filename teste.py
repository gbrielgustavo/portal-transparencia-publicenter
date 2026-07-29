import httpx

url = 'https://transparencia.lagoaformosa.mg.gov.br/publico/despesaDetalhada?elementosPorPagina=20&pagina=1&termoBase64=&indAgrupamento=FOR&datInicio=2026-07-01&datFim=2026-07-31&desNatureza=&codAdministracao=1&filtrarApenasCovid=false&numEmpenho='


response = httpx.get(url)

print(response.text)