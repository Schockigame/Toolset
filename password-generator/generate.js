const crypto = require('crypto');

// Definiere die Zeichen, die verwendet werden können
const CHARS = {
  lowercase: 'abcdefghijklmnopqrstuvwxyz',
  uppercase: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
  numbers: '0123456789',
  symbols: '!@#$%^&*()_+-=[]{}|;:,.<>?'
};

function generatePassword(length = 16, useSymbols = true) {
  let availableChars = CHARS.lowercase + CHARS.uppercase + CHARS.numbers;
  if (useSymbols) {
    availableChars += CHARS.symbols;
  }
  
  if (length <= 0) {
    console.error("Fehler: Die Länge muss größer als 0 sein.");
    return;
  }

  let password = '';
  const randomBytes = crypto.randomBytes(length);
  
  for (let i = 0; i < length; i++) {
    const randomIndex = randomBytes[i] % availableChars.length;
    password += availableChars[randomIndex];
  }

  console.log(`Dein sicheres Passwort: ${password}`);
}


const args = process.argv.slice(2);
const lengthArg = parseInt(args[0], 10) || 16;
const useSymbolsArg = !args.includes('--no-symbols');

generatePassword(lengthArg, useSymbolsArg);
