import pandas as pd
from pandas import DataFrame

def main():
    while(True):
        new_game_str = input('Start new game (Y/N): ')
        new_game = True if new_game_str.lower() == 'y' else False
        
        if not new_game:
            break
        game()


def game():
    names = load_names()
    teamA, teamB = generate_teams(names)
    
    champs = load_champs()
    champA = generate_champs(champs)
    champs = add_team_combo(champs, champA)
    
    champB = generate_champs(champs)
    champs = add_team_combo(champs, champB)
    
    print_team(teamA, champA, 'A')
    print_team(teamB, champB, 'B')
    
    score = get_winner(teamA, teamB)
    names = update_score(names, score)
    
    save_data(names, champs)
    print_status(champs)


def load_names() -> DataFrame:
    return pd.read_csv('names.csv')


def load_champs() -> DataFrame:
    return pd.read_csv('champs.csv', dtype={'champ':str, 'count':int, 'type':str})


def generate_teams(names: DataFrame) -> DataFrame:
    teamA = names.sample(3)
    teamB = names.loc[~names.index.isin(teamA.index)].copy()
    
    teamA['score'] = 0
    teamB['score'] = 0
    
    return teamA, teamB
    

def generate_champs(champs: DataFrame) -> tuple[DataFrame, DataFrame]:
    min_count = champs['count'].min()
    min_count_champs = champs['count']==min_count
    available_champs = champs.loc[min_count_champs]
    
    different_types = available_champs['type'].unique()
    n_different_types = len(different_types)
    
    # If not enough unique types
    if n_different_types < 3:
        while(True):
            champ_pool = available_champs.sample(n_different_types)
            
            if len(champ_pool) == n_different_types:
                break
        
        while(True):
            n_missing_champs = 3 - len(champ_pool)
            extra = champs.loc[champs['count']==min_count+1].sample(n_missing_champs)
            res = pd.concat([champ_pool, extra], axis=0)
            
            if res['type'].nunique() == 3:
                break
            
        return res
    
    while(True):
        res = available_champs.sample(3)

        if res['type'].nunique() == 3:
            return res


def add_team_combo(champs: DataFrame, team_champs: DataFrame) -> DataFrame:
    team_champs['count'] = 1
    
    champs['count'] = champs['count'].add(team_champs['count'], fill_value=0).astype(int)
    
    return champs
    

def print_team(names: DataFrame, champ: DataFrame, team: str) -> None:
    print(f'Team {team}: ', end='')
    print(names.values.T[0], sep=', ')
    print('Champs: ', end='')
    print(champ.iloc[[0, 1, 2]]['champ'].values, sep = ', ')
    print()


def get_winner(A: DataFrame, B: DataFrame) -> DataFrame:
    winner_str = input('Who won? (A/B): ')
    if winner_str.lower() == 'a':
        A['score'] = 1
    else:
        B['score'] = 1
    
    score = pd.concat([A, B], axis=0).sort_index()
    return score
    
    
def update_score(names: DataFrame, score: DataFrame) -> DataFrame:
    names['score'] = names['score'] + score['score']
    print(names.sort_values(by='score', ascending=False))
    print()
    
    return names


def save_data(names: DataFrame, champs: DataFrame) -> None:
    names.to_csv('names.csv', index=False)
    champs.to_csv('champs.csv', index=False)
    
    
def print_status(champs: DataFrame) -> None:
    counts = champs['count']
    n_games = counts.sum()/6
    champs['count'].value_counts()
    print(f'Games played: {n_games}')
    print(f"{counts.value_counts()}")


if __name__ == '__main__':
    main()