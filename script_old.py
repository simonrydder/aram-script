import pandas as pd

# Load names
names = pd.read_csv('names.csv')
champs = pd.read_csv('champs.csv')

new_game = True
while(new_game):
    
    # Define teams
    teamA = names.sample(3)
    teamB = names.loc[~names.index.isin(teamA.index)]
    
    # Find champs
    available_champs = champs['count']==champs['count'].min()
    n_available_champ = available_champs.sum()
    
    while(True):
        if n_available_champ > 6:
            champ_pool = champs.loc[available_champs].sample(6)
        else:
            champ_pool = champs.loc[available_champs].sample(n_available_champ)
            
            draw_new = True
            while(draw_new):
                extra = champs.sample(6 - n_available_champ)
                draw_new = champ_pool['champ'].isin(extra).sum() != 0

            champ_pool = pd.concat([champ_pool, extra], axis=0)

        types = champ_pool['type']
        teamA_types = types.iloc[:3]
        teamB_types = types.iloc[3:]
        
        aIsNotSame = teamA_types.nunique() == 3
        bIsNotSame = teamB_types.nunique() == 3
        
        if (aIsNotSame & bIsNotSame):
            break
        
    print('Team A: ', end='')
    print(teamA.values.T[0], sep=', ')
    print('Champs: ', end='')
    print(champ_pool.iloc[[0, 1, 2]]['champ'].values, sep = ', ')
    print()
    
    print('Team B: ', end='')
    print(teamB.values.T[0], sep=', ')
    print('Champs: ', end='')
    print(champ_pool.iloc[[3, 4, 5]]['champ'].values, sep = ', ')
    print()
    
    champ_pool['count'] = 1
    champs['count'] = champs['count'].add(champ_pool['count'], fill_value=0).astype(int)
    
    winner_str = input('Who won? (A/B): ')
    if winner_str.lower() == 'a':
        teamA['score'] = 1
        teamB['score'] = 0
    else:
        teamA['score'] = 0
        teamB['score'] = 1
    
    score = pd.concat([teamA, teamB], axis=0).sort_index()
    names['score'] = names['score'] + score['score']
    
    print(names)
    
    names.to_csv('names.csv', index=False)
    champs.to_csv('champs.csv', index=False)
    
    new_game_str = input('New Game? (Y/N): ')
    new_game = True if new_game_str.lower() == 'y' else False