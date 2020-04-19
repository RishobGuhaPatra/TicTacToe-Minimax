
let board = [
    ['', '', '','','','',''],
    ['', '', '','','','',''],
    ['', '', '','','','',''],
    ['', '', '','','','',''],
    ['', '', '','','','',''],
    ['', '', '','','','',''],
    ['', '', '','','','','']
  ];
  
  let w; // = width / 3;
  let h; // = height / 3;

  let ai = 'X';
  let human = 'O';
  let currentPlayer = ai;
  
  function setup() {
    createCanvas(800, 800);
    w = width / 7;
    h = height / 7;
    bestMove();
  }
  
  function equals3(a, b, c, d, e, f, g) {
    return a == b && b == c && c == d && d == e && e==f && f==g && a != '';
  }
  
  function checkWinner() {
    let winner = null;
  
    // horizontal
    for (let i = 0; i < 7; i++) {
      if (equals3(board[i][0], board[i][1], board[i][2], board[i][3],board[i][4], board[i][5],board[i][6])) {
        winner = board[i][0];
      }
    }
  
    // Vertical
    for (let i = 0; i < 7; i++) {
      if (equals3(board[0][i], board[1][i], board[2][i], board[3][i], board[4][i], board[5][i],board[6][i])) {
        winner = board[0][i];
      }
    }
  
    // Diagonal
    if (equals3(board[0][0], board[1][1], board[2][2], board[3][3], board[4][4], board[5][5],board[6][6])) {
      winner = board[0][0];
    }
    if (equals3(board[6][0], board[5][1], board[4][2], board[3][3], board[2][4],board[1][5], board[0][6])) {
      winner = board[6][0];
    }
  
    let openSpots = 0;
    for (let i = 0; i < 7; i++) {
      for (let j = 0; j < 7; j++) {
        if (board[i][j] == '') {
          openSpots++;
        }
      }
    }
  
    if (winner == null && openSpots == 0) {
      return 'tie';
    } else {
      return winner;
    }
  }
  
  function mousePressed() {
    if (currentPlayer == human) {
      // Human make turn
      let i = floor(mouseX / w);
      let j = floor(mouseY / h);
      // If valid turn
      if (board[i][j] == '') {
        board[i][j] = human;
        currentPlayer = ai;
        bestMove();
      }
    }
  }
  
  function draw() {
    background(255);
    strokeWeight(6);
  
    line(w, 0, w, height);
    line(w * 2, 0, w * 2, height);
    line(w * 3, 0, w * 3, height);
    line(w * 4, 0, w * 4, height);
    line(w * 5, 0, w * 5, height);
    line(w * 6, 0, w * 6, height);
    line(0, h, width, h);
    line(0, h * 2, width, h * 2);
    line(0, h * 3, width, h * 3);
    line(0, h * 4, width, h * 4);
    line(0, h * 5, width, h * 5);
    line(0, h * 6, width, h * 6);
  
    for (let j = 0; j < 7; j++) {
      for (let i = 0; i < 7; i++) {
        let x = w * i + w / 2;
        let y = h * j + h / 2;
        let spot = board[i][j];
        textSize(32);
        let r = w / 4;
        if (spot == human) {
          noFill();
          ellipse(x, y, r * 2);
        } else if (spot == ai) {
          line(x - r, y - r, x + r, y + r);
          line(x + r, y - r, x - r, y + r);
        }
      }
    }
  
    let result = checkWinner();
    if (result != null) {
      noLoop();
      let resultP = createP('');
      resultP.style('font-size', '32pt');
      if (result == 'tie') {
        resultP.html('Tie!');
      } else {
        resultP.html(`${result} wins!`);
      }
    }
  }