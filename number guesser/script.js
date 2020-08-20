let humanScore = 0;
let computerScore = 0;
let currentRoundNumber = 1;

// Write your code below:
const generateTarget = () => {
    return Math.floor(Math.random() * 10);
}

const compareGuesses = (human, computer, secretTarget) => {
    if (Math.abs(human - secretTarget) <= Math.abs(computer - secretTarget)) {
        return true;
    } else {
        return false;
    }
}

const updateScore = (str) => {
    if (str === 'human') {
        humanScore++;
    } if (str === 'computer') {
        computerScore++;
    }
}

const advanceRound = () => {
    currentRoundNumber++;
}
