# TVRQC BOT
TVRQC is a Discord bot for conducting quizzes made for IIITH TV Room Quiz Club. Used ConvertAPI to convert ppt and replit database to store marks, answer.

## Setup
Clone repository
```bash
git clone https://github.com/chandan-shrivastava/TVRQC-BOT
```
Install Requirements
```bash
pip3 -r requirements.txt
```
Setup the environment variables (Conver API token and Bot token)  
Then Run the bot using
```bash
python3 bot.py
```


## Features
| Command                    | DESCRIPTION                                          | Usage                                            |
|----------------------------|------------------------------------------------------|--------------------------------------------------|
| !help                      | List all commands                                    |  !help                                           |
| !info                      | Get some useful (or not) information about the bot   |  !info                                           |
| !ping                      | Check if the bot is alive                            |  !ping                                           |
| !poll                      | Create a poll with 9 options (from 1 to 9)           |  !poll                                           |
| !answer                    | Finalise Answer                                      |  !ans "Answer" or !answer "Answer"               |
| !pass                      | Passes to next team                                  |  !pass                                           |
| !join                      | Join a team                                          |  !join "Team number"                             |
| !leave                     | Leave a team                                         |  !leave "Team number"                            |
| !kick                      | Kicks a user out of the server                       |  !kick "User" "Reason"                           |
| !nick                      | Change nickname of a user                            |  !nick "User" "Nickname"                         |
| !ban                       | Ban a user from the server                           |  !ban "User" "Reason"                            |
| !warn                      | Warn a user                                          |  !warn "User" "Reason"                           |
| !purge                     | Purge Messages from a channel                        |  !purge "Number"                                 |
| !shutdown                  | Shutdown the bot                                     |  !shutdown                                       |
| !say                       | Make the bot say something                           |  !say "Message"                                  |
| !marks                     | Get current marks                                    |  !marks                                          |
|                            | Add marks to a team                                  |  !marks add "team-x" "Marks"                     |
|                            | Remove all teams marks                               |  !marks remove                                   |
| !uploadppt                 | Upload ppt and convert to jpg                        |  !uploadppt                                      |
| !deleteppt                 | Delete ppt from database                             |  !deleteppt                                      |
| !slide                     | Send slide to every team channel                     |  !slide "Number"                                 |
| !timer                     | Starts timer                                         |  !time "Seconds"                                 |
| !givemarks                 | Give marks to every team after round ends            |  !givemarks                                      |
| !!broadcast                | Broadcast message to every team                      |  !broadcast "Message"                            |

## Contributions
Feel free to make a PR/issue for feature implementation/request.

## Todo
1. !next - Sends next slide
2. !prev - Sends prev slide
3. Convert every command to slash
4. Add more try except block
