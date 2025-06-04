# Discord Server Tag Rotator
A simple Python script that rotates through your existing server tags on Discord

## Installation
1. **Clone this repo**, either by downloading the ZIP through Code > Download ZIP, or by entering `git clone https://github.com/SeekPlush-linux/discord-tag-rotator` into your terminal.
2. **Edit the config file** `config.json` and add server tags you want to rotate through. See the **Editing the config file** section to learn how to edit the config file.
3. **Install the required Python libraries** by entering `pip install -r requirements.txt` into your terminal, in the folder where the script is located. (Make sure you have Python installed!)
4. **Run the Python script** `server-tag-rotator.py`, and if there are no errors, congratulations!

If you do run into errors while setting up the script, please make sure you've followed the above steps accordingly.

## Editing the config file
Before running the script, you **must** edit the config file first for the script to function properly.

The most important parts you'll need to edit are the `tags` and `token` variables. I'll explain each variable in the config here:
- `tags` — A dictionary with server tags the script will rotate through, and their corresponding server ID.

  To get the ID of a server tag, you'll need to do the following:
  1. Enable Developer Mode in Discord by going to your settings > Advanced and enable "Developer Mode".
  2. Right-click the icon of the server you want to get the ID of, and click "Copy Server ID".
     The long string of numbers in your clipboard should be the ID of the server tag!

  Make sure to remove the example server tags in the config first, since those are there to show you how to add your own server tags.

  **Format:**
  ```json
  "tags": {
    // ...
    "CLAN": 1366473681429806335,
    // ...
  }
  ```

- `delay` — Self-explanatory, the script changes your server tag once every N seconds, N being the delay.

  The default value in the config is `300`, which means 300 seconds, aka 5 minutes.

  **Format:**
  ```json
  "delay": 300
  ```

- `token` — A string that contains your Discord token. \
  <ins>**WARNING!**</ins> **Never share your Discord token with anyone you don't trust!** They can use your token to log into your account, bypassing any kind of authentication.

  To get your Discord token, you'll have to do the following:
  1. Open Devtools in Discord and go to the Network tab. Learn how to enable Devtools [here](https://github.com/brunos3d/discord-enable-devtools).
  2. Start typing for a few seconds in any channel.
  3. Once you see a request called `typing` in Devtools, click on it.
  4. Scroll down in the newly opened menu until you find a header called "Authorization".
  5. Copy the long string of numbers and letters next to it. \
     That should be your Discord token!
  
  It usually looks something like this: `NzI4NjU1MDA5NzU5MzYzMTkx.xxxxxx.xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx` (censored so that i don't get my account hacked lol)

  **Format:**
  ```json
  "token": "NzI4NjU1MDA5NzU5MzYzMTkx.xxxxxx.xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
  ```

Now you know how to edit the config file and finish setting up the script!

## Conclusion
I hope you liked using my script and maybe also flexed your tags to your friends, and if you did, then make sure to star this repo, i would appreciate it ^_^

(i spent 2 hours writing this README till 4:30 AM so please do star this repo, thanks)

## Contact Me
In case you have any questions or suggestions for the script, you can find me on Discord [here](https://discord.com/users/728655009759363191), DMs are always open!
