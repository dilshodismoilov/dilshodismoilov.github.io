let secretWord;
const attempts = 6;
let currentAttempt = 0;
let currentLetter = 0;
const uzbekAlphabet = "q e r t y u i o p a s d f g h j k l z x v b n m sh ch o' g'".split('');

document.addEventListener('DOMContentLoaded', () => {
  secretWord = wordsList[Math.floor(Math.random() * wordsList.length)];
  initializeBoard();
  initializeKeyboard();
  //document.getElementById('restart-btn').addEventListener('click', () => location.reload());
  showExplanation();
  document.addEventListener('keydown', handleKeydown);
});

function initializeBoard() {
  const board = document.getElementById('board');
  for (let i = 0; i < attempts; i++) {
    for (let j = 0; j < 5; j++) {
      const cell = document.createElement('div');
      cell.classList.add('cell');
      cell.id = `cell-${i}-${j}`;
      board.appendChild(cell);
    }
  }
}

function initializeKeyboard() {
  const keyboard = document.getElementById('keyboard');
  const rows = [
    'Q E R T Y U I O P'.split(' '),
    'A S D F G H J K L'.split(' '),
    "Z X V B N M O' G' CH SH".split(' '),
  ];
  rows.forEach((row) => {
    const rowDiv = document.createElement('div');
    rowDiv.classList.add('row');
    row.forEach((char) => {
      const key = document.createElement('div');
      key.classList.add('key');
      key.textContent = char;
      key.id = `key-${char}`;
      rowDiv.appendChild(key);
      key.addEventListener('click', () => handleInput(char));
    });
    keyboard.appendChild(rowDiv);
  });

  // Add Backspace key
  const backspaceRow = document.createElement('div');
  backspaceRow.classList.add('row-special');
  const enterKey = document.createElement('div');
  enterKey.classList.add('key');
  enterKey.textContent = '↵';
  enterKey.id = 'key-enter';
  backspaceRow.appendChild(enterKey);
  enterKey.addEventListener('click', handleSubmit);

  const backspaceKey = document.createElement('div');
  backspaceKey.classList.add('key');
  backspaceKey.innerHTML = '&#9003;';
  backspaceKey.id = 'key-backspace';
  backspaceRow.appendChild(backspaceKey);
  keyboard.appendChild(backspaceRow);
  backspaceKey.addEventListener('click', handleDelete);
  // Add Enter key
  //const enterRow = document.createElement('div');
  //enterRow.classList.add('row');
  //   const enterKey = document.createElement('div');
  //   enterKey.classList.add('key', 'special-key');
  //   enterKey.textContent = 'Enter';
  //   enterKey.id = 'key-enter';
  //   backspaceRow.appendChild(enterKey);
  //   //keyboard.appendChild(enterRow);
  //   enterKey.addEventListener('click', handleSubmit);
}

function handleKeydown(event) {
  const key = event.key.toLowerCase();
  if (uzbekAlphabet.includes(key)) {
    handleInput(key);
  } else if (event.key === 'Enter') {
    handleSubmit();
  } else if (event.key === 'Backspace') {
    handleDelete();
  }
}

function handleInput(key) {
  if (currentLetter < 5) {
    const cell = document.getElementById(`cell-${currentAttempt}-${currentLetter}`);
    cell.textContent = key.toUpperCase();
    currentLetter++;
  }
}

function handleDelete() {
  if (currentLetter > 0) {
    currentLetter--;
    const cell = document.getElementById(`cell-${currentAttempt}-${currentLetter}`);
    cell.textContent = '';
  }
}

function handleSubmit() {
  if (currentLetter === 5) {
    const guess = [];
    for (let i = 0; i < 5; i++) {
      const cell = document.getElementById(`cell-${currentAttempt}-${i}`);
      guess.push(cell.textContent.toLowerCase());
    }
    const guessWord = guess.join('');
    if (!wordsList.includes(guessWord)) {
      showAlert("Bu so'z lug'atda yo'q");
      return;
    }
    revealWord(guess);
    currentAttempt++;
    currentLetter = 0;
    if (guessWord === secretWord) {
      showAlert('Tabriklaymiz! Siz topdingiz!');
      document.removeEventListener('keydown', handleKeydown);
    } else if (currentAttempt === attempts) {
      showAlert(`Siz yutqazdingiz! So'z: ${secretWord}`);
      document.removeEventListener('keydown', handleKeydown);
    }
  } else {
    showAlert("So'z to'liq emas");
  }
}

function revealWord(guess) {
  const guessChars = wordIntoArrayOfUzbLetters(guess);
  const secretWordChars = wordIntoArrayOfUzbLetters(secretWord);
  //console.log(guessChars);
  //console.log(secretWordChars);
  for (let i = 0; i < 5; i++) {
    const cell = document.getElementById(`cell-${currentAttempt}-${i}`);
    const key = document.getElementById(`key-${guess[i].toUpperCase()}`);
    setTimeout(() => {
      cell.classList.add('flip');
      setTimeout(() => {
        cell.classList.remove('flip');
        if (guessChars[i] === secretWordChars[i]) {
          cell.classList.add('correct');
          key.classList.add('correct');
          key.classList.remove('present');
        } else if (secretWordChars.includes(guessChars[i])) {
          cell.classList.add('present');
          if (!key.classList.contains('correct')) {
            key.classList.add('present');
          }
        } else {
          cell.classList.add('absent');
          key.classList.add('used');
        }
      }, 250);
    }, i * 300);
  }
}

function showAlert(message) {
  const alertBox = document.getElementById('alert-box');
  alertBox.textContent = message;
  alertBox.style.display = 'block';
  setTimeout(() => {
    alertBox.style.display = 'none';
  }, 3000);
}

function wordIntoArrayOfUzbLetters(word) {
  let res = [];
  for (let i = 0; i < word.length; i++) {
    if (word[i] !== 'o' && word[i] !== 'g' && word[i] !== 'c' && word[i] !== 's') {
      res.push(word[i]);
    } else {
      if (i < word.length - 1) {
        if (
          ((word[i] === 'o' || word[i] === 'g') && word[i + 1] === "'") ||
          ((word[i] === 's' || word[i] === 'c') && word[i + 1] === 'h')
        ) {
          res.push(word[i] + word[i + 1]);
          i += 1;
        } else {
          res.push(word[i]);
        }
      }
    }
  }
  return res;
}

function showExplanation() {
  const modal = document.getElementById('explanation');
  const closeBtn = document.querySelector('.close-btn');
  const playBtn = document.getElementById('play-btn');

  closeBtn.addEventListener('click', () => (modal.style.display = 'none'));
  playBtn.addEventListener('click', () => (modal.style.display = 'none'));

  // Step 1
  const demoBoardStep1 = document.getElementById('demo-board-step1');
  const step1Word = 'SALOM';
  const step1Guess = 'GURUH';
  for (let i = 0; i < 5; i++) {
    const cell = document.createElement('div');
    cell.classList.add('cell');
    cell.textContent = step1Guess[i];
    if (step1Guess[i] !== step1Word[i]) {
      cell.classList.add('absent');
    }
    demoBoardStep1.appendChild(cell);
  }

  // Step 2
  const demoBoardStep2 = document.getElementById('demo-board-step2');
  const step2Word = 'SALOM';
  const step2Guess = 'DOMLA';
  for (let i = 0; i < 5; i++) {
    const cell = document.createElement('div');
    cell.classList.add('cell');
    cell.textContent = step2Guess[i];
    if (step2Guess[i] === step2Word[i]) {
      cell.classList.add('correct');
    } else if (step2Word.includes(step2Guess[i])) {
      cell.classList.add('present');
    } else {
      cell.classList.add('absent');
    }
    demoBoardStep2.appendChild(cell);
  }

  // Step 3
  const demoBoardStep3 = document.getElementById('demo-board-step3');
  const step3Word = 'SALOM';
  const step3Guess = 'SALOM';
  for (let i = 0; i < 5; i++) {
    const cell = document.createElement('div');
    cell.classList.add('cell');
    cell.textContent = step3Guess[i];
    cell.classList.add('correct');
    demoBoardStep3.appendChild(cell);
  }

  modal.style.display = 'block';
}

// function restartGame() {
//   secretWord = wordsList[Math.floor(Math.random() * wordsList.length)];
//   currentAttempt = 0;
//   currentLetter = 0;
//   initializeBoard();
//   initializeKeyboard();
//   document.addEventListener('keydown', handleKeydown);
//   showAlert("Yangi o'yin boshlandi!");
// }
