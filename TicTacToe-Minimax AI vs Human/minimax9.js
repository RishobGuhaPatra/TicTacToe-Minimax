//var random = Math.random(-5, 5);

let scores = {
  X: 10,
  O: -10,
  tie: 0,
};
var count = 0;

function bestMove() {
  // AI to make its turn
  let bestScore = -Infinity;
  let move;
  for (let i = 0; i < 9; i++) {
    for (let j = 0; j < 9; j++) {
      // Is the spot available?
      if (board[i][j] == "") {
        board[i][j] = ai;
        console.log('i')
        count = 0;
        let score = minimax(board, 0, false);
        board[i][j] = "";
        if (score >= bestScore) {
          bestScore = score;
          move = { i, j };
        }
      }
    }
  }
  board[move.i][move.j] = ai;
  currentPlayer = human;
}

function minimax(
  board,
  depth,
  isMaximizing,
  alpha = -Infinity,
  beta = Infinity
) {
  let result = checkWinner();
  if (result !== null) {
    return scores[result];
  }

  if (isMaximizing) {
    let bestScore = -Infinity;
    for (let i = 0; i < 9; i++) {
      for (let j = 0; j < 9; j++) {
        // Is the spot available?
        if (board[i][j] == '' && count <= 200) {
          board[i][j] = ai;
          count = count + 1;
          let score = minimax(board, depth + 1, false, alpha, beta);
          board[i][j] = "";
          bestScore = max(score, bestScore);
          alpha = max(alpha, score);
          if (beta >= alpha) {
            //Nothing
          }
          //count = count + 1;
        }
      }
    }

    return bestScore;
  } else {
    let bestScore = Infinity;
    for (let i = 0; i < 9; i++) {
      for (let j = 0; j < 9; j++) {
        // Is the spot available?
        if (board[i][j] == '' && count <= 200) {
          board[i][j] = human;
          count = count + 1;
          let score = minimax(board, depth + 1, true, alpha, beta);
          board[i][j] = "";
          bestScore = min(score, bestScore);
          beta = max(beta, score);
          if (alpha >= beta) {
            //Nothing
          }
          //count = count + 1;
        }
      }
    }
    //count = 0;
    console.log(count);
    return bestScore;
  }
}
