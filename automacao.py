import os

def criar_tabela_html(lista_tds_por_tabela, urls_to_add, utm_source, utm_medium, utm_campaign, image_base, image_type, special_images=None):
    tabelas_html = []

    td_counter = 1
    img_counter = 1

    # p tipos de imagens alternativas
    if special_images is None:
        special_images = {}

    # loop tabelas
    for numero_tds in lista_tds_por_tabela:
        # HTML table
        tabela = '<table width="100%" cellspacing="0" cellpadding="0" role="presentation">\n'
        tabela += '    <tr>\n'

        # td por tabela
        for _ in range(numero_tds):
            url = '#'
            if td_counter in urls_to_add:
                url = f'{urls_to_add[td_counter]}?utm_source={utm_source}&utm_medium={utm_medium}&utm_campaign={utm_campaign}'

            # tipo especial de img para a posicao
            current_image_type = special_images.get(img_counter, image_type)
            img_src = f'{image_base}{img_counter:02}.{current_image_type}'
            
            tabela += '        <td align="center">\n'
            tabela += f'            <a href="{url}">\n'
            tabela += f'                <img data-assetid="" src="{img_src}" alt="" alias="" width="600" style="display: block; padding: 0px; text-align: center; height: auto; width: 100%; border: 0px;">\n'
            tabela += '            </a>\n'
            tabela += '        </td>\n'
            
            td_counter += 1
            img_counter += 1

        tabela += '    </tr>\n'
        tabela += '</table>'
        
        tabelas_html.append(tabela)

    # tabelas de html [string]
    return tabelas_html

def salvar_html_em_arquivo(html_content, file_path):
    with open(file_path, 'w', encoding='utf-8') as f:
        for tabela in html_content:
            f.write(tabela + '\n')

# VARIAVEIS DE USO
lista_tds_por_tabela = [1, 1, 2, 1, 1]  # INSERIR numero de tb por tabela
urls_to_add = {
    3: 'https://www.vr.com.br',
    4: 'https://www.enext.com.br' #ISNERIR os links diferentes de '#'
}

file_name = 'vr_teste.html'  # INSERIR nome do arquivo com ext
folder_name = 'c:/Users/ketly.santos_enext/Downloads/VR/code/teste'  # INSERIR diretório
file_path = os.path.join(folder_name, file_name)

# Parâmetros UTM
utm_source = "sfmc"  # INSERIR utm_source
utm_medium = "email" # INSERIR utm_medium
utm_campaign = file_name.split('.')[0]

# INSERIR parametros de imagem
image_base = "https://image.relacionamento.vr.com.br/lib/fe3211717164057f741378/m/1/Email1__tombamento_app_pontomais_" #prefixo de img
image_type = 'jpg' #extensão

# imagens que não seguem o parametro
special_images = {
}

tabelas_geradas = criar_tabela_html(lista_tds_por_tabela, urls_to_add, utm_source, utm_medium, utm_campaign, image_base, image_type, special_images)

salvar_html_em_arquivo(tabelas_geradas, file_path)

print(f'Arquivo salvo em: {file_path}')
