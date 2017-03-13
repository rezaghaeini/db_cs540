def db_state():
    state = {}

    state['db_server_address'] = 'localhost'
    state['db_server_port'] = 27017

    state['db_name'] = 'CS540_db'
    state['twitter_collection'] = 'twitter_collection'
    state['movie_collection'] = 'imdb_collection'

    state['movie_limit'] = 20
    state['twitter_limit'] = 50

    return state

