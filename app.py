import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os

#modificacao: image type alternative pode ser vazio

def criar_tabela_html(lista_tds_por_tabela, urls_to_add, utm_source, utm_medium, utm_campaign, image_base, image_type, alt_image_types, alt_image_positions):
    tabelas_html = []
    td_counter = 1
    img_counter = 1

    alt_image_positions_dict = {int(pos): alt_image_types[i] for i, pos in enumerate(alt_image_positions)} if alt_image_positions else {}

    for numero_tds in lista_tds_por_tabela:
        tabela = '<table width="100%" cellspacing="0" cellpadding="0" role="presentation">\n'
        tabela += '    <tr>\n'
        for _ in range(numero_tds):
            url = '#'
            if td_counter in urls_to_add:
                url = f'{urls_to_add[td_counter]}?utm_source={utm_source}&utm_medium={utm_medium}&utm_campaign={utm_campaign}'
            current_image_type = alt_image_positions_dict.get(td_counter, image_type)
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
    return tabelas_html

def salvar_html_em_arquivo(html_content, file_path):
    with open(file_path, 'w', encoding='utf-8') as f:
        for tabela in html_content:
            f.write(tabela + '\n')

def selecionar_pasta():
    pasta = filedialog.askdirectory()
    if pasta:
        entry_folder_name.delete(0, tk.END)
        entry_folder_name.insert(0, pasta)

def gerar_html():
    lista_tds_str = entry_lista_tds_por_tabela.get()
    lista_tds_por_tabela = list(map(int, lista_tds_str.split(',')))
    
    urls_str = entry_urls_to_add.get()
    urls_list = urls_str.split(',')
    urls_to_add = {}
    
    posicoes_str = entry_posicoes_urls.get()
    posicoes_list = list(map(int, posicoes_str.split(',')))
    
    for i, pos in enumerate(posicoes_list):
        if pos > 0 and pos <= sum(lista_tds_por_tabela):
            urls_to_add[pos] = urls_list[i].strip()

    utm_source = entry_utm_source.get()
    utm_medium = entry_utm_medium.get()
    
    file_name = entry_file_name.get() + ".html"
    utm_campaign = entry_file_name.get()
    
    image_base = entry_image_base.get()
    image_type = entry_image_type.get()
    
    alt_image_types_str = entry_alt_image_types.get()
    alt_image_types = alt_image_types_str.split(',') if alt_image_types_str else []

    alt_image_positions_str = entry_alt_image_positions.get()
    alt_image_positions = list(map(int, alt_image_positions_str.split(','))) if alt_image_positions_str else []
    
    folder_name = entry_folder_name.get()
    
    if not file_name or not folder_name:
        messagebox.showerror("Erro", "Por favor, preencha todos os campos obrigatórios.")
        return
    
    file_path = os.path.join(folder_name, file_name)
    
    tabelas_geradas = criar_tabela_html(lista_tds_por_tabela, urls_to_add, utm_source, utm_medium, utm_campaign, image_base, image_type, alt_image_types, alt_image_positions)
    
    salvar_html_em_arquivo(tabelas_geradas, file_path)
    
    messagebox.showinfo("Sucesso", f'Tabelas HTML foram salvas em: {file_path}')

app = tk.Tk()
app.title("HTML Generator")

frame = ttk.Frame(app, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
#botoes app
ttk.Label(frame, text="Lista de TDs por Tabela (separados por vírgula)").grid(row=0, column=0, sticky=tk.W)
entry_lista_tds_por_tabela = ttk.Entry(frame, width=50)
entry_lista_tds_por_tabela.grid(row=0, column=1, pady=5)

ttk.Label(frame, text="URLs to Add (separados por vírgula)").grid(row=1, column=0, sticky=tk.W)
entry_urls_to_add = ttk.Entry(frame, width=50)
entry_urls_to_add.grid(row=1, column=1, pady=5)

ttk.Label(frame, text="Posições dos URLs (separados por vírgula)").grid(row=2, column=0, sticky=tk.W)
entry_posicoes_urls = ttk.Entry(frame, width=50)
entry_posicoes_urls.grid(row=2, column=1, pady=5)

ttk.Label(frame, text="UTM Source").grid(row=3, column=0, sticky=tk.W)
entry_utm_source = ttk.Entry(frame, width=50)
entry_utm_source.grid(row=3, column=1, pady=5)
entry_utm_source.insert(0, "sfmc")

ttk.Label(frame, text="UTM Medium").grid(row=4, column=0, sticky=tk.W)
entry_utm_medium = ttk.Entry(frame, width=50)
entry_utm_medium.grid(row=4, column=1, pady=5)
entry_utm_medium.insert(0, "email")

ttk.Label(frame, text="Image Base").grid(row=5, column=0, sticky=tk.W)
entry_image_base = ttk.Entry(frame, width=50)
entry_image_base.grid(row=5, column=1, pady=5)

ttk.Label(frame, text="Image Type").grid(row=6, column=0, sticky=tk.W)
entry_image_type = ttk.Entry(frame, width=50)
entry_image_type.grid(row=6, column=1, pady=5)

ttk.Label(frame, text="Image Type Alternativos (separados por vírgula)").grid(row=7, column=0, sticky=tk.W)
entry_alt_image_types = ttk.Entry(frame, width=50)
entry_alt_image_types.grid(row=7, column=1, pady=5)

ttk.Label(frame, text="Posições para Image Type Alternativos (separados por vírgula)").grid(row=8, column=0, sticky=tk.W)
entry_alt_image_positions = ttk.Entry(frame, width=50)
entry_alt_image_positions.grid(row=8, column=1, pady=5)

ttk.Label(frame, text="File Name").grid(row=9, column=0, sticky=tk.W)
entry_file_name = ttk.Entry(frame, width=50)
entry_file_name.grid(row=9, column=1, pady=5)

ttk.Label(frame, text="Folder Name").grid(row=10, column=0, sticky=tk.W)
entry_folder_name = ttk.Entry(frame, width=50)
entry_folder_name.grid(row=10, column=1, pady=5)

ttk.Button(frame, text="Selecionar Pasta", command=selecionar_pasta).grid(row=10, column=2, padx=5)

ttk.Button(frame, text="Gerar HTML", command=gerar_html).grid(row=11, column=1, pady=20)

app.mainloop()
