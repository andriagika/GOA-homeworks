def whose_move(last_player, win):
    if win:
        return last_player
    else:
        return "white" if last_player == "black" else "black"
