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
- `tags` — A dictionary with server tags the script will rotate through, and their corresponding ID.

  To get the ID of a server tag, you'll need to do the following:
  1. Go to your Discord settings > Profiles.
  2. Open Devtools by pressing `Ctrl + Shift + I` on your keyboard. Learn how to enable Devtools [here](https://github.com/brunos3d/discord-enable-devtools).
  3. Go to the Network tab, select a server tag you want to get the ID of in Discord, then click "Save Changes".
  4. In Devtools, find a request called `clan`, click on it, go to the Payload tab, and find the value of `identity_guild_id`. \
     The long string of numbers should be the ID of the server tag you selected!

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

  To get your Discord token, you can follow the same steps shown for getting the ID of a server tag. \
  But instead of going to the Payload tab, you would want to:
  1. Go to the Headers tab.
  2. Scroll down until you find a header called "Authorization".
  3. Copy the long string of numbers and letters next to it. \
     That should be your Discord token!
  
  It usually looks something like this: `NzI4NjU1MDA5NzU5MzYzMTkx.xxxxxx.xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx` (censored so that i don't get my account hacked lol)

  **Format:**
  ```json
  "token": "NzI4NjU1MDA5NzU5MzYzMTkx.xxxxxx.xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
  ```

Now you know how to edit the config file and finish setting up the script!

## Conclusion
I hope you liked using my script and maybe also flexed your tags to your friends, and if you did, then make sure to star this repo, i would appreciate it ^_^

(i've spent 2 hours writing this README till 4:30 AM so please do star this repo, thanks)

## Contact Me
In case you have any questions or suggestions for the script, you can find me on Discord [here](https://discord.com/users/728655009759363191), DMs are always open!
