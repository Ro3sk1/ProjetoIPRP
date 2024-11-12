import foosball_alunos_extras
import turtle as t

def le_replay(nome_ficheiro):

    with open(f"{nome_ficheiro}.txt","r") as ficheiro_var:
        bola_coor_data = ficheiro_var.readline().strip("\n").split(";")
        verm_coor_data = ficheiro_var.readline().strip("\n").split(";")
        azul_coor_data = ficheiro_var.readline().strip("\n").split(";")

        bola_coor = list()
        verm_coor = list()
        azul_coor = list()

        for i in range(0,len(bola_coor_data)):
            bola_coor.append(tuple(map(float, bola_coor_data[i].split(','))))
        for i in range(0,len(verm_coor_data)):
            verm_coor.append(tuple(map(float, verm_coor_data[i].split(','))))
        for i in range(0,len(azul_coor_data)):
            azul_coor.append(tuple(map(float, azul_coor_data[i].split(','))))
        
        return({"bola": bola_coor,"jogador_vermelho": verm_coor, "jogador_azul":azul_coor})

    '''
    Função que recebe o nome de um ficheiro contendo um replay, e que deverá 
    retornar um dicionário com as seguintes chaves:
    bola - lista contendo tuplos com as coordenadas xx e yy da bola
    jogador_vermelho - lista contendo tuplos com as coordenadas xx e yy da do jogador\_vermelho
    jogador_azul - lista contendo tuplos com as coordenadas xx e yy da do jogador\_azul
    '''
    pass

def main():
    estado_jogo = foosball_alunos_extras.init_state()
    foosball_alunos_extras.setup(estado_jogo, False)
    replay = le_replay('replay_golo_jv_1_ja_1')
    for i in range(len(replay['bola'])):
        estado_jogo['janela'].update()
        estado_jogo['jogador_vermelho'].setpos(replay['jogador_vermelho'][i])
        estado_jogo['jogador_azul'].setpos(replay['jogador_azul'][i])
        estado_jogo['bola']['bola'].setpos(replay['bola'][i])
    
    estado_jogo['janela'].exitonclick()


if __name__ == '__main__':
    main()