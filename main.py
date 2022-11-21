from rich import print
from rich.console import Console
from rich.panel import Panel

console = Console()
cinema = (
    (
        'WAKANDA FOREVER', 'DURAÇÃO: 2h 14min', 'GÊNERO: Ação, Aventura, Fantasia',
        ['11:00', 'SALA 1', [True for _ in range(1, 4)]],
        ['13:00', 'SALA 1', [True for _ in range(1, 4)]],
        ['17:00', 'SALA 1', [True for _ in range(1, 4)]],
        ['21:00', 'SALA 1', [True for _ in range(1, 4)]],
    ),
    (
        'A VIDA É BELA', 'DURAÇÃO: 1h 56min', 'GÊNERO: Comédia, Drama, Guerra',
        ['10:00', 'SALA 2', [True for _ in range(1, 4)]],
        ['12:00', 'SALA 2', [True for _ in range(1, 4)]],
        ['14:00', 'SALA 2', [True for _ in range(1, 4)]],
        ['16:00', 'SALA 2', [True for _ in range(1, 4)]],

    ),
)
while True:
    opcoes = ['1 - Listar Filmes', '2 - Comprar Ingresso', '3 - Sair']
    print('\n')
    print(Panel('\n'.join(opcoes), title="PYNEMA - CINEMAS",
          border_style="blue", subtitle='Menu Principal'))
    opcao = input('\nEscolha uma opção: ')
    if opcao == '1':
        for filme in cinema:
            print('\n')
            horarios = '\n'.join(
                [f'{horario[0]} - {horario[1]} - {"[green]Disponível[/]" if sum(horario[2]) else "[red]Indisponível[/]"}' for horario in filme[3:]])
            print(Panel(f"{horarios}", title=f'[bold blue]{filme[0]}[/] - {filme[1]}',
                  subtitle=f'{filme[2]}', border_style="blue"))
    elif opcao == '2':
        lista_filmes = [
            f"[magenta]{codigo + 1}[/] - [bold blue]{filme[0]}[/]" for codigo, filme in enumerate(cinema)]
        print(Panel("\n".join(lista_filmes), title='COMPRAR INGRESSO',
              border_style="blue", subtitle='Filmes em cartaz'))
        filme = int(input('\nEscolha codigo do filme: '))
        filme = cinema[filme - 1]
        horarios = '\n'.join(
            [f'[magenta]{codigo_horario + 1}[/] - [magenta]{horario[0]}[/] - [magenta]{horario[1]}[/] - {"[green]Disponível[/]" if sum(horario[2]) else "[red]Indisponível[/]"}' for codigo_horario, horario in enumerate(filme[3:])])
        print(Panel(f'{horarios}', title=f'[bold blue]{filme[0]}[/] - {filme[1]}',
              subtitle=f'Horários', border_style="blue"))
        horario = int(input('\nEscolha codigo do horario: '))
        horario = filme[horario + 2]
        if sum(horario[2]):
            cadeiras_sala = '\n'.join(
                [f'[magenta]{codigo + 1}[/] - {"[green]Disponível[/]" if cadeira else "[red]Indisponível[/]"}' for codigo, cadeira in enumerate(horario[2])])
            print('\n')
            print(Panel(
                cadeiras_sala, title=f'{filme[0]} - {horario[0]} - {horario[1]}', subtitle=f'Cadeiras', border_style="blue"))
            cadeira = int(input('\nEscolha codigo da cadeira: '))
            if horario[2][cadeira - 1]:
                confirmar = input('\nConfirmar compra? [s/n]: ')
                if confirmar.lower() in ['s', 'sim']:
                    horario[2][cadeira - 1] = False
                    print(Panel(f'[green]Ingresso comprado com sucesso![/]\nCadeira de número: {cadeira}',
                          title=f'[bold blue]{filme[0]}[/] - {filme[1]}', subtitle=f'{filme[1]} - Obrigado pela preferência!', border_style="blue"))
                else:
                    print(Panel(f'[red]Compra cancelada![/]',
                          title=f'{filme[0]}', subtitle=f'{filme[1]}', border_style="blue"))
            else:
                print(Panel(f'[red]Cadeira indisponível![/]',
                      title=f'{filme[0]}', subtitle=f'{filme[1]}', border_style="blue"))
        else:
            print(Panel(f'[red]Horário indisponível![/]',
                  title=f'{filme[0]}', subtitle=f'{filme[1]}', border_style="blue"))
    elif opcao == '3':
        print(Panel(f'Até mais!', title=f'FIM', border_style="blue"))
        break
    else:
        print('Opção inválida!')
