# Cerke_code
![language:Python3](https://img.shields.io/badge/language-Python3-blue.svg) ![license:MIT](https://img.shields.io/badge/license-MIT-blue.svg)  
A desktop app of cerke, a kind of board game.  
This app will allow you to practice or play cerke with your friends easily.

## Screenshots
<img src="https://user-images.githubusercontent.com/49038898/65514457-49b02300-df18-11e9-934b-0a07160a3890.png" alt="playing image" width="250" height="150">  <img src="https://user-images.githubusercontent.com/49038898/65514484-5765a880-df18-11e9-8a76-ec1c77569edd.png" alt="playing image" width="250" height="150">

## Requirement
- pygame(1.9.6) (only Mac users)

## Usage
- **For PC only**
- (if you are Win user) download `/font`, `/image`, `/lang_setup`, `/module`, `setting.json` and `.exe` file.
- (if you are not Win user) download`/font`, `/image`, `/lang_setup`, `/module`, `setting.json` and `.py` file.
- The rules of cerke is [here](https://sites.google.com/view/cet2kaik/%E7%B5%B1%E4%B8%80%E8%A6%8F%E5%89%87?authuser=0). (for English speaker, [here](https://sites.google.com/view/cet2kaik/the-standardized-rule-in-english?authuser=0))
- You can use this app like as you play with real set.

## Feature
- Esc key exit program.
- Space key cancels any choice.
- C key judges with the *stickes*.
- Z key undoes, and Q key redoes.(max 10 times)
- P key and M key change score.
- 0 key and 1 key change rate.
- I key initializes the pieces' position.
- T key declares *taxt* and *tymorko*.(Choose *taxt*, output score note)
- By A key, you can abondon the current turn.
- By changing the value of "language" in `setting.json`, you can play in any language you like.(You need font file and json file.)
- Generates score note.(but can't record more than 2 judgement)

